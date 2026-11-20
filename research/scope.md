# Urban-only GTFS scope — 2026-11-20

Source snapshot: uploaded Overpass raw OSM JSON, `2026-11-20T04:10:53Z`. 105 `route=bus` relations.

## Inclusion rules

Include a bus route relation only when its `network` tag **exactly matches**:

- `Urbano Duitama`: 49 relations
- `Servicio de Transporte Urbano Duitama`: 3 relations
- `Urbano Sogamoso`: 30 relations

Total included: **82 relations**, comprising **52 Duitama** and **30 Sogamoso**.

For the current dataset this corresponds to Tundama (26), Cootraheroes (14), Tures (12), TransLago (9), TransAvella (8), Cootradelsol (7), Flota Sugamuxi (6).

## Deferred — excluded from current GTFS

- `network=Interurbano Boyacá`: 9 relations
- `network=Transporte Intermunicipal Boyacá`: 1 relation
- Missing `network` tag: 13 relations (including regional, unclear or unclassified services)

Total deferred: **23 relations**. Keep their metadata for future investigation; do not delete or automatically include these in trips/routes/stops/shapes of the current feed.

A spatial bbox is for *discovery*, **not** sufficient to determine feed inclusion. Regional lines passing through a city are excluded. If a future bus route has a new or missing network value, park it for manual review instead of treating it as urban automatically.

## Generator criteria

- Scope filter runs before GTFS conversion, ideally by OSM relation id/network rather than merely by geometry.
- Keep direction variants separate; relation count is not a unique service-line count.
- Do not invent opposite directions, stop roles, official frequencies or operating windows.
- Match historical Duitama GTFS relation ids where possible.
- Retain OSM provenance and ODbL attribution in outputs.
- Run MobilityData GTFS Validator on each publishable candidate.
- Reconsider intercity inclusion only in a separate later project phase.

## Known issues

- 52 Duitama relations map to historical GTFS routes; 30 Sogamoso relations require independent geometry/direction/stop checks.
- Many OSM relations lack explicit stop/platform members; plan stop sourcing separately.
- OSM `interval` and `opening_hours` values are not independently verified.
