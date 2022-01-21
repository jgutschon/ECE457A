clear all;
close all;

%% Part c. & d.
population_size = 50;
num_generations = 150;
crossover_prob = 0.6;
mutation_prob = 0.25;

optimal_soln = gasolver([population_size; num_generations; crossover_prob; mutation_prob;])

%% Part e.
% Less generations
num_generations = 100;
optimal_soln = gasolver([population_size; num_generations; crossover_prob; mutation_prob;])

% More generations
num_generations = 200;
optimal_soln = gasolver([population_size; num_generations; crossover_prob; mutation_prob;])

%% Part f.
% Lower population
population_size = 25;
optimal_soln = gasolver([population_size; num_generations; crossover_prob; mutation_prob;])

% Higher population
popoulation_size = 75;
optimal_soln = gasolver([population_size; num_generations; crossover_prob; mutation_prob;])

%% Part g.
% Lower crossover probability
crossover_prob = 0.4;
optimal_soln = gasolver([population_size; num_generations; crossover_prob; mutation_prob;])

% Higher crossover probability
crossover_prob = 0.8;
optimal_soln = gasolver([population_size; num_generations; crossover_prob; mutation_prob;])

%% Part h.
% Lower mutation probability
mutation_prob = 0.15;
optimal_soln = gasolver([population_size; num_generations; crossover_prob; mutation_prob;])

% Higher mutation probability
mutation_prob = 0.35;
optimal_soln = gasolver([population_size; num_generations; crossover_prob; mutation_prob;])
