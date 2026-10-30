# run a multinomial logistic regression, the dependent variable is 
#      'KBH_q1_KBH_q1_5_KBH_q1_grid' 
# (Animals used for food have approximately the same ability to feel pain and 
# discomfort as humans)

# The predictor variables are: country age_int_all gender_all.
# Report the −2 log likelihood chi-square test, 
# the Akaike’s Information Criterion (AIC),
# and the the Wald chi-square test and p-values for age, gender, and country. 

import pandas as pd
import statsmodels.api as sm

data = pd.read_csv("/Users/tkmd/Projects/comp_rep/multinom/" + 
                    "multinom_SPSS_Mata.csv")

outcome = "KBH_q1_KBH_q1_5_KBH_q1_grid"
preds = ["country", "age_int_all", "gender_all"]

y = data[[outcome]]
x = data[preds]
x = sm.add_constant(x)

# fit the model
model = sm.MNLogit(y, x)
result = model.fit()

print(result.summary())

# -2 *LL 
-2 * float(result.llf)

# AIC
float(result.aic)

# wald chi-sq

result_strings = []

# outcome levels
for i in [2, 3, 4, 5]:
    for j in preds:
        wald = result.wald_test(f"y{i}_{j} = 0", scalar=True)
        string = f"y={i}, x={j}: wald({wald.df_denom}) = " + \
                    f"{round(wald.statistic, 3)}, " + \
                    f"p = {round(wald.pvalue, 3)}"
        result_strings += [string]
        
final_string = "; ".join(result_strings)
