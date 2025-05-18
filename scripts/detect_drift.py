import pandas as pd
from scipy.stats import ks_2samp

old = pd.read_csv("data/processed/data_train.csv")
new = pd.read_csv("data/processed/data_live.csv")

for col in ["feature1", "feature2"]:
    stat, p = ks_2samp(old[col], new[col])
    if p < 0.05:
        print(f"Dérive détectée sur {col} (p={p:.3f})")
