% Requires "Statistics and Machine Learning Toolbox"

data = readtable("pairedttest_R_Protzko.csv") ;

% Instructions
% run a paired-samples t-test, the dependent variable is 'loyal'
% The two variables are RightMyth and RightProcedural
% Report the t-test, df, and p-value

[h, p, ci, stats] = ttest(data.RightMyth, data.RightProcedural);