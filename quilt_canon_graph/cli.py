"""CLI for quilt-canon-graph."""
import argparse
import json
from pathlib import Path

from .graph import build_graph, get_doctrine_cluster
from .loader import DOCTRINES


def cmd_build(args):
    g = build_graph()
    print(f"✓ Built canon graph: {g['n_nodes']} nodes, {g['n_edges']} edges, {g['n_doctrines']} doctrines")
    print(f"\nDoctrine clusters:")
    for c in g["clusters"]:
        print(f"  • {c['doctrine']:30s} → {c['size']} pieces")


def cmd_query(args):
    g = build_graph()
    pieces = get_doctrine_cluster(g, args.doctrine)
    print(f"Found {len(pieces)} pieces anchored to '{args.doctrine}':")
    for p in pieces[:args.limit]:
        print(f"  • {p}")


def cmd_export(args):
    """Export graph as JSON for the HTML viewer."""
    g = build_graph()
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(g, indent=1))
    print(f"✓ Exported graph → {out}")


def cmd_stats(args):
    g = build_graph()
    density = (2 * g["n_edges"]) / max(1, g["n_nodes"] * (g["n_nodes"] - 1))
    print(f"Nodes: {g['n_nodes']}")
    print(f"Edges: {g['n_edges']}")
    print(f"Doctrines: {g['n_doctrines']}")
    print(f"Density: {density:.4f}")
    print(f"Avg degree: {2 * g['n_edges'] / max(1, g['n_nodes']):.2f}")


def main():
    p = argparse.ArgumentParser(description="quilt-canon-graph — knowledge graph of canon lore")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("build", help="Build and summarize the graph").set_defaults(func=cmd_build)
    sub.add_parser("stats", help="Show graph statistics").set_defaults(func=cmd_stats)

    p_q = sub.add_parser("query", help="Get pieces in a doctrine cluster")
    p_q.add_argument("doctrine")
    p_q.add_argument("--limit", type=int, default=10)
    p_q.set_defaults(func=cmd_query)

    p_e = sub.add_parser("export", help="Export graph as JSON")
    p_e.add_argument("--output", default="canon-graph.json")
    p_e.set_defaults(func=cmd_export)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
