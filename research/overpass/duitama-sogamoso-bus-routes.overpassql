[out:json][timeout:180];

// Approximate regional bounding box: Duitama–Sogamoso, Boyacá, Colombia.
// Routes that intersect the bbox may extend well beyond its limits.
// Fetch route relations and route_master relations plus their full
// recursive members (ordered relation members are preserved).
(
  relation["type"="route"]["route"="bus"](5.65,-73.13,5.91,-72.82);
  relation["type"="route_master"]["route_master"="bus"](5.65,-73.13,5.91,-72.82);
)->.routes;

(
  .routes;
  >>;
);

out body qt;
