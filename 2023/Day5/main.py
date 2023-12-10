# Star 1
import re


with open("data.txt", "r") as file:
    txt = file.read()

almenac = txt.split("\n")

# Part 1

seeds = re.findall(r"(\d+)", almenac[0])
seeds = list(map(int, seeds))

def parse_almenac(almenac):
    destinations = [[] for x in range(7)]
    sources = [[] for x in range(7)]
    category = 0
    for idx in range(2, len(almenac)):
        nums = re.findall(r"(\d+)", almenac[idx])
        if len(nums) == 0:
            category += 0.5
            continue
        category = int(category)
        destination_num = int(nums[0])
        source_num = int(nums[1])
        range_num = int(nums[2])
        destination_range = [destination_num, destination_num + range_num]
        source_range = [source_num, source_num + range_num]
        destinations[category].append(destination_range)
        sources[category].append(source_range)
    return destinations, sources


def get_value_in_bound(x: list[int], search_item: int, dst_values: list[int]) -> int:
    start_item = x[0]
    end_item = x[1]
    if start_item <= search_item <= end_item:
        diff = search_item-start_item
        return dst_values[0] + diff
    return -1

def get_destination(seed):
    current_seed = int(seed)
    for idx in range(len(dst)):
        current_category_src = src[idx]
        current_category_dst = dst[idx]
        current_seed = get_category_destination(current_seed, current_category_src, current_category_dst)
    return current_seed

def get_category_destination(seed, category_str, category_dst):
    current_seed = int(seed)
    for idx in range(len(category_str)):
        current_range = category_str[idx]
        new_value = get_value_in_bound(current_range, current_seed, category_dst[idx])
        if new_value != -1:
            return new_value
    return current_seed

dst, src = parse_almenac(almenac)
all_dests = []
for seed in seeds:
    final_dest = get_destination(seed)
    all_dests.append(final_dest)

print(min(all_dests))

# Part 2
best_solution = float('inf')
for seed_idx in range(int(len(seeds)/2)):
    seed_start = seeds[2*seed_idx]
    num_seeds = seeds[2*seed_idx+1]
    while num_seeds > 0:
        seed_start += 1
        num_seeds -= 1
        final_dest = get_destination(seed_start)
        if final_dest < best_solution:
            best_solution = final_dest
    print("Pair Done!")

print(best_solution)