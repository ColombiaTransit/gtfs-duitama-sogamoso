# OSM inventory — Duitama and Sogamoso

Source: user-provided raw Overpass JSON `export (6).json`, OSM snapshot `2026-11-20T04:10:53Z`.
Query: [duitama-sogamoso-bus-routes.overpassql](overpass/duitama-sogamoso-bus-routes.overpassql).

## Findings

| Metric | Count |
|---|---:|
| Total elements | 29,067 |
| Nodes | 25,973 |
| Ways | 2,989 |
| Bus route relations | 105 |
| Route master relations | 0 |
| Historical GTFS route IDs present in OSM | 52 / 52 |
| New route relations compared with historical GTFS | 53 |
| Relations tagged with `interval` | 94 |
| Relations tagged with `opening_hours` | 94 |
| Relations with no `name` | 5 |
| Route member entries marked `stop` or `platform` | 5 |

The 53 additional relations consist of 30 `Urbano Sogamoso`, 10 Cootrachica/interurban, and 13 other regional or incompletely tagged relations. **Do not count all 105 as distinct active lines.** Opposite directions are individual OSM relations, and some regional services intersect the bbox.

### Operator breakdown

| Operator tag | OSM relations |
|---|---:|
| Tundama | 26 |
| Cootraheroes | 14 |
| Tures | 12 |
| Cootrachica | 10 |
| TransLago | 9 |
| TransAvella | 8 |
| Cootradelsol | 7 |
| Flota Sugamuxi | 6 |
| Other/missing | 13 |

### Scheduling tags

| Interval | Relations |
|---|---:|
| 15 minutes | 86 |
| 10 minutes (4 plain `10`, 2 `00:10:00`) | 6 |
| 20 minutes | 1 |
| 60 minutes | 1 |
| Missing | 11 |

- 86 route relations share `interval=15` and `opening_hours=Mo-Su 05:00-22:00`. Treat these as provisional OSM assertions, not individually independently verified schedules.
- All 52 historical Duitama GTFS route IDs match OSM relation IDs and now have that same 15-minute / 05:00–22:00 tag set.
- The historical GitLab GTFS instead used 5-minute frequency and 06:00–23:00.
- Four Cootrachica relations have `interval=10`, `opening_hours=Mo-Su 04:30-20:00`; one has `interval=20`, `opening_hours=Mo-Su 05:30-19:30`.
- Two additional routes use `interval=00:10:00` but no `opening_hours`. Some other regional `opening_hours` values are nonstandard/incomplete.
- Only five route-relation member entries carry the `stop` or `platform` role. Most relation-member sequences consist only of ways. **Do not claim a ready-made reliable stop list from these relations**: stops must be sourced, verified or generated using the builder's stop modes.

### Quality flags

- Relations without name/ref/operator: `19727288`, `19727878`, `19727886`, `15851183`, `15879135`.
- Several Cootrachica and Sogamoso relations have `fixme=addtags` or similar.
- OSM relation `14534203` (TransAvella `AVELLA-5`) explicitly warns that the two travel directions are unclear; manual direction/geometry inspection required.
- Because full route members are recursively included, unrelated far-away nodes/ways (including Bogotá) occur in this export. Do not interpret their presence as local stops.
- OSM is not proof of legal validity or current operation. Keep route provenance and verification status.
- Explicitly preserve OSM attribution/ODbL when publishing derived GTFS.

## Next steps

1. Export a route-relation register with OSM ID, operator, ref, name, network, direction, interval, opening_hours, member and stop-role counts.
2. Compare 52 historical routes geometrically and by OSM tags; check directional issues.
3. Review Sogamoso routes and incomplete regional relations separately; do not infer return directions.
4. Use Trufi GTFS Builder with provisional OSM schedule values, then run MobilityData GTFS Validator.
5. Independently verify service windows, headways and stop positions before labeling feed accurate.
