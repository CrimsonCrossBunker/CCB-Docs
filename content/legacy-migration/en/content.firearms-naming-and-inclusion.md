## Why distinct firearm entries are limited

Real firearms have many models, but several may create almost identical player decisions at the
game's modeling resolution. Making every model a separate item adds balance, spawn, ammunition,
magazine, localization, and maintenance cost while hiding weapon role and compatible equipment from
players who do not know model names. Prefer a base gun for a meaningful mechanical distinction and
use a variant when only brand, appearance, or a small dimensional difference remains.

The market-count threshold, caliber totals, and similarity numbers in the legacy page were policy
snapshots. Current executable rules live in `tools/json_tools/gun_variant_validator.py` and
`generic_guns_validator.py`. The former resolves inherited gun and magazine data and checks merge
candidates, names, and common identifiers. Its fields, tolerances, blacklists, and descriptors can
change; do not copy them into a second rule set here.

## Naming and compatibility

- A default display name should tell a general player the weapon role, such as pistol, rifle,
  shotgun, or launcher, instead of exposing only an unexplained alphanumeric model.
- A gun and each non-generic magazine or speedloader should share a useful identifier. A caliber or
  generic word such as “magazine” does not establish the relationship by itself.
- Brand variants may preserve real-world distinctions but must not silently change mechanical
  fields on the base item.
- A new entry needs evidence for its real source, regional and period availability, production and
  circulation, and a license-safe description. Do not copy manufacturer prose or imagery.

## Submission flow

Begin with current guns sharing the ammo, magazine, and role, then compare resolved modes, pockets,
dimensions, mass, barrel, dispersion, reload, damage, and other validator fields. Default to a
variant when the validator finds similarity. A separate item needs a documented player-visible
difference and reviewable evidence. Run JSON formatting and loading, the gun-variant and Generic
Guns validators, and relevant item or ammo tests; also inspect spawn groups, migration IDs, name
localization, and mod compatibility.
