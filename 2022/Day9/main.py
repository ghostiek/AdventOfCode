import numpy as np
from copy import deepcopy

# Part 1
with open("data.txt", "r") as file:
    txt = file.readlines()

txt = [elem.replace("\n", "") for elem in txt]


def calculate_euclidean_distance_squared(position1, position2):
    return (position1[0] - position2[0])**2 + (position1[1]-position2[1])**2


def get_diagonal_position(head_position, direction):
    final_position = None
    if direction == "R":
        final_position = [head_position[0] - 1, head_position[1]]
    elif direction == "L":
        final_position = [head_position[0] + 1, head_position[1]]
    elif direction == "U":
        final_position = [head_position[0], head_position[1] - 1]
    elif direction == "D":
        final_position = [head_position[0], head_position[1] + 1]
    return final_position


head_position = [0, 0]
tail_position = [0, 0]

tail_position_logged = [[0, 0]]
for instruction in txt:
    direction, magnitude = instruction.split(" ")
    for iteration in range(int(magnitude)):
        idx = None
        change = None
        if direction == "R":
            change = 1
            idx = 0
        elif direction == "L":
            change = -1
            idx = 0
        elif direction == "U":
            change = 1
            idx = 1
        elif direction == "D":
            change = -1
            idx = 1
        # Update head
        head_position[idx] = head_position[idx] + change
        # Logic to movement of T
        distance = calculate_euclidean_distance_squared(head_position, tail_position)
        if distance == 4:
            tail_position[idx] = tail_position[idx] + change
        elif distance == 5:
            if direction == "R":
                tail_position = [head_position[0]-1, head_position[1]]
            elif direction == "L":
                tail_position = [head_position[0] + 1, head_position[1]]
            elif direction == "U":
                tail_position = [head_position[0], head_position[1] - 1]
            elif direction == "D":
                tail_position = [head_position[0], head_position[1] + 1]
        # logging of squares visited by tails
        if tail_position not in tail_position_logged:
            tmp = deepcopy(tail_position)
            tail_position_logged.append(tmp)

print(tail_position_logged)
print(len(tail_position_logged))


# Part 2
node_position = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
tail_position_logged = [[0, 0]]

for instruction in txt:
    direction, magnitude = instruction.split(" ")
    for iteration in range(int(magnitude)):
        idx = None
        change = None
        if direction == "R":
            change = 1
            idx = 0
        elif direction == "L":
            change = -1
            idx = 0
        elif direction == "U":
            change = 1
            idx = 1
        elif direction == "D":
            change = -1
            idx = 1

        # Update head
        tmp_first = deepcopy(node_position[0])
        node_position[0][idx] = node_position[0][idx] + change

        last_change = np.array(node_position[0]) - np.array(tmp_first)
        # Logic to movement of next node
        for node_idx in range(1, len(node_position)):
            tmp_node = deepcopy(node_position[node_idx])
            distance = calculate_euclidean_distance_squared(node_position[node_idx-1], node_position[node_idx])
            # Simple follow vertical or horizontal
            if distance == 4:
                if node_position[node_idx - 1][0] > node_position[node_idx][0]:
                    node_position[node_idx][0] = node_position[node_idx][0] + 1
                elif node_position[node_idx - 1][0] < node_position[node_idx][0]:
                    node_position[node_idx][0] = node_position[node_idx][0] - 1
                elif node_position[node_idx - 1][1] > node_position[node_idx][1]:
                    node_position[node_idx][1] = node_position[node_idx][1] + 1
                else:
                    node_position[node_idx][1] = node_position[node_idx][1] - 1
            elif distance >= 5:
                if node_idx == 1:
                    node_position[node_idx] = get_diagonal_position(node_position[node_idx-1], direction)
                else:
                    # Check position moved and do the same
                    if node_position[node_idx-1][0] > node_position[node_idx][0]:
                        node_position[node_idx][0] = node_position[node_idx][0] + 1
                    else:
                        node_position[node_idx][0] = node_position[node_idx][0] - 1
                    if node_position[node_idx-1][1] > node_position[node_idx][1]:
                        node_position[node_idx][1] = node_position[node_idx][1] + 1
                    else:
                        node_position[node_idx][1] = node_position[node_idx][1] - 1
        # logging of squares visited by tails
        if node_position[-1] not in tail_position_logged:
            tmp = deepcopy(node_position[-1])
            tail_position_logged.append(tmp)

print(tail_position_logged)
print(len(tail_position_logged))

