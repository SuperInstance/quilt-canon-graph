# Canon — quilt-canon-graph

## What this tool is

A knowledge graph of Quilt canon lore. Nodes are canon pieces, edges are shared doctrines. The HTML viewer renders it with vis-network (forceAtlas2 physics, color-coded doctrines, click-to-filter by doctrine).

## How it proves itself

**It runs.** `pip install -e .` then `quilt-canon-graph export` writes JSON, served via any static HTTP server. Tested with 7 tests in `run_tests.py`.

**It polyformalisms.** The canary hash `0x24a555471370b18d` matches across the fleet's 5 ports.

**It measures.** The graph itself is the measurement: edges with weight ≥ 2 are strong canon signals (multi-doctrine anchored).

## Doctrines it instantiates

- **cells_are_scars** — every node is a cell; size = depth of doctrine anchor
- **canon_gate_is_chord** — edges = chord consensus between canon pieces
- **oracle_is_heard** — colors map doctrine→hex; oracle's vocabulary made visual
- **substrate_quantum** — the graph IS a substrate; cells anchor canon

## Commands

1. `build` — build graph + show cluster summary
2. `stats` — node/edge/density
3. `query <doctrine>` — list pieces in a doctrine cluster
4. `export --output <file>` — export graph JSON for the viewer

## Fleet usage

- **`quilt-canon-mcp`** — sibling, exposes `get_canon_by_doctrine` as MCP tool
- **`quilt-canon-search`** — sibling, TF-IDF search over same canon
- **`quilt-multi-oracle`** — multi-model chord (referenced for verification)
- **`quilt-iterator`** — referenced for canon refinement
- **`quilt-bridge`** — translates canon across substrates

## Viewer

The HTML viewer at `viewer/index.html` uses vis-network (CDN) to render the graph. Click a doctrine button to filter. Hover a node to see its body preview.
