import numpy as np


def get_trees_to_edge(tree_grid, coord):
    up = tree_grid[:coord[0], coord[1]]
    down = tree_grid[coord[0]+1:, coord[1]]
    left = tree_grid[coord[0], :coord[1]]
    right = tree_grid[coord[0], coord[1]+1:]
    return np.array(up).flatten(),\
           np.array(down).flatten(),\
           np.array(left).flatten(),\
           np.array(right).flatten()


def is_largest(trees, tree_size):
    return np.all(tree_size > trees)


def get_scenic_score(trees, tree_size):
    result = np.argwhere(trees >= tree_size).flatten()
    return len(trees) if len(result) == 0 else result[0] + 1

"""

tmp = [[1,2,3,4],[5,6,7,8], [9,10,11,12]]
tmp = np.array([3,4,5,8,1,5])
print(get_scenic_score(tmp, 7))"""