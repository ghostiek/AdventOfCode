# Star 1
import re



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
    if start_item <= search_item < end_item:
        diff = search_item-start_item
        return dst_values[0] + diff
    return -1

def get_destination(seed, src, dst):
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

# Part 2
from multiprocessing.pool import Pool

def get_min_from_seeds(src, dst, seeds):
    min_number = float('inf')
    for seed in seeds:
        final_dest = get_destination(seed, src, dst)
        if final_dest < min_number:
            min_number = final_dest
    return min_number

def multi_run_wrapper(args):
   return get_min_from_seeds(*args)




if __name__ == '__main__':
    with open("data.txt", "r") as file:
        txt = file.read()

    almenac = txt.split("\n")

    # Part 1

    seeds = re.findall(r"(\d+)", almenac[0])
    seeds = list(map(int, seeds))
    dst, src = parse_almenac(almenac)
    all_dests = []
    for seed in seeds:
        final_dest = get_destination(seed, src, dst)
        all_dests.append(final_dest)

    print(min(all_dests))

    iteration = []
    for seed_idx in range(int(len(seeds) / 2)):
        seed_start = seeds[2 * seed_idx]
        num_seeds = seeds[2 * seed_idx + 1]
        iteration.append((src, dst, range(seed_start, seed_start+num_seeds)))

    with Pool() as pool:
        results = pool.map(multi_run_wrapper, iteration)
        print(min(results))