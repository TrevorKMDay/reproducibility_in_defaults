import pandas as pd

# Version: 0.14.6
from statsmodels.stats.weightstats import ttest_ind

from pathlib import Path


data = pd.read_csv(Path("~/Projects/comp_rep/t_test/") /
                        "ttest_R_Protzko.csv")

x1 = [x for x, y in zip(data["v1"], data["v2"]) if y == 0]
x2 = [x for x, y in zip(data["v1"], data["v2"]) if y == 1]

tstat, pvalue, df = ttest_ind(x1, x2)

print(f"t({df}) = {round(tstat, 2)}, p = {round(pvalue, 3)}")
