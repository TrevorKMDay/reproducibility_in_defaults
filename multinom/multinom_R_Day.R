# run a multinomial logistic regression, the dependent variable is 
#      'KBH_q1_KBH_q1_5_KBH_q1_grid' 
# (Animals used for food have approximately the same ability to feel pain and 
# discomfort as humans)

# The predictor variables are: country age_int_all gender_all.
# Report the −2 log likelihood chi-square test, 
# the Akaike’s Information Criterion (AIC),
# and the the Wald chi-square test and p-values for age, gender, and country. 

library(tidyverse)

# ver. 7.3-20
library(nnet)

data <- read_csv("~/Projects/comp_rep/multinom/multinom-SPSS-Mata.csv",
                  show_col_types = FALSE)

# data$KBH_q1_KBH_q1_5_KBH_q1_grid

data2 <- data %>%
  select(KBH_q1_KBH_q1_5_KBH_q1_grid, country, age_int_all, gender_all) %>%
  mutate(
    # Country and gender seem to be factors, not numbers
    across(c(country, gender_all), as.factor)
  )

fit1 <- multinom(KBH_q1_KBH_q1_5_KBH_q1_grid ~ country + age_int_all + 
                      gender_all, 
                  data = data2)

# AIC = 13771.91

# Calculate p values

# Extract coefficients and standard errors
coefficients <- summary(fit1)$coefficients
std_errors <- summary(fit1)$standard.errors

# Compute z-scores
z_scores <- coefficients / std_errors

# Compute p-values
p_values <- 2 * (1 - pnorm(abs(z_scores)))
p_values
