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

    def isValid(self, y: int, x: int) -> bool:
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

    def print_maze(self) -> None:
        for row in self.maze:
            print(row)

    def print_explored(self) -> None:
        print(f"Explored: •  Maze Wall: █")
        for y in range(len(self.maze)):
            for x in range(len(self.maze)):
                if (y, x) in self.closed_queue:
                    print("•", end="")
                elif self.maze[y][x] == 1:
                    print("█", end="")
                else:
                    print(" ", end="")
            print()

    # Breadth First Search
    def bfs_search(self, start_pos: tuple, end_pos: tuple):
        # Reset queues
        self.open_queue = []
        self.closed_queue = []
        self.expanded = [[False for i in range(25)] for j in range(25)]

        # Add starting position to open_queue
        self.open_queue.append(start_pos)
        self.expanded[start_pos[0]][start_pos[1]] = True

        # Start searching
        curr = start_pos
        while len(self.open_queue) != 0:
            # print(self.open_queue)

            # Add node to closed queue
            curr = self.open_queue.pop(0)
            self.closed_queue.append(curr)

            # Check current node for goal
            if curr == end_pos:
                print(f"Found goal after exploring {len(self.closed_queue)} nodes.\n")
                print(f"Closed queue:\n{self.closed_queue}\n")
                return

            # Expand curr, add adjacent nodes to open_queue
            for i in range(len(x_dirs)):
                curr_y = curr[0]
                curr_x = curr[1]
                y = curr_y + y_dirs[i]
                x = curr_x + x_dirs[i]
                if self.isValid(y, x):
                    self.open_queue.append((y, x))
                    self.expanded[y][x] = True

        print(f"Goal not found after exloring {len(self.closed_queue)} nodes.\n")


if __name__ == "__main__":
    # c.1: Agent starts at S, ends at E1
    start_pos = (11, 2)
    end_pos = (19, 23)
    print(f"\n\nc.1 - start, S: {start_pos}, end, E1: {end_pos}\n")

    m = Maze()
    m.bfs_search(start_pos, end_pos)
    m.print_explored()

    # c.2: Agent starts at S, ends at E2
    start_pos = (11, 2)
    end_pos = (21, 2)
    print(f"\n\nc.2 - start, S: {start_pos}, end, E2: {end_pos}\n")

    m.bfs_search(start_pos, end_pos)
    m.print_explored()

    # c.3: Agent starts at (0,0), ends at (24,24)
    start_pos = (0, 0)
    end_pos = (24, 24)
    print(f"\n\nc.3 - start: {start_pos}, end: {end_pos}\n")

    m.bfs_search(start_pos, end_pos)
    m.print_explored()
