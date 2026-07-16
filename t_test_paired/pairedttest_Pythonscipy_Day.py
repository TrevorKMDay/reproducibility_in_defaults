
import pandas as pd

# ver. 2.4.6
import numpy as np

# ver. 1.17.1
from scipy import stats
from pathlib import Path

# Instructions ====

# run a paired-samples t-test, the dependent variable is 'loyal'
# The two variables are RightMyth and RightProcedural
# Report the t-test, df, and p-value

data = pd.read_csv(Path("~/Projects/comp_rep/t_test_paired/") /
                        "pairedttest_R_Protzko.csv")

ttest_result = stats.ttest_rel(data["RightMyth"], data["RightProcedural"])

print(f"t({ttest_result.df}) = {ttest_result.statistic}, p = {ttest_result.pvalue}")
