# Instructions:

# Specify a correlated (oblique) factors model with 4 reflective latent factors 
# with 4 indicator items each as follows

# Note: jl = Joy of Learning, sc = School Connectedness, 
#       ep = Educational Purpose, ae = Academic Efficacy
# jl: SSWQ1, SSWQ5, SSWQ9, SSWQ13
# sc: SSWQ2, SSWQ6, SSWQ10, SSWQ14
# ep: SSWQ3, SSWQ7, SSWQ11, SSWQ15
# ae: SSWQ4, SSWQ8, SSWQ12, SSWQ16

# Allow covariances to be freely estimated between all factors
# Otherwise keep all software defaults to the greatest extent possible to 
#     produce results

# Report default estimator used (e.g., maximum likelihood, WLSMV), 
# standardized factor loadings, and global data-model fit indices CFI, TLI, 
# and RMSEA

import pandas as pd
from semopy import Model, calc_stats

data = pd.read_csv("~/Projects/comp_rep/cfa/cfa_R_Roberson.csv")

model_spec = """

    jl =~ SSWQ1 + SSWQ5 + SSWQ9  + SSWQ13
    sc =~ SSWQ2 + SSWQ6 + SSWQ10 + SSWQ14
    ep =~ SSWQ3 + SSWQ7 + SSWQ11 + SSWQ15
    ae =~ SSWQ4 + SSWQ8 + SSWQ12 + SSWQ16

"""

m = Model(model_spec)

fit = m.fit(data,)

estimates = m.inspect()
std_estimates = m.inspect(std_est=True)

stats = calc_stats(m)
stats[["CFI", "TLI", "RMSEA"]]

# Create string to copy-paste

std_est_16 = std_estimates.iloc[0:15]

string1 = [f"{x} =~ {y}: {v:.3f}" for x, y, v in 
            zip(std_est_16.rval, std_est_16.lval, std_est_16["Est. Std"])]

# import numpy as np
# from factor_analyzer import ConfirmatoryFactorAnalyzer, ModelSpecificationParser

# model_dict = {
#     "jl": ["SSWQ1", "SSWQ5", "SSWQ9", "SSWQ13"],
#     "sc": ["SSWQ2", "SSWQ6", "SSWQ10", "SSWQ14"],
#     "ep": ["SSWQ3", "SSWQ7", "SSWQ11", "SSWQ15"],
#     "ae": ["SSWQ4", "SSWQ8", "SSWQ12", "SSWQ16"],
# }

# raw_array = data.to_numpy().copy()

# model_spec_fa = ModelSpecificationParser.parse_model_specification_from_dict(raw_array, model_dict)

# # 4. Initialize and fit the CFA model
# cfa = ConfirmatoryFactorAnalyzer(model_spec_fa, disp=False)
# cfa.fit(raw_array.values)
