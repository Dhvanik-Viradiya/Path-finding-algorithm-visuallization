"""Gui based path finding alorithm traversal."""
import copy
import enum
import threading
import tkinter as tk

import path_finding_algos


class AlgoEnum(enum.Enum):
    """Name of path finding algorithms."""

    DFS = "dfs"
    BFS = "bfs"
    ASTAR = "astar"


class PathFinding:
    """Class to generate grid ui and search the path using given algorithm."""

    def __init__(
        self,
        grid,
        algo,
        bg_color="white",
        cell_size=25,
        obstacle_color="brown",
        search=[],
        window_number = 0
    ):
        self.grid = grid
        self.algo = algo
        self.canvas = tk.Tk()
        self.canvas.title(f"{len(grid)}x{len(grid[0])} grid with {algo} algorithm")
        self.window_number = window_number
        self.cells = {}
        self.bg_color = bg_color
        self.cell_size = cell_size
        self.obstacle_color = obstacle_color
        self.visited = [[None for j in range(len(grid[0]))] for i in range(len(grid))]

        self.search = search
        if not search:
            self.search = (len(grid) - 1, len(grid[0] - 1))
        if algo not in [data.value for data in AlgoEnum]:
            raise ValueError(f"{algo} algorithm is not implemented here.")

    def set_window_position(self):
        """Setting the GUI window position over screen."""
        padding = 50
        width = len(self.grid[0]) * self.cell_size + padding
        height = len(self.grid) * self.cell_size + padding

        row = self.window_number // 3
        col = self.window_number % 3

        print(self.window_number, height, width, row, col)
        self.canvas.geometry(f"+{width*col+padding}+{height*row+padding}")

    def generate_frames(self):
        """Generate cells to use in a grid of UI."""
        rows = len(self.grid)
        cols = len(self.grid[0])

        for row in range(rows):
            for column in range(cols):
                cell = tk.Frame(
                    self.canvas,
                    bg=self.bg_color,
                    highlightbackground="black",
                    highlightcolor="black",
                    highlightthickness=1,
                    width=self.cell_size,
                    height=self.cell_size,
                    padx=3,
                    pady=3,
                )
                cell.grid(row=row, column=column)
                self.cells[(row, column)] = cell

    def color_cell(self, i, j, color="blue"):
        """Coloring the cell with given color."""
        self.cells[(i, j)].configure(background=color)

    def initialize_destination(self):
        """Coloring the destination."""
        self.color_cell(self.search[0], self.search[1], "red")

    def color_obstacles(self):
        """Coloring the obstacles with given color."""
        for i, _ in enumerate(self.grid):
            for j in range(len(self.grid[0])):
                if self.grid[i][j]:
                    self.color_cell(i, j, self.obstacle_color)

    def start_visualizing(self):
        """Creating thread for traverse the algo and starting the main screen of gui."""
        self.set_window_position()
        self.generate_frames()
        self.color_obstacles()
        self.initialize_destination()
        t = threading.Thread(
            target=eval(f"path_finding_algos.{self.algo}"),
            args=(
                self.grid,
                0,
                0,
                copy.deepcopy(self.visited),
                self.search,
                self.cells,
                self.bg_color,
            ),
        )
        t.start()
        self.canvas.mainloop()
