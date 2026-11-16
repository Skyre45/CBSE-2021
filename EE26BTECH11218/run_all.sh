#!/bin/bash
# 1) compile and run the C programs (they write the .dat files that the Python programs plot)
# 2) regenerate every figure.   Run from the project root:  bash run_all.sh
cd codes
for c in cbXq16 cbXq20 cbXIIq1 cbXIIq6 cbXIIq14 cbXIIq15 cbXIIq26a cbXIIq26b cbXIIq32 cbXIIq35a; do
  echo "== C $c"; gcc -O2 $c.c -o $c -lm && ./$c
done
cd ..
for q in 6 7 16 17 20 22 25 27 35; do
  echo "== 10 Q$q"; MPLBACKEND=Agg python3 codes/cbXq$q.py
done
for q in 1 3 6 14 15 19a 19b 21a 22 26a 26b 28b 30a 30b 32 35a; do
  echo "== 12 Q$q"; MPLBACKEND=Agg python3 codes/cbXIIq$q.py
done
