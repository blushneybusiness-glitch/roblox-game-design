# The line: holding attention without tricking children

Other pages in this repo explain mechanics that keep players: loss, theft, random rewards, clocks, scarcity. This page says where each one stops being fair. It lists what regulators have punished, what Roblox's own rules require (with dates), what the rules do not cover, and a test for the gaps. Open it before you add anything that involves Robux and chance, Robux and a timer, or Robux and a loss, and before you publish to younger players. Rules change often: Roblox moved one threshold three times between May and November 2026. Check each linked page before you rely on it. Nothing here is legal advice.

## What is known

### Who the players are

| Fact | Value | Source |
|---|---|---|
| Roblox's two child catalogues | Roblox Kids, ages 5 to 8; Roblox Select, ages 9 to 15 | [Kids and Select docs](https://create.roblox.com/docs/production/publishing/kids-and-select) |
| Adults among age-checked daily users, Q3 2026 | 29% worldwide, 37% in the US | [MediaPost summary of Roblox's letter](https://www.mediapost.com/publications/article/419134/), secondary. Roblox calls these estimates. |
| Daily users who had completed an age check | 64% overall, over 80% of 13 to 17 year olds | same |
| Share of daily users aged 13+ | about two-thirds (Q3 2025, so about one-third under 13) | [Investing.com transcript](https://ng.investing.com/news/transcripts/earnings-call-transcript-roblox-q3-2025-shows-strong-growth-but-stock-dips-2174759), secondary, not re-checked for 2026 |
| US 13 to 17 year olds on Roblox daily | about 30%, a CEO estimate | MediaPost summary, secondary |
| Under-13 players in [Grow a Garden](../teardowns/grow-a-garden.md) | about 35% | [Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden) |
| [Brookhaven](../teardowns/brookhaven.md)'s audience | aimed at ages 9 to 12; Common Sense Media rates it 8+ | [RoWatcher](https://rowatcher.com/news/what-is-brookhaven-rp-why-400k-players-choose-roblox-s-biggest-game) |

**Our read:** in a typical hit, about one player in three is under 13, and many more are under 16. Whatever a mechanic does, assume a 10-year-old meets it.

### What regulators did

| Action | Conduct named | Source |
|---|---|---|
| US FTC v. Epic Games (Fortnite), Dec 2022, refunds finalised Mar 2023 | $245M in refunds for dark patterns, plus a separate $275M children's-privacy penalty. Named: a button layout that charged on a single press, including presses made while waking the game from sleep, on loading screens, or on a nearby button meant to preview an item; children able to buy currency without a parent until 2018; accounts locked after chargebacks, with threats of a lifetime ban; over 1 million complaints ignored; cancel and refund options hidden. The order requires affirmative consent before a charge, bans locking accounts over disputes, and requires voice and text chat off by default for children and teens. Civil penalty up to $46,517 per violation. | [FTC press release](https://www.ftc.gov/news-events/news/press-releases/2022/12/fortnite-video-game-maker-epic-games-pay-more-half-billion-dollars-over-ftc-allegations) |
| UK Children's Code, Standard 13 (nudge techniques) | Do not nudge children toward weaker privacy or sharing data. Do not exploit unconscious biases (colours or images tied to good outcomes) or the need for social approval. Named examples: a big "yes" beside a small "no"; one click for low privacy against many clicks for high privacy. Nudges toward breaks, saving and parental help are encouraged. The standard is written about data and privacy, not spending in general. | [ICO](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/age-appropriate-design-a-code-of-practice-for-online-services/13-nudge-techniques/) |

Paid loot boxes by country ([Wikipedia: Loot box](https://en.wikipedia.org/wiki/Loot_box)):

| Country | Rule |
|---|---|
| Belgium | Treated as gambling since Apr 2018; fines up to €800,000 |
| Netherlands | 2018 ruling against transferable items overturned in Mar 2022 |
| United Kingdom | Not gambling unless cashable (2017); the government declined to legislate (Jul 2022) |
| China | Published odds since 2017; since 2019, no sales to under-8s and monthly caps of 200 to 400 RMB for under-18s |
| Japan | "Complete gacha" (pay to finish a random set) banned in 2012 |
| South Korea | Odds disclosure law enforced from Mar 2024 |
| Australia | From Sep 2024, games with paid loot boxes rated M; simulated gambling R18+ |
| Austria | A district court ruled FIFA packs gambling (Mar 2023) |

The same article reports a meta-analysis of 15 studies finding a moderate positive link between loot-box spending and problem-gambling symptoms. A June 2026 report ties Roblox's worldwide odds rule to South Korea's law ([TechTimes](https://www.techtimes.com/articles/319148/20260626/koreas-loot-box-rules-push-roblox-disclose-item-odds-worldwide.htm), secondary).

### Roblox's own rules

**Paid random items** (rules clarified 26 May 2026, [DevForum](https://devforum.roblox.com/t/clarifying-requirements-for-paid-random-items/4654622); detail in the [docs](https://create.roblox.com/docs/production/monetization/paid-random-items)):

- Covered: capsules, enhancements, combinations, and anything that changes odds: luck boosts, pity, enhanced drops, rate-up items. A random item inside a bundle makes the whole bundle a paid random item. Rerolls, keys and spin tickets bought with Robux count as indirect purchases.
- Before purchase, every outcome shows its odds as a number, in percent, and the odds sum to 100%. Odds may be rounded to four or more places past the first non-zero digit, with a disclaimer.
- An item that changes odds states its effect as a number, and the displayed odds update live while it is active.
- A long list may sit behind a clickable pop-up labelled with a word such as "Info" or "Details"; a lone (i) icon is not enough.
- If an outcome can be won only once, the remaining odds update for that player.
- Every outcome gives some benefit. No outcome may lose the payment.
- Call `PolicyService` `ArePaidRandomItemsRestricted` per player and give restricted players a compliant alternative: an earnable unpaid path, a fixed order shown up front, a direct sale priced by expected value, or hide, block or remove. Trading of paid random outcomes must check `IsPaidItemTradingAllowed`.
- Markets named as regulated: Australia, Belgium, the Netherlands, the United Kingdom and Brazil.
- Penalty: games are moderated; the post warns of removal and account suspension.

| Rule | Date | What it says | Source |
|---|---|---|---|
| Reward-driven media feeds | 25 Aug 2026 | A game loses Kids and Select access if it shows a media feed (short video, images, stories) with autoplay, loop or infinite scroll, and rewards or implies a reward for continued watching. Player-started rewarded video ads are exempt. | [DevForum](https://devforum.roblox.com/t/roblox-kids-and-select-new-restrictions-on-reward-driven-media-feeds/4829188) |
| Experience notifications | undated page | Banned: false time pressure, disguised ads, bait-and-switch rewards, tricking users into purchases. A game cannot require notifications to play. Recipients must be 13+; one per user per day. | [Notifications docs](https://create.roblox.com/docs/en-us/production/promotion/experience-notifications) |
| Content maturity labels | undated page | Minimal and Mild: Kids (5 to 8) and Select (9 to 15). Moderate: Select and 16+. Content May Vary: age-checked 16+. Restricted: age-verified 18+. Playable gambling is prohibited; gambling scenery that cannot be played is 13+; free-form drawing others can see is 16+; a social hangout with private spaces is 18+ verified (an Aug 2025 newsroom post said 17+, [Roblox](https://about.roblox.com/newsroom/2025/08/extending-roblox-policy-on-romantic-and-sexual-content)). Paid random items must be disclosed. | [Content ratings docs](https://create.roblox.com/docs/en-us/production/promotion/content-ratings) |
| Under-16 catalogue gate | pilot 19 May 2026, global 16 Jun 2026 | A new game is shown only to age-checked 16+ players until it reaches a benchmark of highly engaged players within 60 days: 500 at launch, 250 from 19 Aug 2026, 100 now. The creator also needs ID verification, 2-step verification, two months of Plus or Premium or a refundable 1,000 R$ fee per game, the maturity questionnaire and an evaluation. | [DevForum](https://devforum.roblox.com/t/roblox-kids-and-select-global-launch-upcoming-updates-to-eligibility-ads-manager-and-expedited-review/4685717), [Kids and Select docs](https://create.roblox.com/docs/en-us/production/publishing/kids-and-select) |
| Paid brand deals | posted 20 Mar 2026, in force 4 May 2026 | Brand integrations must be registered at least 5 business days before going live, with restrictions for under-13s. Creator disclosures must be clear and visible or audible, and come right before a code is offered. | [DevForum](https://devforum.roblox.com/t/new-advertising-policies-standards/4527365), [Roblox Help](https://en.help.roblox.com/hc/articles/360026092011) |
| Chat | 7 Jan 2026 (early Dec 2025 in Australia, New Zealand, the Netherlands) | An age check is needed to chat. Bands: under 9, 9 to 12, 13 to 15, 16 to 17, 18 to 20, 21+. Each band chats with its own and neighbouring bands. Under 9 needs parental consent. Kids chat is off by default; Select chat starts off for unchecked accounts. All player text goes through TextChatService. | [Roblox newsroom](https://about.roblox.com/newsroom/2026/01/roblox-age-checks-required-to-chat), [chat guidelines](https://create.roblox.com/docs/en-us/chat/guidelines) |
| Voice | undated page | Age-verified 13+ only, in places with 100 players or fewer. | [Voice chat docs](https://create.roblox.com/docs/en-us/chat/voice-chat) |
| Rewarded video | undated page | The reward must be a developer product normally sold for Robux, never Robux or a random item, granted at once. Progress may not be gated behind an ad. Under-13s are not eligible, per a DevForum post read only in summary. | [Rewarded video docs](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) |
| Community Standards | undated page | No removing purchased content without notice. Ads are not personalised for under-18s. No Robux or items of value in gambling. | [Community Standards](https://about.roblox.com/community-standards) |
| Subscriptions | undated page | Benefits already paid for may not require extra tasks such as social posts. | [Subscriptions docs](https://create.roblox.com/docs/production/monetization/subscriptions) |
| Discovery | undated page | Titles and thumbnails implying a money reward ("Robux! Play now!") are not prioritised; leading with giveaways reduces exposure. | [Discovery docs](https://create.roblox.com/docs/en-us/production/promotion/discovery) |
| Referrals | undated page | A reward for both inviter and invitee is supported; Roblox suggests one reward per invitee and a cooldown. | [Referral docs](https://create.roblox.com/docs/en-us/production/promotion/referral-system) |

**Rules our research could not find.** No official text on rewards for likes, favourites, follows, group joins or ratings. No official text on countdown timers, fake scarcity or pressure inside a purchase flow; only notifications ban false time pressure, and Roblox's design guidance says to state exactly how much time a season has left ([monetization foundations](https://create.roblox.com/docs/en-us/production/game-design/monetization-foundations)). No country list for voice. No mapping from specific content (violence, fear, crude humour) to each maturity label. Treat these as gaps, not permission. One game with nearly 200M visits was auto-moderated as "Scamming" in Aug 2026; its developer suspects a reward for joining a community server plus free crates, and Roblox did not confirm the cause ([DevForum](https://devforum.roblox.com/t/game-with-nearly-200m-visits-banned-for-scamming/4776239)).

## The test

Where no rule applies, ask: **would a parent watching over the player's shoulder call it a trick?** Watch for three things in that moment: a price the child did not read, a clock or a stock count that is not true, and a Robux button shown while the child is upset. If any is on screen, the design fails, whatever the rules say.

## Mechanism by mechanism

| Mechanism | Fine | Over the line | Sourced example |
|---|---|---|---|
| Odds | Every paid roll and every Robux luck boost shows numeric odds summing to 100%, live under the boost; a free path exists for restricted players. Pity shown as a counter. | Odds hidden, rounded to zero, or different from the server's; a paid roll that can give nothing; paid "collect the set" (banned in Japan). | Blue Lock: Rivals publishes Lucky Spin odds with a 50-spin pity ([wiki](https://blue-lock-rivals.fandom.com/wiki/Spins)). Arsenal disables cases in Belgium, the Netherlands, Australia and for UK under-18s ([wiki](https://robloxarsenal.fandom.com/wiki/Crate)). Flee the Facility removed its crate spin animation on 21 Oct 2023 for compliance; crates now cost 100 to 700 credits by rarity ([wiki](https://flee-the-facility.fandom.com/wiki/Crates)). |
| Timers | A fixed public clock (5, 30, 60 minutes); a paid skip with its price shown and the free tick in view. | A countdown that resets itself; a timer shortened on the screen and not on the server; a notification saying "ends soon" when it does not (banned for notifications). | Grow a Garden restocks every 5 minutes on every server and sells a restock for 79 R$ beside the clock ([wiki](https://growagarden.fandom.com/wiki/Seed_Shop)). |
| Scarcity | Limited items with a stated end date; global stock everyone can see. | "Last chance" for an item that returns next week; a stock count that is invented. **Our read**, since no rule names it. | [Jailbreak](../teardowns/jailbreak.md) has 37 seasonal vehicles listed as unobtainable ([Earnaldo](https://earnaldo.com/blog/jailbreak-free-robux-guide), promotional source). |
| Loss and theft | One unit lost per raid, a visible lock, a way to chase the thief within 5 seconds, nothing taken in the first minutes or while offline. | A Robux prompt that opens because something was just stolen; Robux-bought items that can be stolen; losses that wipe a base. | [Steal a Brainrot](../teardowns/steal-a-brainrot.md)'s lock lasts 60 s plus 10 s per rebirth ([wiki](https://stealabrainrot.fandom.com/wiki/Base)); Polygon still wrote that it grew "by making kids miserable" ([Game Rant](https://gamerant.com/roblox-what-is-steal-a-brainrot-explained-gameplay-player-count-scripts/)). See [slop/02-why-it-holds.md](../slop/02-why-it-holds.md). |
| Purchase prompts | Opened by a press meant to buy; Buy and No the same size; one offer at the moment of need. | A charge from a preview, close or navigation press; a large "yes" beside a small "no"; a prompt during a loading screen. | FTC v. Epic. [Dress to Impress](../teardowns/dress-to-impress.md) changed its theme prop from an automatic purchase to an optional prop on 29 Feb 2024 ([guide](https://rblxguide.com/games/dress-to-impress/updates/themes-guide)). |
| Social pressure | Friend bonuses and referral rewards for both sides; a server banner for a big win. | A reward for joining an outside community server; a paid reward that only unlocks by recruiting friends; shaming non-payers. | Grow a Garden pays +10% per friend in the server up to 40% ([wiki](https://growagarden.fandom.com/wiki/Sheckles)). The "Scamming" case above. |
| Feeds and idle rewards | Offline growth; an AFK room that pays a stated rate; player-started rewarded video. | An autoplaying or scrolling feed that pays for watching (removed from Kids and Select since 25 Aug 2026); an ad that gates progress. | [Steal An Egg](../teardowns/steal-an-egg.md)'s treadmill "Reels" feed was removed and the game was briefly pulled ([Kotaku](https://kotaku.com/roblox-cracks-down-on-doomscrolling-games-like-steal-an-egg-that-forces-players-to-watch-reels-while-running-on-a-treadmill-2000727952)). [Anime Vanguards](../teardowns/anime-vanguards.md) pays 20 gems every 4 minutes in its AFK room ([wiki](https://animevanguards.fandom.com/wiki/Time_Chamber)). |
| Events | Same day and hour each week; everyone who attends leaves with something; the exact end time shown. | An event item that only Robux can get; an event "ending" that is extended. **Our read.** | Royale High retired a fountain where players staked 5 to 200 diamonds to double or quadruple them, which its wiki says resembled gambling with a purchasable currency. It is now a free wish every 2 hours ([wiki](https://royale-high.fandom.com/wiki/Fountain)). |

## The rules

1. **Show odds as numbers before any paid roll, summing to 100%, and update them live under a boost.** Roblox rule since 26 May 2026.
2. **Gate every paid random item with `ArePaidRandomItemsRestricted` and offer a compliant path.** Roblox rule; five markets named.
3. **Charge only on a deliberate buy press.** FTC v. Epic. Keep buy buttons at least 1 button-width away from navigation and close buttons (**Start with**; no source names a distance).
4. **Make Buy and No the same size and colour weight.** ICO Standard 13 names the big-yes, small-no layout.
5. **No Robux prompt within 10 seconds of a theft or PvP loss.** **Our read**, matching [12-monetization.md](12-monetization.md).
6. **No feed that pays for watching** in any game that wants Kids and Select. Roblox rule since 25 Aug 2026.
7. **Every timer and stock count on screen is the server's.** Notifications rule, extended to the game by **our read**.
8. **Never lock an account or delete items over a refund request.** FTC v. Epic. Use the refund webhook to take back only the refunded item ([DevForum](https://devforum.roblox.com/t/new-transaction-refunded-webhook-notifies-when-a-purchase-is-cancelled/4890339)).
9. **No reward for joining an outside server or group.** **Our read** from the moderation case; no official rule found either way.

## How to do it

1. List every place Robux meets chance, a timer, a loss or another player. Use [kit/design-audit.md](../kit/design-audit.md).
2. For each, find its row in the table above and write which column it is in.
3. Play the first 15 minutes on a fresh account while someone who has never played watches. Note every moment they ask "is that real?" or "did it just charge?".
4. Answer the content maturity questionnaire for the most mature content you made, then check the label against your audience target.
5. Run the checks below before every update that touches the shop.

## Checks

- [ ] Every paid roll shows numeric odds per outcome, summing to 100%, before purchase.
- [ ] Displayed odds change within one second when a luck boost starts or ends.
- [ ] A test account flagged as restricted cannot buy or trade a paid random item and sees the alternative.
- [ ] No paid roll has an outcome worth nothing.
- [ ] Every purchase needs a press on a button whose label says buy and shows the price.
- [ ] Buy and No buttons are the same size.
- [ ] No prompt opens within 10 seconds of a theft, death in PvP, or a lost round.
- [ ] Every on-screen timer matches the server clock to within 1 second.
- [ ] No feed with autoplay or scroll pays for watching.
- [ ] No notification says "ends soon" unless it ends within the time stated.
- [ ] Nothing bought with Robux can be stolen or removed by a rebirth.
- [ ] No reward for likes, group joins or outside servers.
- [ ] A parent watching for 15 minutes finds nothing they would call a trick.

## Mistakes

| Symptom | Cause | Fix |
|---|---|---|
| Game removed from Kids and Select | Feed with autoplay plus a reward for watching | Remove the reward or the feed; request re-review |
| Moderated as scamming | Rewards for outside communities, unclear crates | Remove the reward; show contents and odds |
| Players report odds as fake | Displayed odds differ from server odds, or do not update under boosts | Read displayed odds from the same table the server rolls |
| Chargebacks rise | Purchases from accidental presses | Separate buy buttons from navigation; add a confirm step showing the price |
| "Pay to win" and "makes kids miserable" reviews | Protection or recovery sold right after a loss | Free counterplay within 5 seconds; no prompt after loss |
| Paid item breaks in Belgium or the UK | No `ArePaidRandomItemsRestricted` check | Gate per player; offer the earnable or fixed-order path |

## Sources

- Regulators: [FTC press release on Epic](https://www.ftc.gov/news-events/news/press-releases/2022/12/fortnite-video-game-maker-epic-games-pay-more-half-billion-dollars-over-ftc-allegations); [ICO Children's Code, Standard 13](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/age-appropriate-design-a-code-of-practice-for-online-services/13-nudge-techniques/); [Wikipedia: Loot box](https://en.wikipedia.org/wiki/Loot_box); [TechTimes](https://www.techtimes.com/articles/319148/20260626/koreas-loot-box-rules-push-roblox-disclose-item-odds-worldwide.htm).
- Roblox rules: [paid random items post](https://devforum.roblox.com/t/clarifying-requirements-for-paid-random-items/4654622) and [docs](https://create.roblox.com/docs/production/monetization/paid-random-items); [media feeds](https://devforum.roblox.com/t/roblox-kids-and-select-new-restrictions-on-reward-driven-media-feeds/4829188); [notifications](https://create.roblox.com/docs/en-us/production/promotion/experience-notifications); [content ratings](https://create.roblox.com/docs/en-us/production/promotion/content-ratings); [Kids and Select](https://create.roblox.com/docs/en-us/production/publishing/kids-and-select); [advertising policies](https://devforum.roblox.com/t/new-advertising-policies-standards/4527365); [age checks for chat](https://about.roblox.com/newsroom/2026/01/roblox-age-checks-required-to-chat); [chat guidelines](https://create.roblox.com/docs/en-us/chat/guidelines); [voice chat](https://create.roblox.com/docs/en-us/chat/voice-chat); [rewarded video](https://create.roblox.com/docs/production/promotion/rewarded-video-ads); [Community Standards](https://about.roblox.com/community-standards).
- Audience: [MediaPost](https://www.mediapost.com/publications/article/419134/); [Investing.com](https://ng.investing.com/news/transcripts/earnings-call-transcript-roblox-q3-2025-shows-strong-growth-but-stock-dips-2174759); [Wikipedia: Grow a Garden](https://en.wikipedia.org/wiki/Grow_a_Garden); [RoWatcher](https://rowatcher.com/news/what-is-brookhaven-rp-why-400k-players-choose-roblox-s-biggest-game).
- Cases: game wikis and articles linked in the mechanism table.
