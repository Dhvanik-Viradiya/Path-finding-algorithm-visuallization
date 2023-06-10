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


def run_dfs(window_number):
    """Run dfs algorithm in GUI."""
    dfs_algo = ui_based_path_search.PathFinding(grid=grid, algo="dfs", search=search, window_number=window_number)
    dfs_algo.start_visualizing()


def run_bfs(window_number):
    """Run bfs algorithm in GUI."""
    bfs_algo = ui_based_path_search.PathFinding(grid=grid, algo="bfs", search=search, window_number=window_number)
    bfs_algo.start_visualizing()

def run_astar(window_number):
    """Run astar algorithm in GUI."""
    astar_algo = ui_based_path_search.PathFinding(grid=grid, algo="astar", search=search, window_number=window_number)
    astar_algo.start_visualizing()


grid = create_grid()
search = (random.randint(0, ROWS - 1), random.randint(0, COLS - 1))
grid[search[0]][search[1]] = 0


t1 = threading.Thread(target=run_dfs, args=(0,))
t2 = threading.Thread(target=run_bfs, args=(1,))
t3 = threading.Thread(target=run_astar, args=(2,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
