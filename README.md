# reproducibility_in_defaults

Trevor Day's (<trevor.day@georgetown.edu>) computational reproductibility code
for John Protzko's "*Reproducibility? in Different Stats program defaults*"
[project][1] from [SIPS 2026][2].

## Tests I did

- **Independent *t*-test**
  - Python (`statsmodels`, v. 0.14.6),
  - MATLAB (R26a; SMLTK)
- **Paired *t*-test**:
  - Python (`scipy` v. 1.17.1),
  - MATLAB (R26a; SMLTK)
- **ANOVA**:
  - R (`effectsize` v. 1.0.3)
- **SEM**:
  - R (`lavaan` v. 0.7-2)
  - Python (`semopy` v. 2.3.11)
- **EFA**:
  - R (`lavaan` v. 0.7-2)
- **CFA**:
  - R (`lavaan` v. 0.7-2)
- **Chi-squared**:
  - MATLAB (R26a), no solution
  - Python (`scipy` v. 1.17.1)
- **Mixed-effects**:
  - Python (`statsmodels` v. 0.14.6)
- **Multinominal logistic regression**:
  - R (`nnet` v. 7.3-20)

SMLTK: *Stats and Machine Learning Toolkit*

OSF link: <https://osf.io/jazrg/files/osfstorage>

[1]: https://osf.io/94uep/overview
[2]: https://www.improvingpsych.org/SIPS2026/