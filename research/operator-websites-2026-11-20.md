# Operator website research — 2026-11-20

Scope: **urban Duitama and urban Sogamoso only**. Do not ingest intercity/regional services. Website details below are claims of the respective operators, not a verified current timetable unless explicitly stated. OSM snapshot had 52 Duitama and 30 Sogamoso route relations.

## Sogamoso

### Flota Sugamuxi — official published urban timetable

Source: https://flotasugamuxisa.com.co/urbano

| Route | Label | Operation type | Service window | Peak headway (minutes) | Off-peak headway (minutes) | Route length (km) | Journey duration (min) |
|---|---|---|---|---:|---:|---:|---:|
| 1FS | Sugamuxi | Circular | 05:00–22:00 | 3 | 5 | 22.4 | 80 |
| 2FS | Magdalena | Circular | 05:00–20:00 | 5 | 7 | 10.5 | 45 |
| 3FS | Toscana | Circular | 05:00–22:00 | 4 | 6 | 23.0 | 93 |
| 4FS | Cementerio | Bidirectional | 05:00–20:00 | 20 | 20 | 18.8 | 80 |

The site uses labels **P.** and **V.**, but does not define actual peak/off-peak clock bands. Do **not** invent changeover times or assume whether bands vary on Saturday/Sunday. The operator presents **4 named urban routes** whereas the OSM inventory has **6 route relations**; matching is pending. Do not assume each relation is an additional line.

### TransAvella — route-specific first departures

Source: https://transavella.co/servicios/ (search-engine indexed content; direct fetch returned 401)

| Route | Name | Mon–Fri with students | Mon–Fri without students | Saturday/Sunday/holidays | Other |
|---|---|---|---|---|---|
| 1 | Villa del Sol / Cementos | 05:00 | 05:20 | 06:00 | |
| 2 | Batallón | 05:30 | 05:30 | 06:00 | |
| 3 | Ramada | 05:30 | 05:30 | 06:00 | |
| 4 | U.P.T.C. | 05:15 | 05:30 | 06:00 | every 20 min |
| 8 | Morca | 06:30 | 06:30 | 06:30? | Pilita 06:30 and 18:30; textual context ambiguous |

Do not assign missing last departures or headways; route 8 needs review because the page lists 'Lunes a domingo / Pilita / 6:30 a.m. / 6:30 p.m.' with unclear service interpretation. Operator homepage https://transavella.co/ says 8 authorized routes. OSM inventory has 8 relations, but equality of counts does not imply one-to-one mapping.

### Cootradelsol — five named urban corridors

Source: https://www.cootradelsol.com/rutas/

1. Reforma – Pradera – Asodea
2. Magdalena – Liberia
3. Laguito – Callejuelas
4. Coservicios – Gustavo Jiménez
5. Sogamoso – LMT

No first/last departures or frequencies on the cited page. The operator page separately lists intermunicipal Sogamoso–Aquitania, Tunja and Duitama; all excluded from this project's active GTFS scope. OSM has 7 urban relations; match 5 named corridors to relations before considering any addition/removal.

### TransLago

No official route-and-schedule website found. Use OSM as provisional and INTRASOG as primary authority for legally active routes. Source: https://www.intrasog.gov.co/resoluciones-planeacion/ and https://www.intrasog.gov.co/resoluciones-direccion/.

## Duitama

- **Tundama**: No verified current operator route/schedule website found. Primary references remain OSM/BusBoy and municipal sources.
- **Cootrahéroes**: Historical Wix site referred to in third-party company listing but specific official timetable was not retrieved.
- **TURES**: No verified current operator site with route-level schedules found. A 2022 engineering research report may contain trip times/frequencies: https://noesis.uis.edu.co/items/cfa85d01-c044-47d1-9fcb-d3e73a9e3ba2

## Supplementary and legal observations

- INTRASOG publishes resolutions: https://www.intrasog.gov.co/resoluciones-planeacion/ , https://www.intrasog.gov.co/resoluciones-direccion/
- In January 2024 a news report states a partial suspension of Resolution 10792 of 18 December 2023, which restructured Sogamoso collective bus routes: https://boyaca7dias.com.co/2024/01/09/frenan-resolucion-que-reestructuro-rutas-del-servicio-publico-colectivo-de-sogamoso/ . **Investigate current legal effect before declaring route changes active; this news is historical, not a current ruling.**
- Official operator website timetable values have higher provisional weight than generic OSM `interval=15`, but never invent unknown periods, day-types, or service end-times.
- Solibus (https://solibus.site/) is an additional non-operator urban transport app displaying route/stop UI and a claimed 05:00–21:00 window, not authoritative for every operator. Investigate only if it adds missing route details.
- In 2023 BusBoy Sogamoso development reportedly involved the four urban operators and INTRASOG, providing useful provenance: https://boyacavisible.com/sogamoso-presenta-la-aplicacion-de-transporte-publico-busboy/.

## Priorities

1. Match Flota Sugamuxi 1FS–4FS and TransAvella 1/2/3/4/8 to existing OSM relation IDs, preserving direction.
2. Inspect map/UI route data for Flota Sugamuxi; identify whether the fourth route is represented by two direction relations.
3. Record operator schedules in a structured CSV with source URLs and `verification_status=operator_published`; mark unknown peak-band limits unresolved.
4. Review INTRASOG route restructuring and tariff acts separately; do not substitute a 2023 proposal for operative 2026 rules.
5. For Duitama, investigate municipal decisions and TURES research instead of guessing unavailable timetables.
