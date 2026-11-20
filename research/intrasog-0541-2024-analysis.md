# INTRASOG Resolución 0541 (20 March 2024) — primary-source findings

**Primary source:** User-provided `RESOLUCION-0541.pdf`, 28 scanned pages, signed 20 March 2024, titled *Por medio de la cual se efectúa la reestructuración de rutas de transporte público colectivo urbano de la ciudad de Sogamoso, se derogan los anteriores actos administrativos y se dictan otras disposiciones*. Full page-level source reviewed visually, without OCR.

**Status:** This resolution is a legal primary source for a **20-route urban restructuring**. It is **not yet proven** to be the latest unmodified operative instrument in November 2026. Distinguish date signed from date published; article 11 makes publication the effective date.

## Operative articles (pages 2 and 26–28)

- **Art. 1** (p. 2): establishes 20 urban routes and their frequencies/vehicle capacity for four authorized operators; detailed route sheets on pp. 2–26.
- **Art. 2** (p. 26): grants **30 calendar days** counted from communication/publication of this resolution to implement the route restructuring, including route markings, operational information and assigned vehicles. It does not prove actual deployment occurred.
- **Art. 2, para. 1** (p. 26): INTRASOG may change routes for warranted service needs, after consideration of legal constraints.
- **Art. 2, para. 2** (p. 26): these regulations constitute the operational regime and are subject to disciplinary procedures if not complied with.
- **Art. 3** (p. 26): passenger carrying capacity allocation is set under prior capacity resolutions (015-1999 and 2374-2020).
- **Art. 4** (p. 26): operators must submit route operating plans and monthly operating reports for verification.
- **Art. 6** (p. 27): shared route-origin locations must have agreed dispatch arrangements among companies sharing such a location.
- **Art. 10 para. 1** (p. 28): derogates prior administrative decisions relating to urban collective route restructuring, **expressly Resolución 10792 of 18 December 2023**.
- **Art. 11** (p. 28): resolution applies **from date of publication**, derogating contrary provisions. Signature: **20 March 2024**; publication date not independently verified.

### Authorized routes and source-by-source specifics

See [`intrasog-0541-2024-routes.csv`](intrasog-0541-2024-routes.csv) for **all 20** route codes, names, type, windows, peak/off-peak durations, headways, length and exact page spans.

| Operator | Routes | PDF pages (1-based) |
|---|---|---|
| Flota Sugamuxi | 1FS Sugamuxi–Gustavo Jiménez–Retorno Argos; 2FS Sugamuxi–Magdalena; 3FS Toscana–Argos; 4FS Cementerio–Campamento–Pedregal | 2–7 |
| TransLago | 1TL UPTC–Parque Laguito; 2TL Universitario–Pinares de San Luis; 3TL Coservicios–Playita; 4TL Caleras–Reforma; 5TL Barrio Oriente–Pinares de San Luis | 7–13 |
| Cootradelsol | 1C Reforma–Pradera–Asodea; 2C Magdalena–Liberia; 3C Callejuelas–Laguito; 4C Coservicios–Gustavo Jiménez–Ramada; 5C Puente Pesca–Límites Aquitania | 13–19 |
| TransAvella | 1TA Villa del Sol–La Tolva; 2TA Prado Norte–Vallado–Aposentos; 3TA Villa del Sol–Ramada–San José de Bolívar; 4TA Prado Norte–Siatame; 5TA Plaza de Mercado–Morca; 6TA Coservicios–La Tolva–Sub Estación San Antonio | 19–26 |

### Timing caveats essential for GTFS

- The tables generally specify **peak and off-peak headways for discrete one-hour blocks**, as well as one weekend block. Treat **only the listed hours** as independently specified. The printed service window often extends later; do not extrapolate the last shown headway into the gap.
- Peak blocks typically cover 06:00–08:59, 12:00–14:59 and 17:00–18:59. Each route's actual table must be used instead of extrapolating this as a universal rule.
- `Tiempo de recorrido: Hora pico / Hora valle` represents scheduled route duration categories; confirm whether full circular route or one-way direction as appropriate.
- **4FS** (pp. 6–7) is exceptional: 20-minute `Cementerio–Campamento` service 06:00–19:00 plus specific `Pedregal` departures/vehicles (including Tuesday specials). Do not model the full named route as one uniform 20-minute frequency.
- **5C** (pp. 18–19) is a fixed-departure service, not a regular headway. Two vehicle departure lists (PDF pp. 18–19): vehicle starting at **Límites Aquitania**: Límites Aquitania 06:30, Puente Pesca 11:30, Límites Aquitania 14:00, Puente Pesca 16:30; vehicle starting at **Puente Pesca**: Puente Pesca 06:30, Límites Aquitania 08:30, Puente Pesca 13:30, Límites Aquitania 16:30. These are stop-based entries for two different vehicles; do not merge into a single hourly frequency. Its stated 66.9 km corridor is presented by the legal text as `urbano`, but the destination `Límites Aquitania` may conflict with our **urban-only, no intercity** project scope. **Hold separately pending geographic/operational classification**; neither silently include nor discard.
- Inaccurate simplification to one departure interval `interval=15` for all Sogamoso OSM relations would discard key official published data.
- Several OSM relation labels differ from route names/codes in 0541. Do **not** match solely by numeric prefix; compare street itineraries, geometries, endpoints and direction.

## Revision of earlier assumption

Earlier research identified the 2023 *Estudio de Reestructuración*, a **proposal**, and partial suspension of 10792. This uploaded original 0541 resolution establishes a **new, express 20-route arrangement** and **expressly repeals 10792**. The 2023 proposal is only supporting design history, while the detailed route sheets of 0541 are primary regulatory source for the specified frequencies. Later modifications and actual implementation remain to be verified.

## Immediate next actions

1. Compare each of 20 legal itineraries (text on pp. 2–26) against the 30 Sogamoso OSM relations. Record match method, certainty and differences; keep OSM relation ids stable in research.
2. Check for 0541 modifications or replacements dated after 20 March 2024 in INTRASOG resolution archives, distinguishing temporary detours from permanent changes.
3. Investigate published/implemented service, art. 4 monthly operational reports if obtainable.
4. Do not update the GTFS generator until the OSM crosswalk and the urban-only exception for 5C are resolved.
5. Preserve original scanned PDF in source archive or record an immutable checksum if publishing it is legally appropriate; cite page numbers for each data field.
