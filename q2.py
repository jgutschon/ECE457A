#!/usr/bin/python3

# Search directions
from typing import Pattern


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
        for y in range(len(self.maze)):
            for x in range(len(self.maze)):
                if (y, x) == self.closed_queue[0]:
                    print("S", end="")
                elif (y, x) == self.closed_queue[-1]:
                    print("E", end="")
                elif (y, x) in self.__find_path():
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
    def __find_path(self) -> list:
        start_pos = self.closed_queue[0]
        end_pos = self.closed_queue[-1]

        node = end_pos
        path = [node]
        while node != start_pos:
            node = self.parents[node]
            path.insert(0, node)
        return path

    # Breadth First Search, Depth First Search
    def search(self, method: str, start_pos: tuple, end_pos: tuple) -> None:
        # Reset queues
        self.open_queue = []
        self.closed_queue = []
        self.expanded = [[False for i in range(25)] for j in range(25)]
        self.parents = {}

        # Add starting position to open_queue, mark as expanded
        self.open_queue.append(start_pos)
        self.expanded[start_pos[0]][start_pos[1]] = True

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
            if curr == end_pos:
                print(f"Found goal after exploring {len(self.closed_queue)} nodes.")
                print(f"Final path:\n{self.__find_path()}\n")
                self.__print_explored()
                return

            # Expand curr, add adjacent nodes to open_queue
            for i in range(len(x_dirs)):
                y = curr[0] + y_dirs[i]
                x = curr[1] + x_dirs[i]
                if self.__isValid(y, x):
                    self.parents[(y, x)] = curr
                    self.open_queue.append((y, x))
                    self.expanded[y][x] = True

        print(f"Goal not found after exloring {len(self.closed_queue)} nodes.\n")

    # Manhattan distance heuristic
    def __hstar(self, curr_pos: tuple, end_pos: tuple) -> int:
        dist = abs(curr_pos[0] - end_pos[0]) + abs(curr_pos[1] - end_pos[1])
        return dist

    def astar_search(self, start_pos: tuple, end_pos: tuple) -> None:
        # Reset queues
        self.open_queue = []
        self.closed_queue = []
        self.expanded = [[False for i in range(25)] for j in range(25)]
        self.parents = {}

        # Add starting position to open_queue, mark as expanded
        self.open_queue.append(start_pos)
        self.expanded[start_pos[0]][start_pos[1]] = True

        # Start search
        while len(self.open_queue) != 0:
            # print(self.open_queue)

            # curr = self.open_queue.pop()  # LIFO
            # f = self.search("bfs", start_pos, end_pos)

            # Add current node to closed queue
            self.closed_queue.append(curr)

            # Check current node for goal
            if curr == end_pos:
                print(f"Found goal after exploring {len(self.closed_queue)} nodes.")
                print(f"Final path:\n{self.__find_path()}\n")
                self.__print_explored()
                return

            # Expand curr, add adjacent nodes to open_queue
            for i in range(len(x_dirs)):
                y = curr[0] + y_dirs[i]
                x = curr[1] + x_dirs[i]
                if self.__isValid(y, x):
                    self.parents[(y, x)] = curr
                    self.open_queue.append((y, x))
                    self.expanded[y][x] = True

        print(f"Goal not found after exloring {len(self.closed_queue)} nodes.\n")


if __name__ == "__main__":
    m = Maze()
    sep = "-" * 80

    # c.1: Agent starts at S, ends at E1
    start_pos = (11, 2)
    end_pos = (19, 23)
    print(f"{sep}\nc.1 - start: {start_pos}, end: {end_pos}\n{sep}")

    print("Breadth First Search:\n")
    m.search("bfs", start_pos, end_pos)

    print("Depth First Search:\n")
    m.search("dfs", start_pos, end_pos)

    # c.2: Agent starts at S, ends at E2
    start_pos = (11, 2)
    end_pos = (21, 2)
    print(f"{sep}\nc.2 - start: {start_pos}, end: {end_pos}\n{sep}")

    print("Breadth First Search:\n")
    m.search("bfs", start_pos, end_pos)

    print("Depth First Search:\n")
    m.search("dfs", start_pos, end_pos)

    # c.3: Agent starts at (0,0), ends at (24,24)
    start_pos = (0, 0)
    end_pos = (24, 24)
    print(f"{sep}\nc.3 - start: {start_pos}, end: {end_pos}\n{sep}")

    print("Breadth First Search:\n")
    m.search("bfs", start_pos, end_pos)

    print("Depth First Search:\n")
    m.search("dfs", start_pos, end_pos)
