# GTFS Duitama–Sogamoso (Colombia)

Open-source research and reproducible GTFS preparation for urban and intermunicipal bus services around Duitama and Sogamoso, Boyacá.

## Research phase: OSM inventory

Run the Overpass query at [`research/overpass/duitama-sogamoso-bus-routes.overpassql`](research/overpass/duitama-sogamoso-bus-routes.overpassql) in [Overpass Turbo](https://overpass-turbo.eu/).

1. Execute the query.
2. Export **raw OSM JSON** (not GeoJSON), retaining relation membership and OSM tags.
3. Save the result locally as `osm/duitama-sogamoso-bus-routes.json` for analysis (do not commit the potentially large raw export yet).
4. Inventory each bus route relation and route master, including OSM id, `ref`, `name`, `operator`, `from`, `to`, stop sequence, direction and geometry.
5. Compare against the historical GitLab GTFS, keeping route identity and direction separate.
6. Only after comparison, configure [Trufi GTFS Builder](https://github.com/trufi-association/trufi-gtfs-builder) and validate its output using MobilityData GTFS Validator.

**Scope:** The query uses an approximate bounding box around Duitama and Sogamoso and may return regional routes. A route intersecting the box is included in full; inclusion in OSM does not independently establish current operation or legal validity.

**Data provenance and licensing:** OSM-derived output must retain OpenStreetMap contributors' attribution and comply with ODbL 1.0. Do not treat assumed headways or operating windows as verified schedules.
