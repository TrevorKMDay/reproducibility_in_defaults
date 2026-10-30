# run a multiple regression, the dependent variable is 'science'
# The predictor variables are math female socst read
# Report the b-values, and p-value for math female socst read

import pandas as pd
import statsmodels.api as sm

data = pd.read_csv("/Users/tkmd/Projects/comp_rep/mult_reg/" + 
                    "multireg_sas_protzko.csv")

preds = ["math", "female", "socst", "read"]

y = data[["science"]]
x = data[preds]
x = sm.add_constant(x)

model = sm.OLS(y, x)
result = model.fit()

rstring = [f"{z}: {round(x, 3)}, p = {round(y, 3)}" for x, y, z in 
            zip(result.params, result.pvalues, ["intercept"] + preds)]
