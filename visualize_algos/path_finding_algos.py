import math
import time
from queue import Queue

#              Down,  right,  up,      left
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_valid_cell(row, col, max_row, max_col, maze, visited=[]):
    """Check whether the arrived cell is valid cell to move ahead or not."""
    if row >= 0 and row < max_row and col >= 0 and col < max_col and not maze[row][col]:
        if visited and visited[row][col]:
            return False
        return True
    return False


def dfs(maze, row, col, visited, search, cells=None, bg_color=None):
    """DFS algorithm to search the path to reach at the destination."""
    time.sleep(0.1)
    if row == search[0] and col == search[1]:
        visited[row][col] = True
        if cells:
            cells[(row, col)].configure(background="red")
        return visited

    visited[row][col] = True
    if cells and bg_color:
        cells[(row, col)].configure(background="blue")

    for i, j in DIRECTIONS:
        r = row + i
        c = col + j
        if is_valid_cell(r, c, len(maze), len(maze[0]), maze, visited):
            if cells and bg_color:
                cells[(r, c)].configure(background="blue")
            data = dfs(maze, r, c, visited, search, cells=cells, bg_color=bg_color)
            if data:
                return data
            else:
                if cells and bg_color:
                    cells[(r, c)].configure(background=bg_color)
    if cells and bg_color:
        cells[(row, col)].configure(background=bg_color)
    return None


def bfs(maze, row, col, visited, search, cells=None, bg_color=None):
    """BFS algorithm to search the path to reach at the destination."""
    que = Queue()
    que.put((row, col))
    visited[row][col] = True
    if (row, col) == search:
        if cells:
            cells[(row, col)].configure(background="red")
        return
    if cells:
        cells[(row, col)].configure(background="orange")
        previous = (row, col)
    while not que.empty():
        time.sleep(0.1)
        a, b = que.get()

        for i, j in DIRECTIONS:
            r = a + i
            c = b + j
            if is_valid_cell(r, c, len(maze), len(maze[0]), maze, visited):
                visited[r][c] = True
                if cells:
                    cells[previous].configure(background="blue")
                    cells[(r, c)].configure(background="orange")
                    previous = (r, c)
                if (r, c) == search:
                    if cells:
                        cells[previous].configure(background="blue")
                        cells[(r, c)].configure(background="red")
                    return
                que.put((r, c))


class Node:
    """A node class for A* algorithm"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0.0
        self.f = 0.0

    def __eq__(self, other):
        return self.position == other.position


def min_f_value(node_list):
    """Find the least f value node."""
    min_node = node_list[0]
    min_ind = 0
    for index, node in enumerate(node_list):
        if min_node.f > node.f:
            min_node = node
            min_ind = index
    return min_ind, min_node


def astar(maze, row, col, visited, search, cells=None, bg_color=None):
    """A* algorithm to search the path to reach at the destination."""

    # Create start and end node
    start_node = Node(None, (row, col))
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, search)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)
    if (row, col) == search:
        if cells:
            cells[(row, col)].configure(background="red")
        return
    if cells:
        cells[(row, col)].configure(background="orange")
        previous = (row, col)

    # Loop until you find the end
    while len(open_list) > 0:
        time.sleep(0.1)
        # Get the current node
        current_ind, current_node = min_f_value(open_list)

        # Pop current off open list, add to closed list
        open_list.pop(current_ind)

        for i, j in DIRECTIONS:
            r = current_node.position[0] + i
            c = current_node.position[1] + j
            if not is_valid_cell(r, c, len(maze), len(maze[0]), maze):
                continue

            new_node = Node(current_node, (r, c))
            if new_node == end_node:
                if cells:
                    cells[previous].configure(background="blue")
                    cells[(r, c)].configure(background="red")
                return

            new_node.g = current_node.g + 1

            x_position = r - end_node.position[0]
            y_position = c - end_node.position[1]
            new_node.h = math.sqrt(x_position**2 + y_position**2)

            new_node.f = new_node.g + new_node.h

            skip = False
            for ind, node in enumerate(open_list):
                if new_node == node:
                    if new_node.f >= node.f:
                        skip = True
                    else:
                        open_list.pop(ind)
                    break

            if skip:
                continue

            for node in closed_list:
                if new_node == node and new_node.f > node.f:
                    skip = True
                    break
            if skip:
                continue
            open_list.append(new_node)
            if cells:
                cells[previous].configure(background="blue")
                cells[(r, c)].configure(background="orange")
                previous = (r, c)
        closed_list.append(current_node)
