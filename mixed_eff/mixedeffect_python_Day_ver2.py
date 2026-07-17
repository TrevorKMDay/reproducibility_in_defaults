# Python: 3.14.6

# ver. 3.0.3
import pandas as pd

# Version: 0.14.6
import statsmodels.formula.api as smf

from pathlib import Path

# Instructions

# run a mixed effects model, the dependent variable is 'loyal'
# squo is a binary predictor, scenario is a factor variable.

# Specification 1: First fit the model with random intercepts and slopes of
# squo for each id. Additionally, there are random intercepts for each scenario,
# which are allowed to covary with the random effects of id.

# Specification 2: If that does not converge or is singular, run the model with
# a fixed intercept and a fixed effect of squo. Randomly varying intercepts and
# slopes are estimated for id and scenarios, but these random effects are forced
# to be uncorrelated.

# Specification 3: If that does not converge or is singular make the random
# slopes/intercepts for squo and id correlated but only include a random
# intercept for scenario.

# Specification 4: If that does not converge or is singular make the random
# slopes for squo and id uncorrelated and only include a random intercept of
# scenario.

# Specification 5: If that does not converge or is singular, make uncorrelated
# random slopes for the scenario and only a random intercept of id.

# Specification 6: If that does not converge or is singular, include only
# random intercepts of id and scenario.

# Specification 7: If that does not converge or is singular, include only
# random intercepts of id make scenario a fixed effect.

# Load data ====

data = pd.read_csv(Path("~/Projects/comp_rep/mixed_eff/") /
                        "mixed-stata_protzko.csv")

# Fit model ====

# R code to match:

# model_1 <- lmer(loyal ~ squo + (1| id), data = data)
# summary(model_1)

# By default, smf.mixedlm() doesn't handle missing values (or well), so in
# order to get anything, you have to do missing="drop"

# Model specification
md = smf.mixedlm("loyal ~ squo", data, groups=data["id"], missing="drop")

# run fit
mdf = md.fit()

print(mdf.summary())
