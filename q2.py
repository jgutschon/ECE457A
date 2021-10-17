#!/usr/bin/python3

# Search directions
y_dirs = (1, 0, -1, 0)
x_dirs = (0, 1, 0, -1)


class Maze:
    maze = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    ]

    def __init__(self):
        # Array to track expanded nodes
        self.expanded = [[False for i in range(25)] for j in range(25)]

        # Track expanded nodes not yet explored
        self.open_queue = []

        # Track explored nodes
        self.closed_queue = []

        # Track parents to generate path
        self.parents = {}

    def __isValid(self, y: int, x: int) -> bool:
        # check bounds
        if y < 0 or x < 0 or y > len(self.expanded) - 1 or x > len(self.expanded) - 1:
            return False

        # check for wall
        if self.maze[y][x] == 1:
            return False

        # ignore repeated states
        if self.expanded[y][x]:
            return False

        return True

    # Print maze with explored nodes and solution path
    def __print_explored(self) -> None:
        print(f"Maze Wall: █\nExplored: •\nSolution Path: ○\n")
        start = self.closed_queue[0]
        end = self.closed_queue[-1]

        for y in range(len(self.maze)):
            for x in range(len(self.maze)):
                if (y, x) == start:
                    print("S", end="")
                elif (y, x) == end:
                    print("E", end="")
                elif (y, x) in self.__find_path(start, end):
                    print("○", end="")
                elif (y, x) in self.closed_queue:
                    print("•", end="")
                elif self.maze[y][x] == 1:
                    print("█", end="")
                else:
                    print(" ", end="")
            print()
        print("\n")

    # Backtrack through parent nodes for solution path
    def __find_path(self, start: tuple, end: tuple) -> list:
        path = [end]
        node = end
        while node != start:
            node = self.parents[node]
            path.insert(0, node)
        return path

    # Breadth First Search, Depth First Search
    def blind_search(self, method: str, start: tuple, end: tuple) -> None:
        # Reset queues
        self.open_queue = []
        self.closed_queue = []
        self.expanded = [[False for i in range(25)] for j in range(25)]
        self.parents = {}

        # Add starting position to open_queue, mark as expanded
        self.open_queue.append(start)
        self.expanded[start[0]][start[1]] = True

        # Start search
        while len(self.open_queue) != 0:
            # print(self.open_queue)

            if method == "bfs":
                curr = self.open_queue.pop(0)  # FIFO
            elif method == "dfs":
                curr = self.open_queue.pop()  # LIFO
            else:
                print("Invalid method")
                return

            # Add current node to closed queue
            self.closed_queue.append(curr)

            # Check current node for goal, print solution
            if curr == end:
                print(f"Found goal after exploring {len(self.closed_queue)} nodes.")
                print(f"Final path:\n{self.__find_path(start, end)}\n")
                self.__print_explored()
                return

            # Expand curr, add adjacent nodes to open_queue
            for i in range(len(x_dirs)):
                y = curr[0] + y_dirs[i]
                x = curr[1] + x_dirs[i]

                if self.__isValid(y, x):
                    # Record parents, mark as expanded
                    self.parents[(y, x)] = curr
                    self.expanded[y][x] = True

                    # Add to open_queue
                    self.open_queue.append((y, x))

        print(f"Goal not found after exloring {len(self.closed_queue)} nodes.\n")

    # Manhattan distance heuristic
    def __h(self, curr: tuple, end: tuple) -> int:
        dist = abs(curr[0] - end[0]) + abs(curr[1] - end[1])
        return dist

    def astar_search(self, start: tuple, goal: tuple) -> None:
        # Reset queues
        self.open_queue = {}
        self.closed_queue = []
        self.expanded = [[False for i in range(25)] for j in range(25)]
        self.parents = {}

        # Add starting position to open_queue, mark as expanded
        self.open_queue[start] = 0
        self.expanded[start[0]][start[1]] = True

        # Start search
        while len(self.open_queue) != 0:
            # print(self.open_queue)

            # Choose node with minimum f value
            curr = min(self.open_queue, key=self.open_queue.get)
            self.open_queue.pop(curr)

            # Add current node to closed queue
            self.closed_queue.append(curr)

            # Check current node for goal
            if curr == goal:
                print(f"Found goal after exploring {len(self.closed_queue)} nodes.")
                print(f"Final path:\n{self.__find_path(start, goal)}\n")
                self.__print_explored()
                return

            # Expand curr, examine adjacent nodes
            for i in range(len(x_dirs)):
                y = curr[0] + y_dirs[i]
                x = curr[1] + x_dirs[i]

                if self.__isValid(y, x):
                    # Record parents, mark as expanded
                    self.parents[(y, x)] = curr
                    self.expanded[y][x] = True

                    # Evaluation function: f = g + h
                    f = len(self.__find_path(start, (y, x))) + self.__h((y, x), goal)

                    # Add to open_queue with f value
                    self.open_queue[(y, x)] = f

        print(f"Goal not found after exloring {len(self.closed_queue)} nodes.\n")


if __name__ == "__main__":
    m = Maze()
    sep = "-" * 80

    coords = [
        {"start": (11, 2), "end": (19, 23)},
        {"start": (11, 2), "end": (21, 2)},
        {"start": (0, 0), "end": (24, 24)},
    ]

    for i in range(len(coords)):
        start = coords[i]["start"]
        end = coords[i]["end"]
        print(f"{sep}\nc.{i+1} - start: {start}, end: {end}\n{sep}")

        print("Breadth First Search:\n")
        m.blind_search("bfs", start, end)

        print("Depth First Search:\n")
        m.blind_search("dfs", start, end)

        print("A* Search\n")
        m.astar_search(start, end)
