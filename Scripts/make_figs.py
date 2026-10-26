"""Q1 illustration: simple random vs stratified sampling on a population with a 1% rare class.

Run from anywhere:  python Scripts/make_figs.py   ->  Results/q1_srs_vs_stratified.png
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent.parent / "Results"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"figure.dpi": 150, "axes.spines.top": False, "axes.spines.right": False, "font.size": 11})
rng = np.random.default_rng(42)

# Population: 10,000 items, 100 of them rare (1%). Take a 200-item sample (2%) 2,000 times.
N, rare, n, reps = 10_000, 100, 200, 2000
pop = np.zeros(N, int)
pop[:rare] = 1
srs = np.array([pop[rng.choice(N, n, replace=False)].sum() for _ in range(reps)])
# Stratified: take 2% of each stratum -> exactly 2 rare + 198 common items every time.

fig, ax = plt.subplots(figsize=(7.5, 3.6))
vals, counts = np.unique(srs, return_counts=True)
ax.bar(vals - 0.2, counts / reps * 100, width=0.4, color="#7f8c8d", label="Simple random sampling")
ax.bar([2.2], [100], width=0.4, color="#2e86c1", label="Stratified sampling")
ax.set_xlabel("Rare-class items in a sample of 200 (true expected value = 2)")
ax.set_ylabel("% of 2,000 repeated samples")
ax.set_title("Sampling a population with a 1% rare class")
ax.legend(frameon=False)
zero = np.mean(srs == 0) * 100
ax.annotate(f"{zero:.0f}% of random samples\ncontain NO rare items", xy=(-0.2, zero), xytext=(4.3, 55),
            arrowprops=dict(arrowstyle="->", color="#c0392b"), color="#c0392b")
fig.tight_layout()
fig.savefig(OUT / "q1_srs_vs_stratified.png")
print(f"Samples with zero rare items: {zero:.1f}%   range: {srs.min()}–{srs.max()}")
