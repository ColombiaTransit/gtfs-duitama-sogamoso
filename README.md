# GTFS Duitama–Sogamoso (Colombia)

Open-source research and reproducible GTFS preparation for **urban bus services only** in Duitama and Sogamoso, Boyacá.

## Current scope (2026-11-20)

The uploaded Overpass export contains **105 bus route relations**. Based on their literal OSM `network` tags, **82** are in scope:

- **Duitama: 52 route relations** — 49 with `network=Urbano Duitama` plus 3 with `network=Servicio de Transporte Urbano Duitama`. Operators: Tundama 26, Cootraheroes 14, Tures 12.
- **Sogamoso: 30 route relations** — `network=Urbano Sogamoso`. Operators: TransLago 9, TransAvella 8, Cootradelsol 7, Flota Sugamuxi 6.
- **Deferred: 23 relations** — 9 `Interurbano Boyacá`, 1 `Transporte Intermunicipal Boyacá`, and 13 lacking a `network` tag. These are **not** included in urban GTFS generation, even when they traverse one or both cities.

See [`research/scope.md`](research/scope.md) for inclusion/exclusion rules. This scope can be revised only upon explicit new evidence or a deliberate project decision. `route_master` relations are not counted as GTFS routes.

## Research phase: OSM inventory

Run the Overpass query at [`research/overpass/duitama-sogamoso-bus-routes.overpassql`](research/overpass/duitama-sogamoso-bus-routes.overpassql) in [Overpass Turbo](https://overpass-turbo.eu/).

1. Execute the query.
2. Export **raw OSM JSON** (not GeoJSON), retaining relation member order and tags.
3. Save the result locally as `osm/duitama-sogamoso-bus-routes.json` for analysis.
4. Apply the urban scope before generation. Keep regional relations in the research register, not in the published feed.
5. Compare the 52 Duitama OSM relations against the historical GitLab GTFS and inspect Sogamoso route directions/stops.
6. Configure [Trufi GTFS Builder](https://github.com/trufi-association/trufi-gtfs-builder), generate a candidate, then run MobilityData GTFS Validator.

**Data provenance and licensing:** OSM-derived output must retain OpenStreetMap contributors' attribution and comply with ODbL 1.0. OSM tags such as `interval` and `opening_hours` are provisional until verified; route presence is not proof of current operation.
