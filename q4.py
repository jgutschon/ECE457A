from urllib.request import HTTPDigestAuthHandler
from PIL.Image import init
import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt
import matplotlib as mpl

# to compare
from scipy import optimize
from scipy.optimize._trustregion_constr.canonical_constraint import (
    initial_constraints_as_canonical,
)
from scipy.sparse.construct import rand

import seaborn as sns

sns.set(
    context="talk", style="darkgrid", palette="hls", font="sans-serif", font_scale=1.05
)

# Figure size in inches
FIGSIZE = (19, 8)
mpl.rcParams["figure.figsize"] = FIGSIZE

# Bounds
interval = (-100, 100)

# function to minimize
def easom(x1, x2):
    return (
        -1
        * np.cos(x1)
        * np.cos(x2)
        * np.exp(-1 * (x1 - np.pi) ** 2 - (x2 - np.pi) ** 2)
    )


# Temperature Scheduling
def temp_schedule(t, alpha, rule):
    if rule == "lin":
        t -= alpha
    elif rule == "exp":
        t *= alpha
    elif rule == "slow":
        t /= 1 + alpha
    else:
        print("Invalid rule")

    return t


def acceptance_probability(cost, new_cost, temperature):
    if new_cost < cost:
        # print("    - Acceptance probabilty = 1 as new_cost = {} < cost = {}...".format(new_cost, cost))
        return 1
    else:
        p = np.exp(-(new_cost - cost) / temperature)
        # print("    - Acceptance probabilty = {:.3g}...".format(p))
        return p


# b.i. Generate 10 initial points
def rand_point():
    rand_points = [[-101 for i in range(2)] for i in range(10)]
    best_point = [-100, -100]
    for i in range(10):
        rand_points[i][0] = np.random.uniform(low=interval[0], high=interval[1], size=1)
        rand_points[i][1] = np.random.uniform(low=interval[0], high=interval[1], size=1)

        print(rand_points[i])
        if easom(rand_points[i]) < easom(best_point):
            best_point = rand_points[i]

    return best_point


# b.ii. Generate 10 initial temperatures
def rand_temp():
    rand_temps = np.random.uniform(low=0, high=10, size=10)
    best_temp = max(rand_temps)
    return best_temp


# Annealing implementation
def annealing(
    start_point: tuple,
    alpha: float,
    init_temp,
    sched_rule,
    maxsteps=1000,
    debug=True,
):
    state = start_point
    cost = easom(state)
    states, costs = [state], [cost]
    temp = init_temp

    for step in range(maxsteps):
        temp = temp_schedule(temp, alpha, sched_rule)
        new_state = state
        new_cost = easom(new_state)

        if debug:
            print(
                "Step #{:>2}/{:>2} : T = {:>4.3g}, state = {:>4.3g}, cost = {:>4.3g}, new_state = {:>4.3g}, new_cost = {:>4.3g} ...".format(
                    step, maxsteps, temp, state, cost, new_state, new_cost
                )
            )

        if acceptance_probability(cost, new_cost, temp) > np.random.uniform():
            state, cost = new_state, new_cost
            states.append(state)
            costs.append(cost)
            # print("  ==> Accept it!")
        # else:
        #    print("  ==> Reject it...")
    return state, easom(state), states, costs


annealing(rand_point(), 0.1, rand_temp(), "lin", 1000)
