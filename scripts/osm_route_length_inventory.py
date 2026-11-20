#!/usr/bin/env python3
"""Inventory OSM bus routes and length of their ordered member ways.

Usage:
    python scripts/osm_route_length_inventory.py "export (6).json" > research/osm-urban-route-metrics.csv

The length is the sum of the node-to-node Haversine lengths of all way
members, not an independently surveyed or validated timetable distance.
"""
import argparse
import csv
import json
import math
import sys
from collections import Counter

URBAN_NETWORKS = {
    "Urbano Duitama",
    "Servicio de Transporte Urbano Duitama",
    "Urbano Sogamoso",
}


def km(a, b):
    la1, lo1 = math.radians(a["lat"]), math.radians(a["lon"])
    la2, lo2 = math.radians(b["lat"]), math.radians(b["lon"])
    angle = (
        math.sin((la2 - la1) / 2) ** 2
        + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    )
    return 12742 * math.asin(min(1, math.sqrt(angle)))


def inventory(data):
    objects = {(e["type"], e["id"]): e for e in data["elements"]}
    for r in data["elements"]:
        if r["type"] != "relation" or r.get("tags", {}).get("route") != "bus":
            continue
        tags = r.get("tags", {})
        if tags.get("network") not in URBAN_NETWORKS:
            continue
        missing_ways = missing_nodes = total = stop_members = 0
        endpoints = []
        kinds = Counter()
        for m in r.get("members", []):
            kinds[m["type"]] += 1
            if m.get("role", "").lower() in {"stop", "platform", "stop_entry_only", "stop_exit_only"}:
                stop_members += 1
            if m["type"] != "way":
                continue
            w = objects.get(("way", m["ref"]))
            if w is None:
                missing_ways += 1
                continue
            previous = None
            first = None
            last = None
            for nodeid in w.get("nodes", []):
                node = objects.get(("node", nodeid))
                if node is None:
                    missing_nodes += 1
                    previous = None
                    continue
                if previous is not None:
                    total += km(previous, node)
                if first is None:
                    first = node
                last = node
                previous = node
            if first is not None and last is not None:
                endpoints.append((first, last))
        gaps_km = [
            min(km(a, c), km(a, d), km(b, c), km(b, d))
            for (a, b), (c, d) in zip(endpoints, endpoints[1:])
        ]
        yield {
            "osm_relation_id": r["id"],
            "ref": tags.get("ref", ""),
            "name": tags.get("name", ""),
            "network": tags.get("network", ""),
            "operator": tags.get("operator", ""),
            "member_way_count": kinds["way"],
            "member_node_count": kinds["node"],
            "member_stop_roles": stop_members,
            "missing_ways": missing_ways,
            "missing_nodes": missing_nodes,
            "member_way_length_km": round(total, 3),
            "gaps_over_100m": sum(x > 0.1 for x in gaps_km),
            "gaps_over_500m": sum(x > 0.5 for x in gaps_km),
            "largest_member_gap_km": round(max(gaps_km, default=0), 3),
            "interval": tags.get("interval", ""),
            "opening_hours": tags.get("opening_hours", ""),
        }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("osm_json", help="Raw Overpass JSON (not GeoJSON)")
    args = parser.parse_args()
    with open(args.osm_json, encoding="utf-8") as stream:
        data = json.load(stream)
    rows = sorted(inventory(data), key=lambda r: (r["network"], r["ref"], r["osm_relation_id"]))
    fields = list(rows[0]) if rows else []
    writer = csv.DictWriter(sys.stdout, fields)
    writer.writeheader()
    writer.writerows(rows)


if __name__ == "__main__":
    main()
