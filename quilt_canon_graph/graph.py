"""Build a knowledge graph from canon pieces.

Nodes = canon pieces
Edges = shared doctrines (weight = number of shared doctrines)
Edge "title" attribute = doctrine names that connect them
"""
from typing import Dict, List

from .loader import DOCTRINES, load_canon


def build_graph() -> Dict:
    """Build the canon knowledge graph."""
    pieces = load_canon()
    nodes = []
    edges = []

    # Nodes
    for p in pieces:
        nodes.append({
            "id": p.name,
            "label": p.title,
            "doctrines_hit": p.doctrines_hit,
            "tags": p.tags,
            "characters": p.characters,
            "size": 5 + len(p.doctrines_hit) * 5,  # bigger = more doctrines
            "color": _doctrine_color(p.doctrines_hit),
            "body_preview": p.body[:100] if p.body else "",
        })

    # Edges (pairwise shared doctrines)
    edge_set = {}  # (a, b) -> list of doctrines
    for i, p1 in enumerate(pieces):
        for p2 in pieces[i + 1:]:
            shared = set(p1.doctrines_hit) & set(p2.doctrines_hit)
            if shared:
                key = tuple(sorted([p1.name, p2.name]))
                edge_set[key] = sorted(shared)

    for (a, b), doctrines in edge_set.items():
        edges.append({
            "source": a,
            "target": b,
            "weight": len(doctrines),
            "doctrines": doctrines,
            "label": ", ".join(doctrines),
        })

    # Doctrine cluster centers
    clusters = []
    for d in DOCTRINES:
        cluster_pieces = [p.name for p in pieces if d in p.doctrines_hit]
        if cluster_pieces:
            clusters.append({
                "doctrine": d,
                "size": len(cluster_pieces),
                "pieces": cluster_pieces[:10],  # first 10
            })

    return {
        "n_nodes": len(nodes),
        "n_edges": len(edges),
        "n_doctrines": len(DOCTRINES),
        "nodes": nodes,
        "edges": edges,
        "clusters": clusters,
    }


def _doctrine_color(doctrines: List[str]) -> str:
    """Map doctrine set to color hex."""
    if not doctrines:
        return "#888888"
    # Pick the first doctrine's color
    colors = {
        "cells_are_scars": "#e74c3c",           # red
        "witness_log_is_prediction": "#3498db",  # blue
        "canon_gate_is_chord": "#2ecc71",        # green
        "oracle_is_heard": "#9b59b6",            # purple
        "substrate_quantum": "#f39c12",          # orange
    }
    for d in doctrines:
        if d in colors:
            return colors[d]
    return "#1abc9c"


def get_doctrine_cluster(graph: Dict, doctrine: str) -> List[str]:
    """Get all canon piece names in a doctrine cluster."""
    for c in graph.get("clusters", []):
        if c["doctrine"] == doctrine:
            return c["pieces"]
    return []
