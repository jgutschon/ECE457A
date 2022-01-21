import operator
import numpy
from deap import algorithms, base, creator, tools, gp


class MultiplexerGA:
    def __init__(self):
        self.num_a_terminals = 2
        self.num_d_terminals = 2 ** self.num_a_terminals
        self.num_terminals = self.num_a_terminals + self.num_d_terminals
        self.fitness_cases = 2 ** self.num_terminals

        # input: [a0, a1, d0, d1, d2, d3]
        self.inputs = [[0] * self.num_terminals for i in range(self.fitness_cases)]
        self.outputs = [None] * (self.fitness_cases)

        self.toolbox = base.Toolbox()

    def if_function(self, condition_x, out_y, out_z):
        return out_y if condition_x else out_z

    def setup(self):
        for i in range(self.fitness_cases):
            val = i
            cases = self.fitness_cases

            # Fill in the input bits
            for j in range(self.num_terminals):
                cases /= 2
                if val >= cases:
                    self.inputs[i][j] = 1
                    val -= cases

            # Find the corresponding output
            index_output = self.num_a_terminals
            for j, k in enumerate(self.inputs[i][: self.num_a_terminals]):
                index_output += k * 2 ** j
            self.outputs[i] = self.inputs[i][index_output]

        # Add primitives to primitive set
        prim_set = gp.PrimitiveSet("main", self.num_terminals, "term")
        prim_set.addPrimitive(operator.and_, 2)
        prim_set.addPrimitive(operator.or_, 2)
        prim_set.addPrimitive(operator.not_, 1)
        prim_set.addPrimitive(self.if_function, 3)

        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax)

        self.toolbox.register("expr", gp.genFull, pset=prim_set, min_=2, max_=4)
        self.toolbox.register(
            "individual", tools.initIterate, creator.Individual, self.toolbox.expr
        )
        self.toolbox.register(
            "population", tools.initRepeat, list, self.toolbox.individual
        )
        self.toolbox.register("compile", gp.compile, pset=prim_set)
        self.toolbox.register("evaluate", self.fitness)
        self.toolbox.register("select", tools.selTournament, tournsize=7)
        self.toolbox.register("mate", gp.cxOnePoint)
        self.toolbox.register("expr_mut", gp.genGrow, min_=0, max_=2)
        self.toolbox.register(
            "mutate", gp.mutUniform, expr=self.toolbox.expr_mut, pset=prim_set
        )

    def fitness(self, individual):
        func = self.toolbox.compile(expr=individual)
        fit = (sum(func(*in_) == out for in_, out in zip(self.inputs, self.outputs)),)
        return fit

    def run_ga(self):
        self.setup()

        stats = tools.Statistics(lambda ind: ind.fitness.values)
        stats.register("avg", numpy.mean)
        stats.register("std", numpy.std)
        stats.register("min", numpy.min)
        stats.register("max", numpy.max)

        population = self.toolbox.population(n=20)
        hall_of_fame = tools.HallOfFame(1)

        # use evolutionary algorithm to get optimized population
        algorithms.eaSimple(
            population, self.toolbox, 0.8, 0.1, 20, stats, halloffame=hall_of_fame
        )

        return population, stats, hall_of_fame


if __name__ == "__main__":
    multiplexer_ga = MultiplexerGA()
    [population, stats, hall_of_fame] = multiplexer_ga.run_ga()

    finalist = hall_of_fame.items[0]
    print(f"\nFinalist:\n{finalist}")

    nodes, edges, labels = gp.graph(finalist)

    ### Graphviz Section ###
    import pygraphviz as pgv

    g = pgv.AGraph()
    g.add_nodes_from(nodes)
    g.add_edges_from(edges)
    g.layout(prog="dot")

    for i in nodes:
        n = g.get_node(i)
        n.attr["label"] = labels[i]

    g.draw("tree.pdf")
