#!/bin/bash
# Regenerates every figure in figs/ (run from the project root).
for q in 6 7 16 17 19 20 22 25 27 34 35; do
  echo "== Q$q"; MPLBACKEND=Agg python3 codes/cbXq$q.py
done
for q in 1 3 6 7 14 15 19a 19b 21a 22 26a 26b 28b 29 30a 30b 32 35a 35b; do
  echo "== XII Q$q"; MPLBACKEND=Agg python3 codes/cbXIIq$q.py
done
