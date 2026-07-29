# Instructions

# SEM

# make a latent variable called recommend with the following three variables: 
#      npmcd npfries npfood
# missing data values are 9999.

# make as predictors of the latent variable the following variables:
# mcdad	
#  	female	age24	age35	age44	age54	age64
#     hispanic	black	other racemiss
#     lesshs	hsgrad	somecollege
#     less50k	less75k	less100k	
#     northeast	midwest	west regionmiss	

from pandas.core.arrays import numeric
import pandas as pd
from semopy import Model, calc_stats

data = pd.read_csv("/Users/tkmd/Projects/comp_rep/sem/sem-stata-Protzko.csv",
                    na_values=9999)

data.isna().sum().sum()

# Triple quotes allows newlines
model_string = """

recommend =~ npmcd + npfries + npfood

recommend ~ mcdad + female + age24 + age35 + age44 + age54 + age64 + \
    hispanic + black + other + racemiss + lesshs + hsgrad + somecollege + \
    less50k + less75k + less100k + northeast + midwest + west + regionmiss

"""

m = Model(model_string)

opt_res = m.fit(data)
estimates = m.inspect()

stats = calc_stats(m)
stats[["CFI", "RMSEA"]]

def format(string):

    if string == "-":
        return("NA")
    else:
        to_float = float(string)
        return(f"{to_float:.3f}")

estimates["string"] = [
    f"{lh} {op} {rh} = {est:.3f} ({format(se)}, p = {format(p)})" for 
        lh, op, rh, est, se, p in 
        zip(estimates["lval"], estimates["op"], estimates["rval"], 
            estimates["Estimate"], estimates["Std. Err"], estimates["p-value"])
    ]


estimates["string"].str.cat(sep = "; ")
