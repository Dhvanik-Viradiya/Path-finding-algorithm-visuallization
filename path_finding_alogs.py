import copy
import time
from queue import Queue

# maze = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 1, 1],
#     [0, 1, 0],
#     [0, 0, 0],
# ]


#              Down,  right,  up,      left
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


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
        if (
            r >= 0
            and r < len(maze)
            and c >= 0
            and c < len(maze[0])
            and not visited[r][c]
            and not maze[r][c]
        ):
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
        previous = (0, 0)
    while not que.empty():
        # print(que)
        time.sleep(0.1)
        a, b = que.get()

        for i, j in DIRECTIONS:
            r = a + i
            c = b + j
            if (
                r >= 0
                and r < len(maze)
                and c >= 0
                and c < len(maze[0])
                and not visited[r][c]
                and not maze[r][c]
            ):
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


# visited = [[None for j in range(len(maze[0]))] for i in range(len(maze))]
# print(visited)
# # visited[0][0] = True
# data = dfs(maze, 0, 0, copy.deepcopy(visited))
# print(data)
