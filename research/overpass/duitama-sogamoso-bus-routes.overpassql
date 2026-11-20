[out:json][timeout:240];

// Duitama and Sogamoso, Boyacá, Colombia.
// Enlarged regional bbox (south,west,north,east):
// 5.55,-73.22,6.05,-72.73
// Encompasses mapped municipal extents plus a buffer.
// Relations intersecting the bbox may extend well outside it.
// Export raw OSM JSON to retain relation member order and tags.
(
  relation["type"="route"]["route"="bus"](5.55,-73.22,6.05,-72.73);
  relation["type"="route_master"]["route_master"="bus"](5.55,-73.22,6.05,-72.73);
)->.routes;

(
  .routes;
  >>;
);

out body qt;
