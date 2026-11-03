# run a survival analysis. Note this data is in wide format and may need to be 
#     reshaped to long with an added categorical period variable (1–5).
# The variables d1 through d5 indicate whether someone dropped out of one of 
#     5 pages of an online study.
# The predictors of dropping out are the big 5 variables 
#      'o' (openness), 
#      'co' (conscientiousness), 
#      'e' (extraversion', 
#      'a' (agreeableness) and 
#      'n' (neuroticism):

# Report b coefficient, z-value, p-value, and odds ratio.


import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
from math import exp

# Load data
data = pd.read_csv("/Users/tkmd/Projects/comp_rep/surv_analysis/" + 
                      "survival_mplus_nestler.csv",
                    dtype={"id": str})

covars = ["o", "co", "e", "a", "n"]

data_long = pd.melt(
    data,
    id_vars=['id'] + covars,
    value_vars=["d1", "d2", "d3", "d4", "d5"],
    var_name="period",
    value_name="event"
)

# Pivot longer
data_long["period"] = [float(x.replace("d", "")) for x in data_long["period"]]

model = smf.logit(
    "event ~ C(period) + o + co + e + a + n",
    data = data_long
).fit()

print(model.summary())

coefs = model.params[5:10]
z = model.tvalues[5:10]
p = model.pvalues[5:10]
odds = [exp(b) for b in coefs]

strings = [f"{v}: b={b:.3f}, z={z:.3f}, p={p:.3f}, OR={OR:.3f}" 
           for v, b, z, p, OR in zip(covars, coefs, z, p, odds)]

final_string = "; ".join(strings)
