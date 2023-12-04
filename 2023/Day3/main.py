# Star 1
import re

with open("data.txt", "r") as file:
    txt = file.read()

board = txt.split("\n")

# Part 1

class Number:
    def __init__(self, number, row_start, index_start, index_end):
        self.number = int(number)
        self.row_start = int(row_start)
        self.index_start = int(index_start)
        self.index_end = int(index_end)
        self.surrounding_indexes = self.get_surrounding_indexes(board)
        self.part_number = self.is_part(board)
        self.gear_idxs = self.find_gears(board)

    def get_surrounding_indexes(self, board):
        #row above
        indexes = []
        for row in range(self.row_start-1, self.row_start+2):
            for idx in range(self.index_start-1, self.index_end+2):
                if (0 <= row < len(board)) and (0 <= idx < len(board[0])):
                    indexes.append((row, idx))
        return indexes

    def is_part(self, board):
        indexes = self.surrounding_indexes
        for item in indexes:
            board_item = board[item[0]][item[1]]
            if not board_item.isnumeric() and board_item != ".":
                return True
        return False

    def find_gears(self, board):
        indexes = self.surrounding_indexes
        gear_indexes = []
        for item in indexes:
            board_item = board[item[0]][item[1]]
            if board_item == "*":
                gear_indexes.append(item)
        return gear_indexes

all_part_numbers = []
part_numbers = 0
for idx in range(len(board)):
    row = board[idx]
    all_nums_match = list(re.finditer("\d+", row))
    for number_found in all_nums_match:
        num_span = number_found.span()
        num = Number(number_found.group(0), idx, num_span[0], num_span[1]-1)
        if num.part_number:
            all_part_numbers.append(num)
            part_numbers += num.number
print(part_numbers)

# Part 2

gear_counts = {}
for num in all_part_numbers:
    # get the gear idxs, loop through them and check if the others match it
    for idx in num.gear_idxs:
        gear_counts[idx] = gear_counts.get(idx, 0) + 1

gear_ratios = 0
for k, v in gear_counts.items():
    if v == 2:
        gear_ratio = []
        # mult both nums
        for num in all_part_numbers:
            if k in num.surrounding_indexes:
                gear_ratio.append(num.number)
                if len(gear_ratio)==2:
                    gear_ratios += gear_ratio[0]*gear_ratio[1]
                    #early exit
                    break

print(gear_ratios)
