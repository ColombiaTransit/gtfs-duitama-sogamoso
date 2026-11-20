# INTRASOG route restructuring and legal status — investigation, 2026-11-20

Scope: **urban Sogamoso only**. The 2023 research is an analytical/proposed network, **not itself a valid permission to replace the existing OSM network**.

## Primary study and verified structure

- INTRASOG, *Estudios de Transporte para la Reestructuración de las Rutas de Transporte Público Colectivo de Sogamoso*, Ing. Esp. Karen Camargo, 2023, **206 scanned PDF pages**:
  https://www.intrasog.gov.co/wp-content/uploads/2023/11/ESTUDIO-REESTRUCTURACION-DE-RUTAS.pdf
- Inspection: PDF page indices 1–4 (printed contents), 171–172 (summary/proposal), 183 and 199 (frequencies and route characteristics). Pdf page index is zero-based; **printed page numbers differ**.
- The initial diagnostics chapter inventories TransAvella 8 routes, TransLago 9, Flota Sugamuxi 6, Cootradelsol 5 routes subjected to detailed surveys. Other routes appear in summary tables; do not treat the 28 as a definitive legal inventory.
- Proposal chapter 6 lists **20 proposed route codes**, not the same as the 30 urban OSM relations in 2026.

| Operator | Proposed route labels and names in contents | Count |
|---|---|---:|
| TransLago | 1T UPTC–Laguito; 2T Universitario–Pinares; 3T UPTC–Playita; 4T Reforma–Caleras; 5T Barrio Oriente–Gustavo Jimenez | 5 |
| Cootradelsol | 1C Reforma–Gustavo Jimenez; 2C Abuelo Prospero–Laguito; 3C Callejuelas–Laguito; 4C Abuelo Prospero–Ramada–Gustavo Jimenez; 5C Puente Pesca–Limites Aquitania | 5 |
| Flota Sugamuxi | 1F Sugamuxi–La Tolva; 2F Sugamuxi–Barrio Magdalena; 3F Toscana–Argos; 4F Cementerio–Campamento–Pedregal | 4 |
| TransAvella | 1TA Villa del Sol–La Tolva; 2TA Prado Norte–Vallado; 3TA Villa del Sol–Ramada–San Jose de Bolivar; 4TA Prado Norte–Siatame; 5TA Plaza de Mercado–Morca; 6TA Abuelo Prospero–Nazareth | 6 |
| **Total** | | **20** |

### Example route scheduling from the *proposed* network (not yet legally verified)

Proposed TransLago **1T UPTC–Laguito**, study PDF page 172 (0-based; printed page 156):
- Circular, 15.8 km, basic service, microbus; 17 vehicles proposed.
- Operating service window 05:00–23:00.
- Trip duration: 55 min peak, 50 min offpeak.
- Headways: weekday peak 06:00–08:59, 12:00–14:59, 17:00–18:59 at **3 minutes**; weekday offpeak *hours explicitly listed* 05:00–05:59, 09:00–11:59, 15:00–16:59 and 19:00–19:59 at **6 minutes**.
- Weekend: 06:00–19:00 at **10 minutes**.
- IMPORTANT: the weekday headway table does **not** explicitly cover 20:00–23:00 although the stated overall window ends at 23:00. Do not infer missing headways.

Other candidate route time tables and street-by-street itineraries are present in chapter 6 (printed pages 156–185). Targeted page extraction is better than whole-document OCR.

## Legal chain / evidence status

| Date | Act | Evidence and status |
|---|---|---|
| 2023-12-18 | Resolución 10792 | Urban restructuring; some provisions were suspended by 0015. Original operative PDF not yet read. |
| 2024-01-05 | Resolución 0015 | Official file URL https://www.intrasog.gov.co/wp-content/uploads/2024/01/RESOLUCION-015-DE-ENERO-5-DE-2024.pdf (14 MB; web extraction blocked); secondary account https://boyaca7dias.com.co/2024/01/09/frenan-resolucion-que-reestructuro-rutas-del-servicio-publico-colectivo-de-sogamoso/ reports partial suspension of 10792 art. 1, 5 and 9, and partial modification of 2851-2014 art. 1. Exact operative text pending. |
| 2024-03-20 | Resolución 0541 | Official https://www.intrasog.gov.co/wp-content/uploads/2024/03/RESOLUCION-0541.pdf ; INTRASOG's archive has inconsistent displayed date (20/04/2024), but later signed official documents explicitly call it **20 March 2024**. PDF 28 pages, web access returns Cloudflare verification; full text and annexes not read. **Priority primary legal source.** |
| 2024-10-02 | Resolución 2957 | Official https://www.intrasog.gov.co/wp-content/uploads/2024/10/RESOLUCION-2957-POR-LA-CUAL-SE-ORDENA-EL-CIERRE-VIAL-POR-MOTIVO-DE-LA-VUELTA-A-BOYACA-.pdf ; explicitly refers to 0541 as urban transport route regulation for all 4 operators. Temporary road restrictions only. |
| 2024-11-21 | Resolución 3262 | Official https://www.intrasog.gov.co/wp-content/uploads/2024/11/RESOLUCION-3262-DE-NOVIEMBRE-21-DE-2024-TEMPORADA-NAVIDENA.pdf ; independently cites 0541 as the instrument regulating urban routes. Temporary modifications for festivities only. |

Public archive: https://www.intrasog.gov.co/resoluciones-planeacion/ , https://www.intrasog.gov.co/resoluciones-direccion/ .

## What remains unknown

1. Whether 0541 adopted the proposal entirely, partially or with alterations, and the exact line/operator assignments.
2. Whether 0541 repealed/superseded the suspended 10792 provisions, or retains dependencies on earlier permits.
3. Any later *urban* restructuring (not to confuse with **intermunicipal** Resolución 2101-2025, outside project scope).
4. Exact clock-level frequencies and hours per *legally current* route. Study proposal is not equivalent to current official operation.
5. Why official operator websites and current 2026 OSM contain different numbers of routes (possibly proposal vs baseline).

## Generator decision

**Keep urban OSM 30 Sogamoso relations as provisional research candidates; do not apply proposed 20-route study schedule or drop OSM lines yet.** Before production generation, obtain and inspect the PDF contents of 0541, and reconcile with 10792/0015 and any later applicable act. Record original vs proposed route IDs separately.

Provenance for every candidate data point must include document, actual PDF page index or printed page, effective date/status, and whether observed, proposed, regulated or operator-published.
