---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.martial-grappling
title: Active martial-arts grappling
language: en
status: draft
doc_type: reference
audiences:
- mod-author
- player
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: Pending review
source_paths:
- data/json/martial_grappling.json
- data/json/martialarts.json
- src/martialarts.h
- src/martialarts.cpp
- src/melee.cpp
- src/monster.cpp
- src/avatar_action.cpp
- tests/martial_grappling_test.cpp
source_symbols:
- use_grapple_technique
- grapple_cooldown_effect
source_queries: []
source_fingerprint: 3fea3da996506b145f5a008d65da1c90ff8dbd01a936b76daf87150bfc734f2a
authority: source-and-tests
verified_commit: 603cd50217c18f1ba9b4fab50d25fb0d46216dd1
verified_at: '2026-11-04'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: aa749873f5ff8e39ca1fec84deb1b60c6dfc454886c12480e9d23eff14fc830f
prerequisites:
- json.overview
depends_on:
- reference.json-object-types
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; gameplay design inspired by CTLG monster dragging.
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: martial-arts
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/1166
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/martial-grappling/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/json/martial-grappling/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/martial-grappling/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/json/martial-grappling/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/603cd50217c18f1ba9b4fab50d25fb0d46216dd1
source_urls:
- path: data/json/martial_grappling.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/603cd50217c18f1ba9b4fab50d25fb0d46216dd1/data/json/martial_grappling.json
- path: data/json/martialarts.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/603cd50217c18f1ba9b4fab50d25fb0d46216dd1/data/json/martialarts.json
- path: src/martialarts.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/603cd50217c18f1ba9b4fab50d25fb0d46216dd1/src/martialarts.h
- path: src/martialarts.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/603cd50217c18f1ba9b4fab50d25fb0d46216dd1/src/martialarts.cpp
- path: src/melee.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/603cd50217c18f1ba9b4fab50d25fb0d46216dd1/src/melee.cpp
- path: src/monster.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/603cd50217c18f1ba9b4fab50d25fb0d46216dd1/src/monster.cpp
- path: src/avatar_action.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/603cd50217c18f1ba9b4fab50d25fb0d46216dd1/src/avatar_action.cpp
- path: tests/martial_grappling_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/603cd50217c18f1ba9b4fab50d25fb0d46216dd1/tests/martial_grappling_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.martial-grappling%29%3A+&body=Document+ID%3A+json.martial-grappling%0ALanguage%3A+en%0AVerified+commit%3A+603cd50217c18f1ba9b4fab50d25fb0d46216dd1%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Active martial-arts grappling

Grappling techniques belong to a martial art's `techniques` list and appear in the active-technique
menu. Inspired by CTLG's G-key monster dragging, they let an unarmed character establish a grip,
drag a controlled monster, and finish with a style-specific throw.

## Technique fields

| Field | Meaning |
| --- | --- |
| `manual_activation` | Set to `true` for player-selected execution. |
| `strictly_unarmed` | Set to `true`; grappling requires two usable, empty arms. |
| `attack_vectors` | Provide an eligible unarmed vector, such as `vector_punch`. |
| `grapple_action` | `hold`, `drag`, or `throw`. |
| `grapple_power` | Positive leverage percentage used in weight capacity and throw damage. |
| `grapple_stamina` | Positive base stamina cost, increased by target weight. |
| `grapple_cooldown` | Positive duration shared by techniques with the same action. |

The character must be upright, awake, and unmounted. Ordinary technique requirements still apply.
The menu displays base stamina, shared cooldown, and remaining recovery time.

## Grip and movement

`hold` applies the source-owned `martial_grapple` effect to one adjacent monster. Establishing a
new hold releases the character's previous target. The hold prevents monster movement while its
source remains adjacent, able to use two empty arms, and has at least 100 stamina.

`drag` moves the character one tile directly backward and pulls the monster into the character's
previous tile. It preserves the hold's remaining duration. `throw` releases the grip, moves the
monster behind the character, and applies bash damage and `downed`. Dragging and throwing require
the acting character's own grip and a clear, supported destination; restraints and vehicle
attachments also affect eligibility.

## Weight, size, and cost

Capacity in kilograms is `(strength * 10 + unarmed_skill * 5) * grapple_power / 100`.
The target must fit that capacity and be at most one size category larger than the character.
With `load = target_weight_kg / capacity_kg`, stamina cost is
`grapple_stamina + floor(grapple_stamina * load)`. Action cost is
`floor(100 + 100 * load + max(0, size_difference) * 25)` moves.

Increasing load shortens control and knockdown duration and reduces throw damage. Size also
reduces control and impact independently of weight. Core hold and drag cooldowns are 3 seconds and
1 second; throw cooldowns range from 4 to 6 seconds. Effect serialization preserves grip ownership
and recovery across saves, and shared action cooldowns continue across martial-art changes.

## Core styles

| Style | Active finish |
| --- | --- |
| Judo | O-goshi Hip Throw: higher leverage. |
| Aikido | Kokyu-nage Projection: low-impact redirection. |
| Pankration | Pankration Body Slam: higher impact and stamina cost. |
| Tai Chi | Push-Hands Unbalancing: controlled, low-impact knockdown. |
| Krav Maga | Controlled Takedown: balanced impact and recovery. |
| Muay Thai | Clinch control through the shared hold and drag techniques. |

Definitions live in `data/json/martial_grappling.json`; style assignments live in
`data/json/martialarts.json`. Run `cata_test "[martial_arts]" --rng-seed 20261104` to cover grappling
and existing martial-arts behavior. The dedicated cases are in `tests/martial_grappling_test.cpp`.
