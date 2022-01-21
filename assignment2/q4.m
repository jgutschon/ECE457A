close all;
clear all;

% i. 10 different random starting points
min = -100;
max = 100;
r = min + rand(1, 2) * (max - min);

% ii. 10 different initial temperatures, random in range


% iii. Annealing schedules - 3 of each with different alphas
% Linear

% Exponential

% Slow

% Generate options
options = optimoptions(@simulannealbnd,)

ObjectiveFunction = @simple_objective;
x0 = [r(1) r(2)];
lb = [min min];
ub = [max max];
[x,fval,exitFlag,output] = simulannealbnd(ObjectiveFunction, x0, lb, ub)


% Easom function
function easom = simple_objective(x)

x1 = x(1);
x2 = x(2);
easom = -1 .* cos(x1) .* cos(x2) .* exp(-1.*(x1-pi).^2 - (x2-pi).^2);

end
