% run a 2x3 chi-square test.
% The first variables are quartile and covidence_support
% Report the χ2, df, and p-value

data = readtable("chi2_r_schiekiera.csv") ;

% No built-in method I could find, or available in a package that didn't
% require doing it by hand