import numpy as np
import random


class TabuSearch:
    def __init__(self):
        # Stopping criterion, sets maximum allowed iterations of TS
        self.iterations = 200
        self.solution_len = 20
        self.choose = 2
        self.permutation = int(
            np.math.factorial(self.solution_len)
            / (
                np.math.factorial(self.choose)
                * np.math.factorial(self.solution_len - self.choose)
            )
        )

        self.distance = [
            [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7],
            [1, 0, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 4, 5, 6],
            [2, 1, 0, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 4, 5],
            [3, 2, 1, 0, 1, 4, 3, 2, 1, 2, 5, 4, 3, 2, 3, 6, 5, 4, 3, 4],
            [4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3],
            [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6],
            [2, 1, 2, 3, 4, 1, 0, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5],
            [3, 2, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4],
            [4, 3, 2, 1, 2, 3, 2, 1, 0, 1, 4, 3, 2, 1, 2, 5, 4, 3, 2, 3],
            [5, 4, 3, 2, 1, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2],
            [2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 1, 2, 3, 4, 5],
            [3, 2, 3, 4, 5, 2, 1, 2, 3, 4, 1, 0, 1, 2, 3, 2, 1, 2, 3, 4],
            [4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 2, 3],
            [5, 4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 0, 1, 4, 3, 2, 1, 2],
            [6, 5, 4, 3, 2, 5, 4, 3, 2, 1, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1],
            [3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4],
            [4, 3, 4, 5, 6, 3, 2, 3, 4, 5, 2, 1, 2, 3, 4, 1, 0, 1, 2, 3],
            [5, 4, 3, 4, 5, 4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 0, 1, 2],
            [6, 5, 4, 3, 4, 5, 4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 0, 1],
            [7, 6, 5, 4, 3, 6, 5, 4, 3, 2, 5, 4, 3, 2, 1, 4, 3, 2, 1, 0],
        ]

        self.flow = [
            [0, 0, 5, 0, 5, 2, 10, 3, 1, 5, 5, 5, 0, 0, 5, 4, 4, 0, 0, 1],
            [0, 0, 3, 10, 5, 1, 5, 1, 2, 4, 2, 5, 0, 10, 10, 3, 0, 5, 10, 5],
            [5, 3, 0, 2, 0, 5, 2, 4, 4, 5, 0, 0, 0, 5, 1, 0, 0, 5, 0, 0],
            [0, 10, 2, 0, 1, 0, 5, 2, 1, 0, 10, 2, 2, 0, 2, 1, 5, 2, 5, 5],
            [5, 5, 0, 1, 0, 5, 6, 5, 2, 5, 2, 0, 5, 1, 1, 1, 5, 2, 5, 1],
            [2, 1, 5, 0, 5, 0, 5, 2, 1, 6, 0, 0, 10, 0, 2, 0, 1, 0, 1, 5],
            [10, 5, 2, 5, 6, 5, 0, 0, 0, 0, 5, 10, 2, 2, 5, 1, 2, 1, 0, 10],
            [3, 1, 4, 2, 5, 2, 0, 0, 1, 1, 10, 10, 2, 0, 10, 2, 5, 2, 2, 10],
            [1, 2, 4, 1, 2, 1, 0, 1, 0, 2, 0, 3, 5, 5, 0, 5, 0, 0, 0, 2],
            [5, 4, 5, 0, 5, 6, 0, 1, 2, 0, 5, 5, 0, 5, 1, 0, 0, 5, 5, 2],
            [5, 2, 0, 10, 2, 0, 5, 10, 0, 5, 0, 5, 2, 5, 1, 10, 0, 2, 2, 5],
            [5, 5, 0, 2, 0, 0, 10, 10, 3, 5, 5, 0, 2, 10, 5, 0, 1, 1, 2, 5],
            [0, 0, 0, 2, 5, 10, 2, 2, 5, 0, 2, 2, 0, 2, 2, 1, 0, 0, 0, 5],
            [0, 10, 5, 0, 1, 0, 2, 0, 5, 5, 5, 10, 2, 0, 5, 5, 1, 5, 5, 0],
            [5, 10, 1, 2, 1, 2, 5, 10, 0, 1, 1, 5, 2, 5, 0, 3, 0, 5, 10, 10],
            [4, 3, 0, 1, 1, 0, 1, 2, 5, 0, 10, 0, 1, 5, 3, 0, 0, 0, 2, 0],
            [4, 0, 0, 5, 5, 1, 2, 5, 0, 0, 0, 1, 0, 1, 0, 0, 0, 5, 2, 0],
            [0, 5, 5, 2, 2, 0, 1, 2, 0, 5, 2, 1, 0, 5, 5, 0, 5, 0, 1, 1],
            [0, 10, 0, 5, 5, 1, 0, 2, 0, 5, 2, 2, 0, 5, 10, 2, 2, 1, 0, 6],
            [1, 5, 0, 5, 1, 5, 10, 10, 2, 2, 5, 5, 5, 0, 10, 0, 0, 1, 6, 0],
        ]

    # Returns the cost of the given solution (distance * flow)
    def get_cost(self, solution) -> int:
        cost = 0
        for i in range(self.solution_len):
            for j in range(self.solution_len):
                cost += self.distance[i][j] * self.flow[solution[i]][solution[j]]
        return cost

    # Gets all possible combinations of swaps, saves in neighbors array
    def update_neighbors(self, curr_solution, neighbors, neighborhood_size) -> list:
        index = -1
        for i in range(self.solution_len):
            for j in range(self.solution_len):
                if i < j:
                    index += 1
                    if index >= neighborhood_size:
                        break

                    # Get current swap for index
                    curr_solution[j], curr_solution[i] = (
                        curr_solution[i],
                        curr_solution[j],
                    )

                    # Save swapped solution to neighbors list
                    neighbors[index, :-2] = curr_solution
                    neighbors[index, -2:] = [curr_solution[i], curr_solution[j]]

                    # Restore curr_solution for next swap
                    curr_solution[i], curr_solution[j] = (
                        curr_solution[j],
                        curr_solution[i],
                    )

        # Evaluate the cost of the candidate neighbors
        cost = np.zeros(len(neighbors))
        for i in range(len(neighbors)):
            cost[i] = self.get_cost(neighbors[i, :-2])

        # Sorted neighbors by cost
        rank = np.argsort(cost)
        neighbors = neighbors[rank]

        return neighbors

    # Returns True if the given pair is in the Tabu list
    def check_tabu(self, pair, tabu_list) -> bool:
        is_tabu = True
        if not pair.tolist() in tabu_list:
            pair[0], pair[1] = pair[1], pair[0]
            if not pair.tolist() in tabu_list:
                is_tabu = False

        return is_tabu

    # Tabu Search method
    def search(
        self,
        aspiration=False,
        tabu_size=15,
        rand_tabu_size=False,
        frequency_tabu=False,
        neighborhood_size=0,
    ) -> None:

        # Set default neighborhood size to number of permutations
        if neighborhood_size == 0 or neighborhood_size > self.permutation:
            neighborhood_size = self.permutation

        # Initialize tabu list and frequency list to empty
        tabu_list = []
        frequency = {}

        # Choose random starting solution
        curr_solution = random.sample(range(self.solution_len), self.solution_len)
        best_solution = curr_solution

        # Initialize neighbors array to zero
        neighbors = np.zeros(
            (neighborhood_size, self.solution_len + self.choose), dtype=int
        )

        print(
            f"Initial Solution:\t{curr_solution}\nCost:\t{self.get_cost(curr_solution)}\n"
        )

        # Search until stopping criterion met
        while self.iterations > 0:
            # Update neighboring solutions sorted by cost
            neighbors = self.update_neighbors(
                curr_solution, neighbors, neighborhood_size
            )

            # Randomly change tabu list size
            if rand_tabu_size:
                tabu_size = random.randint(5, 25)

            # Check neighbors in order of cost
            neighbor_i = 0
            found_best_pair = False
            while neighbor_i < neighborhood_size and not found_best_pair:
                curr_solution = neighbors[neighbor_i, :-2].tolist()
                curr_pair = neighbors[neighbor_i, -2:].tolist()
                curr_cost = self.get_cost(curr_solution)
                best_cost = self.get_cost(best_solution)

                is_tabu = self.check_tabu(neighbors[neighbor_i, -2:], tabu_list)
                if not is_tabu:
                    # Add to recency based Tabu list
                    tabu_list.append(curr_pair)

                    found_best_pair = True

                # Aspiration criteria
                elif aspiration and (curr_cost < best_cost):
                    tabu_pair = curr_pair
                    if not tabu_pair in tabu_list:
                        tabu_pair = [tabu_pair[1], tabu_pair[0]]
                    tabu_list.insert(-1, tabu_list.pop(tabu_list.index(tabu_pair)))

                    found_best_pair = True

                # Keep Tabu list same size by removing oldest pair
                if len(tabu_list) > tabu_size:
                    tabu_list = tabu_list[1:]

                # Update frequency based Tabu list
                if frequency_tabu:
                    if not tuple(curr_solution) in frequency.keys():
                        frequency[tuple(curr_solution)] = 1
                    else:
                        # Penalize solution cost by freqeuency value
                        curr_cost += frequency[tuple(curr_solution)]

                        # Increment frequency for the current visit
                        frequency[tuple(curr_solution)] += 1

                # Check solution against best so far, update if better
                if curr_cost < best_cost:
                    best_solution = curr_solution

                neighbor_i += 1

            self.iterations -= 1
        print(f"Best Solution:\t\t{best_solution}\nCost:\t{best_cost}\n\n")


if __name__ == "__main__":
    # 1. Choose 10 different starting points
    print("Recency based TS")
    for _ in range(10):
        ts = TabuSearch()
        ts.search()

    # 2. Different tabu list sizes (default 15)
    print("Tabu list size: 10")
    ts = TabuSearch()
    ts.search(tabu_size=10)

    print("Tabu list size: 20")
    ts = TabuSearch()
    ts.search(tabu_size=20)

    # 3. Random tabu list size
    print("Randomized tabu list size")
    ts = TabuSearch()
    ts.search(rand_tabu_size=True)

    # 4. Aspiration criteria
    # Best so far
    print("TS with aspiration")
    ts = TabuSearch()
    ts.search(aspiration=True)

    # Best in neighborhood
    ts = TabuSearch()
    ts.search(aspiration=True)

    # 5. Less than whole neighborhood
    print("TS with neighborhood size: 80")
    ts = TabuSearch()
    ts.search(neighborhood_size=80)

    # 6. Frequency based tabu
    print("Frequency based TS")
    ts = TabuSearch()
    ts.search(frequency_tabu=True)
