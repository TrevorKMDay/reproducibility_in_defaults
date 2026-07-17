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

library(tidyverse)

# ver. 0.7-2
library(lavaan)

data <- read_csv("~/Projects/comp_rep/cfa/cfa_R_Roberson.csv", 
                  show_col_types = FALSE)

model_spec <- "

    jl =~ SSWQ1 + SSWQ5 + SSWQ9 + SSWQ13
    sc =~ SSWQ2 + SSWQ6 + SSWQ10 + SSWQ14
    ep =~ SSWQ3 + SSWQ7 + SSWQ11 + SSWQ15
    ae =~ SSWQ4 + SSWQ8 + SSWQ12 + SSWQ16

"

# estimator: ML
cfa1 <- cfa(model_spec, data = data)

fitMeasures(cfa1, c("CFI", "TLI", "RMSEA"))

#   cfi   tli rmsea 
# 0.936 0.922 0.072 