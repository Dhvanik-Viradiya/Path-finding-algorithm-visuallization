import random
import threading
import ui_based_path_search

ROWS = 15
COLS = 13


def create_grid():
    """Creating grid."""
    grid = [[0 for j in range(COLS)] for i in range(ROWS)]
    grid[5][COLS - 1] = 1
    for i in range(40):
        r = random.randint(0, ROWS - 1)
        c = random.randint(0, COLS - 1)
        grid[r][c] = 1
    grid[0][0] = 0
    return grid

def run_dfs():
    dfs_algo = ui_based_path_search.PathFinding(grid=grid, algo="dfs", search=search)
    dfs_algo.start_visualizing()

def run_bfs():
    bfs_algo = ui_based_path_search.PathFinding(grid=grid, algo="bfs", search=search)
    bfs_algo.start_visualizing()

grid = create_grid()
search = (random.randint(0, ROWS - 1), random.randint(0, COLS - 1))
grid[search[0]][search[1]] = 0


threading.Thread(target=run_dfs).start()
threading.Thread(target=run_bfs).start()

