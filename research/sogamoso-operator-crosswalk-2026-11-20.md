# Urban Sogamoso: operator-to-OSM matching (2026-11-20)

Scope: 30 OSM `route=bus` relations whose `network` is exactly `Urbano Sogamoso`. Raw OSM snapshot: `2026-11-20T04:10:53Z`. Full row-by-row register: [`sogamoso-urban-operator-matching.csv`](sogamoso-urban-operator-matching.csv).

## Counts

- TransLago: 9 OSM relations, no verified operator timetable/route site
- TransAvella: 8 relations; operator advertises eight authorized urban routes, five route descriptions and selected first departures
- Cootradelsol: 7 relations; operator lists five urban named routes, names/numbers **do not align** 1:1 with OSM
- Flota Sugamuxi: 6 relations; operator lists four urban named routes, some **do not align** with OSM

All 30 relations have `interval=15` and `opening_hours=Mo-Su 05:00-22:00` in this OSM snapshot. **Do not overwrite operator-published schedule data with these generic OSM values.**

## Flota Sugamuxi

Official page: https://flotasugamuxisa.com.co/urbano

| Operator line | Operator name | OSM relation | OSM name | Relation-to-operator mapping |
|---|---|---|---|---|
| 1FS | Sugamuxi | 14508007 / SUGA-1 | Sugamuxi - Gustavo Jimenez | Candidate: number + name |
| 2FS | Magdalena | 14668950 / SUGA-2 | Sugamuxi - Barrio Magdalena | Candidate: number + name |
| 3FS | Toscana | 15851148 / SUGA-3 | Barrio Libertador - Argos | **Unverified name conflict** |
| 4FS | Cementerio | 15851206 / SUGA-4 | Libertador Centro - Nogal | **Unverified name conflict** |
| — | — | 14718744 / SUGA-5 | Puente Pesca - El Crucero | Not shown on website |
| — | — | 14618145 / SUGA-6 | Sugamuxi - Prado Norte | Not shown on website |

Operator schedule (not yet assigned automatically in generator):

- 1FS Sugamuxi: 05:00–22:00, P=3 min / V=5 min, 22.4 km, 80 min, circular.
- 2FS Magdalena: 05:00–20:00, P=5 min / V=7 min, 10.5 km, 45 min, circular.
- 3FS Toscana: 05:00–22:00, P=4 min / V=6 min, 23 km, 93 min, circular.
- 4FS Cementerio: 05:00–20:00, interval 20 min, 18.8 km, 80 min, bidirectional.

**P/V clock boundaries are unspecified.** It is unsafe to generate a real peak timetable by arbitrarily guessing them. Also verify whether 'Tiempo' is full loop, one-way or round-trip before treating as GTFS trip duration.

## TransAvella

Official website: https://transavella.co/servicios/ (direct page fetch returned HTTP 401, but indexed page showed schedule).

- AVELLA-1 `15818789` shares Villa del Sol with operator route 1 (05:00/05:20 weekday depending on students, 06:00 weekends); not verified geometry.
- AVELLA-2 `14534132` number matches route 2 Batallón (05:30 weekday; 06:00 weekends), name does not.
- AVELLA-3 `14496452` shares Ramada with route 3 (05:30 weekday, 06:00 weekends).
- AVELLA-4 `15818632` shares UPTC with route 4 (20-minute interval; weekdays 05:15 students/05:30 non-students; weekends 06:00).
- AVELLA-8 `15818794` shares Morcá with route 8, but 'Pilita 06:30 / 18:30' meaning uncertain.
- AVELLA-5, -6, -7 lack specific operator website details. AVELLA-5 (`14534203`) contains OSM `fixme` on ambiguous directions; prioritize visual inspection.

**The operator's eight-authorized-routes claim is not proof that the eight numbered OSM relations are the same routes.** School-day separation must not be extrapolated to generic Colombian holidays without school calendar data.

## Cootradelsol

Official website: https://www.cootradelsol.com/rutas/

Website lists five routes (1 Reforma–Pradera–Asodea, 2 Magdalena–Liberia, 3 Laguito–Callejuelas, 4 Coservicios–Gustavo Jimenez, 5 Sogamoso–LMT), compared with seven OSM `SOL-1..SOL-7` relations. Examples:
- OSM SOL-3 (La Liberia–Magdalena) seems to correspond to website route **2**, not 3.
- OSM SOL-5 (Callejuelas Oasis–Coliseo) shares a place with website route **3**, not 5.
- OSM SOL-1 includes Asodea and may overlap website route 1, but endpoints differ.
- OSM SOL-2/4 have number/name conflict with the website.

No official departure windows, headways or running times found on the listed page. **Do not renumber OSM routes to website numbering until geometry/stop evidence is checked.**

## INTRASOG legal and documentary leads

- Official urban network reorganization study (2023, **206 pages, scanned**): https://www.intrasog.gov.co/wp-content/uploads/2023/11/ESTUDIO-REESTRUCTURACION-DE-RUTAS.pdf . It needs targeted page/image analysis; not yet interpreted for legally operative routing.
- Official resolution archive: https://www.intrasog.gov.co/resoluciones-planeacion/ ; administrative resolutions: https://www.intrasog.gov.co/resoluciones-direccion/.
- Historical partial suspension of Resolution 10792 (18 December 2023) reported 9 January 2024: https://boyaca7dias.com.co/2024/01/09/frenan-resolucion-que-reestructuro-rutas-del-servicio-publico-colectivo-de-sogamoso/ . Its **current operative status has not been independently established**.
- 2024 legal annual report refers to restructuring **33 existing urban routes** for the four companies (historical description; does not establish 33 present-day routes): https://www.intrasog.gov.co/wp-content/uploads/2025/08/INFORME-DE-GESTION-JURIDICA-VIGENCIA-2024.pdf .
- Resolution 2101-2025 in the INTRASOG archive concerns **intermunicipal access to the terminal**; exclude it from this urban-only investigation unless a later effect on urban service is shown.

## Generator implications

1. Retain the **82 explicit urban OSM relations** in the research scope, with 30 in Sogamoso. Do not equate number of relations to number of independent routes.
2. Store operator facts with sources, but only automatically apply route-specific numbers after reliable mapping and peak clock blocks.
3. For Sogamoso investigate website map geometries, route direction, missing stop members. No full OSM stop sequences are present in the 30 relations: all route member roles are empty.
4. Independently verify current legal service state, including the post-2023 suspension outcome. Do not automatically use a planned restructured network.
5. Preserve regional and intercity exclusions.
