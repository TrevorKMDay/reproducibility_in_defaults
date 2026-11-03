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

# report model fit via CFI, RMSEA, all standardized paths, p-values, and 
#   95% CIs.

from pandas.core.arrays import numeric
import pandas as pd
from semopy import Model, calc_stats

data = pd.read_csv("/Users/tkmd/Projects/comp_rep/sem/sem_stata_Protzko.csv",
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
estimates = m.inspect(std_est=True)

stats = calc_stats(m)
stats[["CFI", "RMSEA"]]

# Format results for table

def format(string):

    if string == "-":
        return(None)
    else:
        to_float = float(string)
        return(f"{to_float:.3f}")

def ci(m, se):

    if se == "-":
        return(["-, -"])

    low = m - 1.96 * se
    high = m + 1.96 * se
    
    return(f"[{low:.3f}, {high:.3f}]")

# Set this to "Estimate" to use the unstandardized estimate
est = "Est. Std"

estimates["CI"] = [ci(x, y) for x, y in 
                    zip(estimates[est], estimates["Std. Err"])]

estimates["string"] = [
    f"{lh} {op} {rh} = {est:.3f} {ci} (p = {format(p)})" for 
        lh, op, rh, est, ci, p in 
        zip(estimates["lval"], estimates["op"], estimates["rval"], 
            estimates[est], estimates["CI"], 
            estimates["p-value"])
    ]


estimates["string"].str.cat(sep = "; ")
