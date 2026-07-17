# run a one-way ANOVA, the dependent variable is 'Rating'
# The group variable is Condition.
# Report the F-value, df, p-value, and the partial eta squared

# ver. 1.0.3
# library(effectsize)

vieria <- read.csv(paste0("C:/Users/Trevor/Documents/research/",
                          "reproducibility_in_defaults/anova/",
                          "anova_python_vieira.csv"))

result <- aov(Rating ~ Condition, data = vieria)

summary(result)

# F  = 4.705
# df = 3, 796
# p  = .00291

effectsize::eta_squared(result, partial = TRUE)

# eta^2 = .02