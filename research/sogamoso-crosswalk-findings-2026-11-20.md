# Sogamoso: 0541-2024 vs OSM geometric crosswalk — 2026-11-20

**Sources and checks**

1. User-uploaded signed, 28-page scan of **INTRASOG Resolución 0541 (20 March 2024)**; SHA-256 `6d264badb4e90707976a2f1557eab04590189ac65b46c62be709f4898891b532`. Official source URL: https://www.intrasog.gov.co/wp-content/uploads/2024/03/RESOLUCION-0541.pdf .
2. User-uploaded raw Overpass JSON with `timestamp_osm_base=2026-11-20T04:10:53Z`; SHA-256 `a0fefed524b01101238962dbcb89cdb3f3ce0c167666ae77ed869d7f7c3a5784`.
3. Exactly **30 OSM bus route relations** have literal `network=Urbano Sogamoso`, across 4 operators; the PDF officially establishes **20** routes for those operators.
4. Compared **official route names, textual street itineraries, route structure, and published route length** against OSM relation name, OSM member-way street names and calculated sum of way lengths. The primary crosswalk is [`intrasog-0541-osm-crosswalk-2026-11-20.csv`](intrasog-0541-osm-crosswalk-2026-11-20.csv).
5. The OSM length metric is the **sum of geodesic node-to-node distances of the relation's included way members**. It is not a survey, not automatically a single connected shape, and not equivalent to the official distance. Use [`../scripts/osm_route_length_inventory.py`](../scripts/osm_route_length_inventory.py) to recalculate.

## Provisional matching results

| Matching category | 0541 routes |
|---|---:|
| Strong candidate (name + distinctive street path + plausible length) | 6 |
| Partial candidate (some corridor agreement; not yet full itinerary) | 5 |
| Partial conflict (name/corridor, but notable length or itinerary conflict) | 4 |
| Weak candidate (needs targeted manual verification) | 4 |
| **No OSM candidate / scope hold** | **1 (5C)** |
| **Total** | **20** |

The 19 nominated OSM candidates are **not confirmed geometric equivalents**, and strong is not a publication-ready status. They are **19 different OSM relations**. The other **11 of the 30** remain unassigned: [`sogamoso-osm-unassigned-2026-11-20.csv`](sogamoso-osm-unassigned-2026-11-20.csv).

### High-confidence starting points

- **1TL UPTC–Parque Laguito ↔ LAGO-2** (relation `14507684`): official 12.6 km vs OSM 12.3 km; Calle 3 Sur → Carrera 18 → Calle 1 Sur → Carrera 23 → Calle 2E/Carrera 26 and Laguito corridors correspond (PDF p. 7).
- **2TL Universitario–Pinares de San Luis ↔ LAGO-3** (`14534137`): official 13.8 vs OSM 13.02 km; Calle 40/Carrera 10B and Calle 27/Carrera 9A/UPTC alignment (PDF p. 8).
- **2C Magdalena–Liberia ↔ SOL-3** (`15851158`): official 8.89 vs OSM 8.07 km; same named endpoints and central streets. Caution: **legal 2C is not OSM SOL-2** (PDF p. 14).
- Additional strong candidates: **1FS ↔ SUGA-1**, **1C ↔ SOL-1**, **1TA ↔ AVELLA-1**. Their full loop/directions still require checks.

### High-risk discrepancies

- Official **2FS Sugamuxi–Magdalena** is **10.5 km**, OSM **SUGA-2** is **15.0 km** (+42.9%). Do not apply 2FS official times to the old SUGA-2 shape blindly.
- Official **3TA Villa del Sol–Ramada–San José de Bolívar** is **22 km**, OSM **AVELLA-3** is **15.64 km** (-28.9%): likely missing or changed extension.
- Official **4FS Cementerio–Campamento–Pedregal** does **not** correspond merely by number to OSM **SUGA-4** (Libertador Centro–Nogal). OSM **SUGA-5** (Puente Pesca–El Crucero, 18.9 km) is a **weak alternative** due to Puente Pesca corridor/length only; Pedregal and Cemetery legs unconfirmed.
- Official **4C** needs extra Coservicios/Gustavo Jiménez/Ramada verification vs `SOL-6`.
- Official **5C Puente Pesca–Límites Aquitania**, 66.9 km, fixed departures from **two vehicles**, has no credible full 66.9 km urban OSM relation. Although defined as urban in the resolution, the project explicitly defers intercity service; **put on a scope hold, not a deletion**.
- Official route names in 0541 may differ from those in legacy OSM even when some street corridors overlap. Do not assume OSM `ref` is an official numbering scheme.

## OSM member-way topology audit

Across 30 urban Sogamoso relations, inspect the **minimum distance between endpoints** of consecutive OSM way members in their existing order.

- **27/30** have no consecutive-way gap over 100 m in this screening test.
- **LAGO-5** `14534204`: discontinuities **3.973 km** and **6.584 km**, involving way `1172507625` (unnamed), and adjacent ways `1097531032` and `1375912610`. This affects the tentative **4TL** mapping.
- **AVELLA-5** `14534203`: **5.302 km** gap between ways `1532601669` and `87392192`, plus a **104 m** gap earlier. This relation also has an OSM fixme on ambiguous travel direction.
- **AVELLA-6** `15818613`: **3.167 km** gap between ways `1097531032` and `294434072`, plus **1.847 km** between ways `1097531046` and `1411690223`.
- The other 27 have no >100m consecutive gap, but their directions/branch order/stop positions are **not yet verified**. This test does not prove their shapes form correct routes.

**Do not route directly across these gaps** in a candidate GTFS. First distinguish wrong OSM member ordering from missing street segments or incompatible variants, and repair only if the legal itinerary supports the correction.

## Service data and legal status

- Use the specific headways, operating windows and journey times in [`intrasog-0541-2024-routes.csv`](intrasog-0541-2024-routes.csv) **only after mapping** to legal geometry and checking day-type hours.
- For **5C**, the signed PDF pp. 18–19 lists 2 separate vehicle departure sequences. Correct start at Límites Aquitania is **06:30**, not 05:30; the earlier register was corrected on 20 November 2026.
- As article 11 is effective on publication, the actual publication date remains unknown. Later permanent amendments through Nov 2026 are not exhaustively excluded, so label 0541 `legal_base_as_signed`, not `latest_confirmed`.
- Keep the 11 currently unassigned OSM urban relations **as research records** rather than declaring them inactive. Some may be pre-restructuring routes, alternate itineraries or still operational local lines.

## Next actions ordered by value

1. Detailed street-by-street verification of **six strong candidates** (1TL, 2TL, 2C, 1FS, 1C, 1TA); mark matched only after full loop and direction review.
2. Test four major geometry conflicts (2FS, 3FS, 4C, 3TA) against original street lists and update/replace shapes **only when traceable**.
3. Diagnose and possibly repair disconnected OSM member sequences for LAGO-5, AVELLA-5, AVELLA-6.
4. Confirm which remaining 11 urban relations are displaced, modified or still operating; no automatic drop based solely on 0541 code mismatch.
5. Configure Trufi GTFS Builder **only after** verified route geometry/stop plan, and run MobilityData validator on candidate GTFS. Do not add deferred interurban routes.
