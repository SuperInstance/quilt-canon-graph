"""Test runner for quilt-canon-graph (no pytest dep)."""
import sys

sys.path.insert(0, "/workspace/repos/quilt-canon-graph")

from quilt_canon_graph.canary import canary
from quilt_canon_graph.graph import build_graph, get_doctrine_cluster
from quilt_canon_graph.loader import DOCTRINES

results = []
failures = []


def test(name, func):
    try:
        func()
        results.append((name, "PASS"))
    except AssertionError as e:
        results.append((name, f"FAIL: {e}"))
        failures.append(name)
    except Exception as e:
        results.append((name, f"ERROR: {type(e).__name__}: {e}"))
        failures.append(name)


def t_canary():
    assert canary() == "0x24a555471370b18d"


def t_build_graph():
    g = build_graph()
    assert g["n_nodes"] > 0
    assert g["n_doctrines"] == 5
    assert isinstance(g["edges"], list)


def t_edges_have_weight():
    g = build_graph()
    if g["edges"]:
        e = g["edges"][0]
        assert "weight" in e
        assert "doctrines" in e
        assert e["weight"] >= 1


def t_clusters():
    g = build_graph()
    assert len(g["clusters"]) == 5
    for c in g["clusters"]:
        assert "doctrine" in c
        assert "size" in c


def t_doctrine_query():
    g = build_graph()
    pieces = get_doctrine_cluster(g, "cells_are_scars")
    assert isinstance(pieces, list)
    assert len(pieces) > 0


def t_doctrine_color():
    from quilt_canon_graph.graph import _doctrine_color
    assert _doctrine_color(["cells_are_scars"]) == "#e74c3c"
    assert _doctrine_color(["witness_log_is_prediction"]) == "#3498db"
    assert _doctrine_color([]) == "#888888"


def t_node_attrs():
    g = build_graph()
    n = g["nodes"][0]
    assert "id" in n
    assert "doctrines_hit" in n
    assert "size" in n
    assert "color" in n


test("test_canary", t_canary)
test("test_build_graph", t_build_graph)
test("test_edges_have_weight", t_edges_have_weight)
test("test_clusters", t_clusters)
test("test_doctrine_query", t_doctrine_query)
test("test_doctrine_color", t_doctrine_color)
test("test_node_attrs", t_node_attrs)

print("\n=== quilt-canon-graph test results ===")
for name, status in results:
    print(f"  {status:60} {name}")

print(f"\n{len(results) - len(failures)}/{len(results)} passed")
if failures:
    sys.exit(1)
