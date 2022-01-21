function [optimal_soln] = gasolver(x)

lb = [2; 1.05; 0.26];
ub = [18; 9.42; 2.37];

population_size = x(1);
num_generations = x(2);
crossover_prob = x(3);
mutation_prob = x(4);

options = optimoptions('ga', ...
    'PopulationSize', population_size, ...
    'MaxGenerations', num_generations, ...
    'MaxStallGenerations', num_generations, ...
    'CrossoverFraction', crossover_prob, ...
    'MutationFcn', {'mutationuniform', mutation_prob}, ...
    'SelectionFcn', 'selectionroulette', ...
    'EliteCount', 2, ...
    'PlotFcn', @gaplotbestf2);

optimal_soln = ga(@fitness, 3, [], [], [], [], lb, ub, [], options);
