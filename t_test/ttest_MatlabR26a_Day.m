% Requires "Statistics and Machine Learning Toolbox"

data = readtable("ttest_R_Protzko.csv") ;

v0 = data.v1(data.v2 == 0) ;
v1 = data.v1(data.v2 == 1) ;

[h, p, ci, stats] = ttest2(v0, v1);