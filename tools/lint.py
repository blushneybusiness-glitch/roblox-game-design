#!/usr/bin/env python3
"""Checks the handbook against its own writing standard.

    python tools/lint.py            # errors only
    python tools/lint.py --words    # also list banned words to review

Errors (exit code 1):
  - a relative link that points at a file that does not exist
  - a genre playbook or teardown missing a required section, or with sections out of order

Warnings (--words): the words CONTRIBUTING.md bans unless a number follows.
A human still has to decide whether each one is earned.

Python 3.8 or newer. No packages needed.
"""

import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GENRE_SECTIONS = [
    "At a glance", "Why people play it", "The loop, with a stopwatch", "The first five minutes",
    "Numbers that work", "What brings them back", "Other players", "Money", "Live ops",
    "How these games die", "Checklist", "Twists and open space", "Sources",
]
TEARDOWN_SECTIONS = [
    "1. Core loop", "2. First session", "3. Progression", "4. Session and return hooks",
    "5. Other players", "6. Money", "7. Why it works", "8. What went wrong",
    "9. What to take from it", "Sources",
]
BANNED = [
    "engaging", "rewarding", "satisfying", "immersive", "polished", "balanced", "addictive",
    "compelling", "intuitive", "juicy", "smooth", "seamless", "robust", "meaningful",
    "dynamic", "innovative",
]
SKIP_DIRS = {".git", "raw", "__pycache__"}
# Pages that quote the banned words in order to ban them.
WORD_EXEMPT = {"CONTRIBUTING.md", os.path.join("kit", "nothing-detector.md"),
               os.path.join("foundations", "01-why-designs-fail.md")}

LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
HEADING = re.compile(r"^(#{2,3})\s+(.*?)\s*$")


def markdown_files():
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in sorted(files):
            if name.endswith(".md"):
                yield os.path.join(base, name)


def strip_code(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def check_links(path, text, errors):
    for target in LINK.findall(strip_code(text)):
        if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
            continue
        clean = target.split("#")[0]
        if not clean:
            continue
        full = os.path.normpath(os.path.join(os.path.dirname(path), clean))
        if not os.path.exists(full):
            errors.append("%s: link to missing file %s" % (os.path.relpath(path, ROOT), target))


def check_sections(path, text, required, errors):
    found = [m.group(2) for m in (HEADING.match(line) for line in text.splitlines()) if m and m.group(1) == "##"]
    position = -1
    for section in required:
        try:
            index = found.index(section)
        except ValueError:
            errors.append("%s: missing section '## %s'" % (os.path.relpath(path, ROOT), section))
            continue
        if index < position:
            errors.append("%s: section '## %s' is out of order" % (os.path.relpath(path, ROOT), section))
        position = max(position, index)


def check_words(path, text, warnings):
    rel = os.path.relpath(path, ROOT)
    if rel in WORD_EXEMPT:
        return
    for number, line in enumerate(strip_code(text).splitlines(), 1):
        if line.lstrip().startswith(">"):
            continue
        line = re.sub(r"\(https?://[^)\s]*\)|<https?://[^>\s]*>", "", line)  # a word inside an address is not prose
        for word in BANNED:
            for match in re.finditer(r"\b%s\b" % word, line, flags=re.I):
                rest = line[match.end():match.end() + 60]
                if not re.search(r"\d", rest):
                    warnings.append("%s:%d: '%s' with no number after it" % (rel, number, word))


def main():
    parser = argparse.ArgumentParser(description="Check links, required sections and banned words.")
    parser.add_argument("--words", action="store_true", help="also list banned words to review")
    args = parser.parse_args()

    errors, warnings, count = [], [], 0
    for path in markdown_files():
        count += 1
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
        check_links(path, text, errors)
        if rel.startswith("genres/") and not rel.endswith("README.md"):
            check_sections(path, text, GENRE_SECTIONS, errors)
        if rel.startswith("teardowns/") and not rel.endswith("README.md"):
            check_sections(path, text, TEARDOWN_SECTIONS, errors)
        if args.words:
            check_words(path, text, warnings)

    for line in errors:
        print("ERROR  " + line)
    for line in warnings:
        print("review " + line)
    print("%d files, %d errors%s" % (count, len(errors), ", %d words to review" % len(warnings) if args.words else ""))
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
