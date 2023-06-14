# visualize-algos

[![PyPI version](https://badge.fury.io/py/visualize-algos.svg)](https://badge.fury.io/py/visualize-algos)

A Python package for visualizing pathfinding algorithms on a graphical user interface (GUI).

## Installation

You can install the package using following command:

`pip install visualize-algos`

## Usage

Here's a simple example of how to use the package:

```python
import visualize_algos

# Create grid for creating a maze
# grid = 2D list containing 0's and 1's where 1 denotes obstacles and 0 denotes open space.
grid = [[]]

# Set destination coordinates
search = [x,y]

# Visualize the pathfinding process
dfs_algo = visualize_algos.PathFinding(grid=grid, algo="dfs",search=search)
dfs_algo.start_visualizing()
```

For more detailed example, please refer to the [example](https://github.com/Dhvanik-Viradiya/Path-finding-algorithm-visuallization/blob/main/visualize_algos/example/visualize_all_algos.py).

## Supported Algorithms

- dfs
- bfs
- A\*

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the [GitHub repository](https://github.com/Dhvanik-Viradiya/Path-finding-algorithm-visuallization/issues).
