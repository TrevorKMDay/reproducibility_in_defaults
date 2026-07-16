
import pandas as pd

# Version: 0.14.6
import statsmodels.api as sm
import statsmodels.formula.api as smf

from pathlib import Path

# Load data ====

data = sm.datasets.get_rdataset("dietox", "geepack").data

data = pd.read_stata(Path("~/Projects/comp_rep/mixed_eff") /
                     "2024-07-18-squo-debias-long-blind.dta")

# Fit model ====

# R code to match:
# model_1 <- lmer(loyal ~ squo + (1| id), data = data)
# summary(model_1)

# By default, smf.mixedlm() doesn't handle missing values (or well), so in
# order to get anything, you have to do missing="drop"

md = smf.mixedlm("loyal ~ squo", data, groups=data["id"], missing="drop")
mdf = md.fit()

print(mdf.summary())
