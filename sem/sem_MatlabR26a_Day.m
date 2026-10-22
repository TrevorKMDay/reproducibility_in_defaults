
% Downloaded community SEM toolbox 
%   (with most downloads, 4.3k on Oct. 22, 2026): 
%   https://www.mathworks.com/matlabcentral/fileexchange/54147-pls-sem-toolbox

% See reference manual:
%   Aria, M. (2015). Example of new PLS-PM matlab toolbox. 
%   https://doi.org/10.13140/RG.2.1.1780.3602

% I'm not sure what to do here ...


data = readtable("sem-stata-Protzko.csv", 'TreatAsMissing', '9999') ;

% Create a single latent variable called recommend
cr_LV_labels = {"recommend"} ;

% Regress this LV 'recommend' on npmcd, npfries, npfood

% Create the matrix that holds this weights
cr_MV = num2cell([0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ...
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) ;

cr_MV_table = table(cr_MV{:}) ;

% Run the model
Mmode = ['A'] ;
method = 'path' ;
max_iter = 300 ;

[results] = plspm(table2array(data), cr_MV_table, ...
    cr_MV_table, Mmode, method, max_iter);