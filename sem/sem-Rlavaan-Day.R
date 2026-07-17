
# Insructions

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
#     northeast	midwest	west	regionmiss	



library(tidyverse)

# ver. 0.6-21
library(lavaan)

data <- read_csv("~/Projects/comp_rep/sem/sem-stata-Protzko.csv", 
                  show_col_types = FALSE, na = "9999")

model_spec <- "

  recommend =~ npmcd + npfries + npfood

  recommend ~ mcdad + female + age24 + age35 + age44 + age54 + age64 +
    hispanic + black + other + racemiss + lesshs + hsgrad + somecollege +
    less50k + less75k + less100k + northeast + midwest + west + regionmiss

"

# Fit the model
sem1 <- sem(model_spec, data = data)

# Instructions: 
# report model fit via CFI, RMSEA, all standardized paths, p-values, and 
# 95% CIs.

summary(sem1)

fitMeasures(sem1, c("CFI", "RMSEA"))

# cfi:   .991
# rmsea: .026

sem1_standardized <- standardizedSolution(sem1)

# remove covariances?
results <- sem1_standardized %>% 
  filter_out(
    op == "~~"
  ) %>%
  mutate(
    to_copy = str_glue("{lhs} {op} {rhs} = {round(est.std, 3)}, ",
                        "p = {round(pvalue, 3)}, [{round(ci.lower, 3)}, ",
                        "{round(ci.upper, 3)}]")
  )

clipr::write_clip(results$to_copy)
