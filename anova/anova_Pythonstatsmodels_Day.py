import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# This is the verification of the results reported in the paper

# paper: https://doi.org/10.1007/s13164-025-00785-w
# prereg: https://osf.io/ajf2g/overview?view_only=03812bd3b53d41f5a9323a52e1aadb85

# dep var:   rating
# group var: condition
# report:    f-value, df, p-value, and partia eta squared

vieria = pd.read_csv("/Users/tkmd/Projects/comp_rep/anova/" +
                     "anova_python_vieira.csv")

model = ols("Rating ~ C(Condition)", data=vieria).fit()

anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

#                    sum_sq     df         F    PR(>F)
# C(Condition)    415514.95    3.0  4.704984  0.002905
# Residual      23432592.87  796.0       NaN       NaN

ss_effect = anova_table.loc['C(Condition)', 'sum_sq']
ss_error = anova_table.loc['Residual', 'sum_sq']

partial_eta_squared = ss_effect / (ss_effect + ss_error)
print(f"Partial Eta Squared: {partial_eta_squared:.3f}")
