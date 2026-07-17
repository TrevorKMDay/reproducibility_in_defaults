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

library(tidyverse)

# ver. 0.7-2
library(lavaan)

data <- read_csv("~/Projects/comp_rep/efa/efa_R_Roberson.csv", 
                  show_col_types = FALSE)

# default estimator: ML
# default rotation: geomin
efa1 <- efa(data, nfactors = 4)

fitMeasures(efa1, c("chisq", "CFI", "TLI", "RMSEA"))

#        nfct=4
# chisq 165.025
# cfi     0.987
# tli     0.976
# rmsea   0.040

results <- summary(efa1)$model.list$nf4$efa$lambda[[1]] %>%
  as_tibble(rownames = "var") %>%
  mutate(
    across(starts_with("f"), ~round(as.numeric(.x), 3)),
    to_copy = str_glue("{var}, {f1}, {f2}, {f3}, {f4}")
  )

clipr::write_clip(results$to_copy)
