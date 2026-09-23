# quilt-canon-graph

**Knowledge graph of Quilt substrate walker canon with interactive HTML viewer.**

## Quick start

```bash
pip install -e .

# Build & export the graph
quilt-canon-graph build
quilt-canon-graph stats
quilt-canon-graph export --output viewer/canon-graph.json

# Serve the viewer (any static server works)
cd viewer && python3 -m http.server 8000
# Open http://localhost:8000
```

## What the graph shows

- **Nodes** = canon pieces (one per file in `canon_writings/*.md` and substrate-walker/canon/cells/*.md)
- **Node size** ∝ number of doctrines anchored
- **Node color** = first doctrine's color
- **Edges** = shared doctrines between two pieces; weight = number of shared doctrines
- **Edge label** = the doctrines that connect them

## CLI commands

- `build` — build the graph and show cluster summary
- `stats` — node/edge/density statistics
- `query <doctrine>` — list pieces anchored to a doctrine
- `export --output <file>` — export as JSON for the HTML viewer

## Doctrines (color-coded)

| Doctrine | Color |
|----------|-------|
| `cells_are_scars` | red `#e74c3c` |
| `witness_log_is_prediction` | blue `#3498db` |
| `canon_gate_is_chord` | green `#2ecc71` |
| `oracle_is_heard` | purple `#9b59b6` |
| `substrate_quantum` | orange `#f39c12` |

## Fleet integration

- **`quilt-canon-mcp`** — exposes this graph as MCP tools (`get_canon_by_doctrine`)
- **`quilt-canon-search`** — sibling, TF-IDF search over same canon
- **`quilt-multi-oracle`** — multi-model chord verifies the relationships
- **`quilt-iterator`** — referenced for canon refinement
- **`quilt-bridge`** — translates canon across substrates

## The 5 bedrock doctrines

1. `cells_are_scars` — every cell records an attempted entry
2. `witness_log_is_prediction` — the log IS the prediction
3. `canon_gate_is_chord` — canon passes when multiple agents agree
4. `oracle_is_heard` — JEV probes canon with multi-model consensus
5. `substrate_quantum` — the substrate is the walker; canon is substrate-aware

## Polyformalism canary

```bash
python -m quilt_canon_graph.canary
# → 0x24a555471370b18d
```

## License

MIT
