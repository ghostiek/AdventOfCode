import helper
import numpy as np

# Part 1
with open("data.txt", "r") as file:
    txt = file.readlines()

txt = [elem.replace("\n", "") for elem in txt]
txt = [[elem for elem in line] for line in txt]

# all the edges are visible
h = len(txt)
w = len(txt[0])
edges = 2*h + 2*(w-2)

inside = 0
txt_matrix = np.matrix(txt)
for idx1 in range(1, w-1):
    for idx2 in range(1, h-1):
        size = txt[idx1][idx2]
        # Get trees from each direction
        up, down, left, right = helper.get_trees_to_edge(txt_matrix, (idx1, idx2))
        states = [helper.is_largest(up, size),
                  helper.is_largest(down, size),
                  helper.is_largest(left, size),
                  helper.is_largest(right, size)]
        if np.any(states):
            inside+=1

print(edges+inside)

max_score = 0
# Part 2

for idx1 in range(1, w-1):
    for idx2 in range(1, h-1):
        size = txt[idx1][idx2]
        # Get trees from each direction
        up, down, left, right = helper.get_trees_to_edge(txt_matrix, (idx1, idx2))
        up = np.flip(up)
        left = np.flip(left)
        scores = [helper.get_scenic_score(up, size),
                  helper.get_scenic_score(down, size),
                  helper.get_scenic_score(left, size),
                  helper.get_scenic_score(right, size)]
        result = 1
        for i in scores:
            result = result*i
        if max_score < result:
            max_score = result

print(max_score)