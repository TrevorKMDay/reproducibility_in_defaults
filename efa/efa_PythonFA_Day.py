

# Instructions:

# Conduct an exploratory factor analysis on the 16 items from the SSWQ using 
# software defaults to the greatest extent possible to produce results

# Extract a 4 factor solution

# Report on the default factoring method (e.g., maximum likelihood, minres), 
# default factor rotation method (e.g., none, oblimin), pattern matrix loadings, 
# and model fit indices chi-square, CFI, TLI, and RMSEA.

# NOTES:
# 1. It is ok if the software default is to conduct a principal components 
#    analysis rather than a true common factors analysis EFA, just make a note 
#    of this
# 2. If any of the fit indices are not available, just report "NA"

import pandas as pd

# NOTE: MUST USE GITHUB VERSION:
# pip install \
#     git+https://github.com/EducationalTestingService/factor_analyzer.git
# SEE ISSUE: 
#     https://github.com/EducationalTestingService/factor_analyzer/issues/148
from factor_analyzer import FactorAnalyzer

data = pd.read_csv("/Users/tkmd/Projects/comp_rep/efa/efa_R_Roberson.csv")

# Default rotation='promax', method='minres'
# See docs: \
#     https://factor-analyzer.readthedocs.io/en/latest/factor_analyzer.html#
#     factor_analyzer.factor_analyzer.FactorAnalyzer
fa4 = FactorAnalyzer(n_factors=4)
result = fa4.fit(data)

# Pretty print out loadings for entry into doc
loadings = pd.DataFrame(result.loadings_, columns=["F1", "F2", "F3", "F4"])
loadings2 = round(loadings, 3)

# Concatenate each column
single_strings = [loadings2[x].astype(str).str.cat(sep=', ') 
                  for x in ["F1", "F2", "F3", "F4"]]

final_string = "; ".join(single_strings)
