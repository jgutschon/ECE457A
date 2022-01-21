function [cost] = fitness(x)

specs = perfFCN([x(1); x(2); x(3);]);
cost = sum(specs);

end
