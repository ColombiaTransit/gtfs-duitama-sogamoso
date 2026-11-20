# Duitama — historical GTFS vs current OSM audit (2026-11-20)

## Sources and methodology

- User-uploaded historical GitLab `gtfs (1).zip` containing 52 routes, 52 trips, 52 shapes, 1,227 stops and 3,255 stop_times.
- User-uploaded raw Overpass `export (6).json` with `timestamp_osm_base=2026-11-20T04:10:53Z`.
- Match **historical `routes.route_id` exactly to OSM relation numeric ID**, not the short-name or OSM `ref`. Compare graph of relation member ways, node distances and historical stops, and calculate total polyline lengths and topology-gaps.
- The calculated stop-to-route distances and sampled geometry distances use **nearest OSM nodes**, not true perpendicular distance to a road segment; treat ~100m warnings as candidates for examination, not proof of route detour.

## Inventory comparison

| Finding | Count/Value |
|---|---:|
| Historical route IDs present in OSM | **52 / 52** |
| Operators | Tundama 26 relations, Cootraheroes 14, Tures 12 |
| Historical route long names identical to current OSM names | 40 / 52 |
| OSM route relations with missing referenced ways/nodes | **0** |
| Largest relative difference of old shape length vs sum of member-way lengths | **4.7%** |
| Median old→current and current→old sampled closest-vertex distance | **0.1 m / 0.7 m**, respectively, across relations |
| Historic stop-to-current OSM nearest-vertex median for each route | 0–1.5 m |
| Historical stops > 100m from any current OSM route **node** | 8 route-stop occurrences across 5 relations |
| OSM relations with a gap >100m between consecutive member way endpoints | **4** |
| OSM interval tags | all 52 = `15` |
| OSM opening_hours tags | all 52 = `Mo-Su 05:00-22:00` |

Both old and current geometry are very similar. This can indicate the export is derived from the same OSM geometry and is **not an independent validation of legal itinerary or current operation**.

### Four disconnected ordered-way route variants

| Old line | OSM relation | Largest gap between successive way endpoints |
|---|---:|---:|
| B7 | 6594055 | **4,485 m** |
| A12 | 6585999 | **567 m** |
| C3 | 6594071 | **3,850 m** |
| C3 | 6594078 | **1,533 m** |

The gap calculation minimizes endpoint distance for each consecutive pair, ignoring way direction; these remain real ordering/connection flags. Need inspect whether OSM member ordering is wrong, a piece is missing, or a branch is intentionally discontiguous. **Do not bridge as straight line** in GTFS.

### Eight stop-distance outlier occurrences

Nearest OSM node >100m:

- B1 relation `6577983`: **2** stops, max 143 m
- B7 relation `6594055`: **1** stop, max 124 m
- A12 relation `6585999`: **1** stop, max 124 m
- C3 relation `6594071`: **1** stop, max 124 m
- C5 relation `6578133`: **3** stops, max 143 m

This is a nearest-vertex test, **not** a proper point-to-line distance; recheck against segment geometry before flagging any of these as invalid stops. Overlap with shape-gap flags does not prove causation.

### Timetable problem

The historical feed uses one placeholder weekday/weekend pattern for all services: every direction has headway **300 seconds** (5 min), `exact_times=1`, between **06:00 and 23:00** every day. A single calendar spans **2000–2100**; `agency_name=default` with example.com URL. The 2026 OSM tags instead put **15 minutes** and **05:00–22:00** on **every** direction.

**Neither uniform set should be called legally/operationally verified**. Static GTFS trips contain unrealistic short per-stop travel increments. Preserve original stop ordering and coordinates while looking for primary schedule documents. The current old feed should not be republished unchanged as authoritative.

## NEW official legal trail

A 2024 court ruling publicly reproduces a response from Duitama's **Secretaría de Tránsito y Transporte**, dated 22 May 2024 (oficio `STT-1060 0193-2024`). The municipality identifies **Resolución 3641, 10 November 2003** as the act defining the city-level three operators' authorized itineraries, frequency, service windows and vehicle classes. The response includes route-level detail for **A7, A12, C5, C8** near San Antonio Norte / El Cogollo / Santa Lucía, with interval figures including 9, 10 and 6 minutes and **05:30–20:00** windows. The OCR/web extraction's layout of tables/headings may make specific route-to-frequency association ambiguous; **verify from the original visual PDF or the municipal response before assignment to each route**. The municipality notes these authorized frequencies are from 2003 and travel times have since increased.

- Court PDF: https://publicacionesprocesales.ramajudicial.gov.co/documents/6098902/7631478/Sentencia%2BTutela%2B15238-40-88-004-2024-00037-00%2B%281%29.pdf/8659b89a-6577-df5a-b32c-839303be0ecd?t=1717019090173
- Court PDF web text was accessible, but screenshot request returned **403**, hence route-specific table alignment remains unconfirmed.
- Municipality development plan 2020–23: 26 routes total, Tundama 13, Cootraheroes 7, Tures 6; approximate **7-min average** frequency, not route-specific: https://ccduitama.org.co/wp-content/uploads/2025/12/46588_plan-de-desarrollo-sembrando-civismo-duitama-florece-20202023-vfinal.pdf
- 2025 collective service tariff decree **809 of 31 December 2024** reported by local press, with special **veredal** service windows **05:00–21:00** and route examples B7, A1/A6/A9/A10/A12 and C1/C2/C3/C5/C7/C8. These pertain to rural/municipal routes, not necessarily all buses: https://boyaca7dias.com.co/2025/01/13/en-duitama-ya-comenzaron-a-cobrar-las-nuevas-tarifas-del-transporte-colectivo-urbano-y-de-taxi/
- Sept 2025 municipality began **new optimization/restructuring study**; this is not proof it changed a legally effective network: https://boyaca7dias.com.co/2025/09/28/duitama-inicio-estudio-para-optimizar-rutas-del-transporte-publico-colectivo/
- June 2025 town council minutes discuss route A5 and service interruptions around pandemic; needs direct inspection to establish its current status: https://www.concejomunicipaldeduitama.gov.co/wp-content/uploads/2025/06/Acta-N%C2%B0-036-2025.pdf

## Publication decisions

1. **Keep all 52 Duitama OSM route variants in scope for now**, preserving historical GTFS identifiers and stop sequences, subject to individual status checks. Do not invent route omissions from silence.
2. **Do not automatically replace historical five-minute schedules with generic OSM fifteen-minute schedules**, especially for veredal services.
3. Get and analyse original **Resolución 3641-2003** and any amended acts; inspect court PDF A7/A12/C5/C8 with visual page extraction or direct source.
4. Diagnose four way-member topology breaks, and check five stop-distance cases with point-to-line distance.
5. Check whether A5, B7 and veredal route operations were modified by 2025–2026 acts.
6. Compare routing and timing independently before turning on GTFS Builder. Preserve OpenStreetMap ODbL attribution.

This audit **does not claim** 52 routes are all active; it verifies all 52 are still mapped and have close geometric correspondence.
