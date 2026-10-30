# run a Generalized Additive Model (GAM), the dependent variable is PAI_SUI 
# (suicidal Ideation)
# The predictor variables are 
#     the categorical variable Overall_Combined, 
#     categorical variable Gender, and 
#     Age
# Report the coefficients and p-values for the intercept, 
# Overall_Combined levels 1 through 3,
# the overall R2 adjusted and total % deviance explained

import pandas as pd
from pygam import LinearGAM, f, l

data = pd.read_csv("/Users/tkmd/Projects/comp_rep/gams/gams_r_larocca.csv")

# LinearGAM can't handle NaNs
data_noNaN = data.dropna()

y = data_noNaN[["PAI_SUI"]]
x = data_noNaN[["Overall_Combined", "Gender", "Age"]]

# Instructions say to treat these as categories
x["Overall_Combined"], levels1 = pd.factorize(x["Overall_Combined"], 
                                                sort=True)

x["Gender"], levels2 = pd.factorize(x["Gender"], sort=True)

gam = LinearGAM(f(0) + f(1) + l(2))
result = gam.fit(x, y)

# R2 adjusted
r2_adj = float(result.statistics_["pseudo_r2"]["McFadden_adj"])

# deviance
dev = 100 - float(result.statistics_["deviance"])

oc_terms = gam.terms.get_coef_indices(0)
gen_terms = gam.terms.get_coef_indices(1)
age_term = gam.terms.get_coef_indices(2)[0]

oc_string = [f"OC={x}: {round(y, 3)}" for x, y in zip(levels1, result.coef_[oc_terms])]
gen_string = [f"gender={x}: {round(y, 3)}" for x, y in zip(levels2, result.coef_[gen_terms])]
age_string = f"age: {round(float(result.coef_[age_term]), 3)}"

[float(round(x, 3)) for x in result.statistics_["p_values"]]

"; ".join([", ".join(oc_string), ", ".joing(gen_string), age_string])
