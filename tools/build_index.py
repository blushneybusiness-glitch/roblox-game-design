#!/usr/bin/env python3
"""Rebuilds the index pages from the pages themselves.

    python tools/build_index.py

Writes genres/README.md, teardowns/README.md and llms.txt. Run it after adding
or renaming a genre playbook or a teardown.

Python 3.8 or newer. No packages needed.
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GENRE_GROUPS = [
    ("Collect and earn", ["steal-and-defend", "grow-and-harvest", "plus-one", "simulator", "tycoon", "rng",
                          "fishing-and-digging"]),
    ("Runs and rounds", ["obby", "horror", "survival", "story", "party-and-minigames", "social-deduction",
                         "puzzle-word-rhythm"]),
    ("Combat and competition", ["fighting", "anime-rpg", "shooter", "sports", "tower-defense"]),
    ("Places to be", ["roleplay", "pet-raising-and-animal", "dress-up", "hangout", "driving", "sandbox"]),
]


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print("wrote " + os.path.relpath(path, ROOT))


def title_of(text):
    match = re.search(r"^#\s+(.*)$", text, flags=re.M)
    return match.group(1).strip() if match else "Untitled"


def blockquote_of(text):
    match = re.search(r"^>\s+(.*)$", text, flags=re.M)
    if not match:
        return ""
    line = re.sub(r"\*\*The feeling sold:\*\*\s*", "", match.group(1).strip())
    return line


def glance_row(text, label):
    match = re.search(r"^\|\s*%s\s*\|\s*(.*?)\s*\|\s*$" % re.escape(label), text, flags=re.M)
    return match.group(1) if match else "not stated"


def unlink(cell):
    """Turn [text](target) into text so a cell copied to another folder has no broken links."""
    return re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", cell)


def first_sentence(cell, limit=150):
    cell = unlink(cell)
    cut = re.split(r"(?<=[.;])\s", cell, maxsplit=1)[0].rstrip(".;")
    return cut if len(cut) <= limit else cut[:limit].rsplit(" ", 1)[0] + " ..."


def build_genres():
    folder = os.path.join(ROOT, "genres")
    present = {name[:-3] for name in os.listdir(folder) if name.endswith(".md") and name != "README.md"}
    out = ["# Genres", "",
           "One playbook per genre. Every playbook has the same sections in the same order, so you can put two side by side:",
           "the loop with a stopwatch, the first five minutes, numbers that work, what brings players back, other players,",
           "money, live ops, how games in the genre die, a pass/fail checklist, and open space.", "",
           "Not sure which one is yours? Pick by what the player does most: owns things that earn (collect and earn),",
           "survives or wins a run or a round (runs and rounds), fights or competes (combat and competition), or simply",
           "spends time somewhere (places to be). Many hits mix two; read both.", ""]
    listed = set()
    for group, slugs in GENRE_GROUPS:
        rows = []
        for slug in slugs:
            if slug not in present:
                continue
            listed.add(slug)
            text = read(os.path.join(folder, slug + ".md"))
            rows.append("| [%s](%s.md) | %s | %s | %s |" % (
                title_of(text), slug, blockquote_of(text), first_sentence(glance_row(text, "Core verb")),
                first_sentence(glance_row(text, "Players per server"))))
        if rows:
            out += ["## " + group, "", "| Playbook | The feeling sold | Core verb | Players per server |", "|---|---|---|---|"]
            out += rows + [""]
    extra = sorted(present - listed)
    if extra:
        out += ["## More", ""] + ["- [%s](%s.md)" % (title_of(read(os.path.join(folder, s + ".md"))), s) for s in extra] + [""]
    out += ["Trend games as a whole, across these genres, are covered in [../slop/](../slop/README.md).", ""]
    write(os.path.join(folder, "README.md"), "\n".join(out))


def build_teardowns():
    folder = os.path.join(ROOT, "teardowns")
    out = ["# Teardowns", "",
           "How individual hits work, in numbers. Each follows [the same template](../kit/templates/teardown.md): loop,",
           "first session, progression, return hooks, other players, money, why it works, what went wrong, and what to take",
           "from it. Unless a page says otherwise, the game was studied from its wiki, Roblox's public endpoints and",
           "published sources in November 2026, and was not timed on a device.", "",
           "| Game | In one line |", "|---|---|"]
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".md") or name == "README.md":
            continue
        text = read(os.path.join(folder, name))
        out.append("| [%s](%s) | %s |" % (title_of(text), name, unlink(blockquote_of(text))))
    out += ["", "To add one, see [CONTRIBUTING.md](../CONTRIBUTING.md).", ""]
    write(os.path.join(folder, "README.md"), "\n".join(out))


def build_llms():
    out = ["# Roblox Game Design", "",
           "> A handbook for designing, auditing and fixing Roblox games, built from teardowns of real hits. Every",
           "> statement carries a time, a number or what is on screen, and every fact carries its source. AI agents",
           "> should follow AGENTS.md.", ""]
    sections = [("Start", ["AGENTS.md", "README.md", "CONTRIBUTING.md"]), ("Foundations", "foundations"),
                ("Trend games", "slop"), ("Genres", "genres"), ("Teardowns", "teardowns"), ("Kit", "kit"),
                ("Templates", os.path.join("kit", "templates")), ("Data and research", ["data/README.md",
                 "data/ANALYSIS.md", "research/README.md"])]
    for heading, source in sections:
        out += ["## " + heading, ""]
        if isinstance(source, list):
            paths = source
        else:
            paths = sorted(os.path.join(source, n) for n in os.listdir(os.path.join(ROOT, source)) if n.endswith(".md"))
        for rel in paths:
            full = os.path.join(ROOT, rel)
            if not os.path.exists(full):
                continue
            text = read(full)
            summary = blockquote_of(text)
            if not summary:
                body = [l.strip() for l in text.splitlines() if l.strip() and not l.startswith(("#", "|", "-", ">", "```"))]
                summary = body[0] if body else ""
            summary = unlink(summary)
            if len(summary) > 180:
                summary = summary[:180].rsplit(" ", 1)[0] + " ..."
            out.append("- [%s](%s): %s" % (title_of(text), rel.replace(os.sep, "/"), summary))
        out.append("")
    write(os.path.join(ROOT, "llms.txt"), "\n".join(out))


def build_sources():
    """List every external address the handbook cites, grouped by site."""
    by_site = {}
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in (".git", "raw", "__pycache__")]
        for name in files:
            if not name.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(base, name), ROOT).replace(os.sep, "/")
            if rel == "research/sources.md":
                continue
            for url in re.findall(r"\]\((https?://[^)\s]+)\)", read(os.path.join(base, name))):
                site = re.sub(r"^www\.", "", url.split("/")[2].lower())
                by_site.setdefault(site, {}).setdefault(url, set()).add(rel)
    total = sum(len(urls) for urls in by_site.values())
    out = ["# Sources", "",
           "Every external address cited anywhere in the handbook: %d addresses on %d sites, grouped by site, with the" % (total, len(by_site)),
           "pages that cite each. Built by `python tools/build_index.py`. All were read in November 2026.", ""]
    for site in sorted(by_site, key=lambda s: (-len(by_site[s]), s)):
        out += ["## %s (%d)" % (site, len(by_site[site])), ""]
        for url in sorted(by_site[site]):
            pages = sorted(by_site[site][url])
            shown = ", ".join(pages[:4]) + (" and %d more" % (len(pages) - 4) if len(pages) > 4 else "")
            out.append("- <%s> (cited in %s)" % (url, shown))
        out.append("")
    write(os.path.join(ROOT, "research", "sources.md"), "\n".join(out))


if __name__ == "__main__":
    build_genres()
    build_teardowns()
    build_llms()
    build_sources()
