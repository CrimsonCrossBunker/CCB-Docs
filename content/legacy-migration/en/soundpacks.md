## Soundpack contracts

A soundpack is a directory under `data/sound/` with `soundpack.txt`. `NAME` is the unique ID used by
the option and `VIEW` is its display name. `load_soundset` resolves the current choice, falls back to
`basic` when needed, and loads JSON from the directory through `DynamicDataLoader`. Sound JSON
loaders return early when audio initialization has not succeeded.

### SFX and playlists

A `sound_effect` requires `id` and `files`; `volume` defaults to 100. `variant` may be a string or an
array and defaults to `default`. `season`, `is_indoors`, and `is_night` become part of the lookup key.
Multiple files are random alternatives for the same key, and paths are relative to the soundpack.
Actual fallback is implemented by the `sfx_resources` lookup. Some call sites require an exact
variant, so not every ID is guaranteed to fall back to `default`.

`sound_effect_preload` warms the listed keys without changing playback semantics. A `playlist`
contains a `playlists` array; each entry has an ID, optional shuffle, and `{file, volume}` entries.
A later definition of the same ID replaces its map entry. Current `music` call sites define
activation and priority; the historical four-ID list is not guaranteed to be a complete registry.

### Inventory and validation

There is no permanently complete hand-maintained SFX ID/variant list. Generate an inventory from all
`play_variant_sound`, ambient, vehicle, UI, and music call sites, then compare it with soundpack JSON.
Check missing or undecodable files, empty lists, duplicate keys, exact/default fallback, seasonal,
indoor, and night combinations, preload, shuffle, compounded volume, loops/channels, distance, pan,
pitch, pack switching, and disabled sound. Distribution also requires author, source, and compatible
license records. A test-mode or no-audio-backend load is not proof of real playback.
