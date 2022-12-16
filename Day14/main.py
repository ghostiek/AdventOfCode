import numpy as np
from helper import *

# Part 1
with open("data.txt", "r") as file:
    txt = file.readlines()

txt = [elem.replace("\n", "") for elem in txt]

sand_coordinates = (500, 0)
board=[]
for path in txt:
    rock_coordinates = parse_line(path)
    rocks = create_rocks(rock_coordinates)
    for rock in rocks:
        board.append(rock)

x_min = min(board)
x_max = max(board)

y_max = max(board, key=lambda x:x[1])
"""
# Set up lower box
for idx in range(x_min[0], x_max[0] + 1):
    board.append((idx, 9))
"""

# order is sand down to left, then down to the right
finished = False
counter = 0
while not finished:
    counter+=1
    # Fall from sand coord
    tmp_coord = sand_coordinates
    moving = True
    while moving:
        if tmp_coord[0] < x_min[0] or tmp_coord[0] > x_max[0]:
            moving = False
            finished = True
        # Check below
        elif (tmp_coord[0], tmp_coord[1]+1) not in board:
            tmp_coord = (tmp_coord[0], tmp_coord[1]+1)
        # Check below left
        elif (tmp_coord[0] - 1, tmp_coord[1]+1) not in board:
            tmp_coord = (tmp_coord[0] - 1, tmp_coord[1] + 1)
        # Check below right
        elif (tmp_coord[0] + 1, tmp_coord[1] + 1) not in board:
            tmp_coord = (tmp_coord[0] + 1, tmp_coord[1] + 1)
        # Don't move
        else:
            board.append(tmp_coord)
            moving = False

print(counter-1)

# Part 2
with open("data.txt", "r") as file:
    txt = file.readlines()

txt = [elem.replace("\n", "") for elem in txt]

sand_coordinates = (500, 0)
board=[]
for path in txt:
    rock_coordinates = parse_line(path)
    rocks = create_rocks(rock_coordinates)
    for rock in rocks:
        board.append(rock)

x_min = min(board)
x_max = max(board)

y_max = max(board, key=lambda x:x[1])


# order is sand down to left, then down to the right
finished = False
counter = 0
while not finished:
    if sand_coordinates in board:
        finished = True
        moving = False
    counter+=1
    # Fall from sand coord
    tmp_coord = sand_coordinates
    moving = True
    while moving:
        if tmp_coord[1] == y_max[1] + 1:
            board.append(tmp_coord)
            moving = False
        # Check below
        elif (tmp_coord[0], tmp_coord[1]+1) not in board:
            tmp_coord = (tmp_coord[0], tmp_coord[1]+1)
        # Check below left
        elif (tmp_coord[0] - 1, tmp_coord[1]+1) not in board:
            tmp_coord = (tmp_coord[0] - 1, tmp_coord[1] + 1)
        # Check below right
        elif (tmp_coord[0] + 1, tmp_coord[1] + 1) not in board:
            tmp_coord = (tmp_coord[0] + 1, tmp_coord[1] + 1)
        # Don't move
        else:
            board.append(tmp_coord)
            moving = False

print(counter-1)