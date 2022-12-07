import helper
import numpy as np

with open("data.txt", "r") as file:
    txt = file.readlines()

txt = [elem.replace("\n", "") for elem in txt]

# instructions have a $, outputs don't
result = helper.get_dir_sizes(txt)
result_vals = np.array(list(result.values()))

part1 = result_vals[result_vals<100000].sum()
print(part1)

# Part 2
total_size = result[""]
unused_space = 70000000 - total_size
space_needed = 30000000 - unused_space

part2 = result_vals[result_vals>=space_needed].min()
print(part2)
