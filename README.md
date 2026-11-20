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


## Sogamoso INTRASOG crosswalk (20 November 2026)

The signed [INTRASOG Resolución 0541-2024](https://www.intrasog.gov.co/wp-content/uploads/2024/03/RESOLUCION-0541.pdf) regulates **20** routes (four operators); the OSM snapshot contains **30** urban route relations.

- [Legal route details, service windows and headways](research/intrasog-0541-2024-routes.csv)
- [Legal-to-OSM candidate crosswalk](research/intrasog-0541-osm-crosswalk-2026-11-20.csv) — 6 strong, 5 partial, 4 partial-conflict, 4 weak, 1 missing/held
- [Eleven OSM relations not assigned to a legal route](research/sogamoso-osm-unassigned-2026-11-20.csv)
- [Geometry and discontinuity analysis](research/sogamoso-crosswalk-findings-2026-11-20.md)
- [Reproducible OSM geometry inventory script](scripts/osm_route_length_inventory.py)

**Do not automatically publish the 20 legal schedules against unverified legacy OSM shapes.** Three existing urban relations have large ordered member-way gaps: LAGO-5, AVELLA-5 and AVELLA-6. Legal route 5C to Límites Aquitania is on an explicit scope hold because the current project excludes intercity services.

To reproduce the way lengths and topological screening from a fresh raw Overpass export:

```bash
python scripts/osm_route_length_inventory.py path/to/export.json > urban-route-metrics.csv
```

## Duitama historic-feed audit (20 November 2026)

- [Historical GTFS vs OSM geometry, stops and legal sources](research/duitama-gtfs-osm-audit-2026-11-20.md)
- All 52 historic GTFS route IDs were found unchanged in the current OSM export; do **not** infer operation/validity solely from this match.
- Four route variants (B7 `6594055`, A12 `6585999`, C3 `6594071` and `6594078`) have gaps in ordered OSM way members requiring targeted review.
- Municipality's **Resolución 3641-2003**, cited in a 2024 court case, is now a priority legal schedule source; keep published individual route windows separate from the historical feed's placeholder five-minute frequencies and OSM's uniform fifteen-minute tags.
