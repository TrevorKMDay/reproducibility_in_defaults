import pandas as pd 
from scipy.stats import chi2_contingency

# run a 2x3 chi-square test.
# The first variables are quartile and covidence_support
# Report the χ2, df, and p-value


data = pd.read_csv("/Users/tkmd/Projects/comp_rep/chi_square/chi2_r_schiekiera.csv")

contingency = pd.crosstab(data["quartile"], data["covidence_support"])

stat, p, dof, expected = chi2_contingency(contingency)

print(f"chi2 = {stat:.3f}, p-value: {p:.3f}")
