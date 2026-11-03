
# seed number 41970

# run a test of measurement invariance using defaults
# single latent variable with reflective indicators:
#     sd1 sd2 sd3 sd4 sd5 sd6 sd7 sd8 sd9 sd10
# grouping variable is binary variable 'fast'

# report configural model CFI and RMSEA
# constrain factor loadings to be the same across groups and report 
#     CFI and RMSEA
# also constrain item intercepts to be the same across gorups and report 
#     CFI and RMSEA


import pandas as pd

data = pd.read_csv("/Users/tkmd/Projects/comp_rep/sem/sem_stata_Protzko.csv",
                    na_values=9999)