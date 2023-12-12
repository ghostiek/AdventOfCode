# read data
# update universe
# recognize pairs
# calculate shortest distances
# sum them

from itertools import combinations


with open("data.txt", "r") as file:
    txt = file.read()


universe_map = txt.split("\n")


def find_idx(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def find_empty(universe):
    columns_to_expand = set(range(len(universe)))
    rows_to_expand = set(range(len(universe[0])))
    for idx_y in range(len(universe)):
        current_row = universe[idx_y]
        galaxy_idxs = find_idx(current_row, "#")
        columns_to_expand = columns_to_expand - set(galaxy_idxs)
        if len(galaxy_idxs) > 0:
            rows_to_expand = rows_to_expand - {idx_y}

    columns_to_expand = sorted(columns_to_expand)
    rows_to_expand = sorted(rows_to_expand)
    return rows_to_expand, columns_to_expand


def expand_universe(universe, expand_factor=2):
    rows_to_expand, columns_to_expand = find_empty(universe)
    expanded_universe = []
    for idx_y in range(len(universe)):
        current_row = universe[idx_y]
        pad = 0
        for col_to_insert in columns_to_expand:
            current_row = current_row[:col_to_insert+pad] + '.'*(expand_factor-1) + current_row[col_to_insert+pad:]
            pad += (expand_factor-1)
        expanded_universe.append(current_row)
    pad = 0
    row_to_append = "." * len(expanded_universe[0])
    for row_to_insert in rows_to_expand:
        for rep in range(expand_factor-1):
            pad += 1
            expanded_universe.insert(row_to_insert+pad, row_to_append)
    return expanded_universe


def get_galaxies(universe):
    galaxies = {}
    galaxy_count = 0
    for idx_y in range(len(universe)):
        for idx_x in range(len(universe[0])):
            if "#" == universe[idx_y][idx_x]:
                galaxies[galaxy_count] = (idx_y, idx_x)
                galaxy_count+=1
    return galaxies

def get_shortest_distance(pair, galaxy_coords):
    galaxy_a = galaxy_coords[pair[0]]
    galaxy_b = galaxy_coords[pair[1]]
    return abs(galaxy_a[0] - galaxy_b[0]) + abs(galaxy_a[1] - galaxy_b[1])


def get_shortest_distance_fixed(pair, galaxy_coords, expand_rows, expand_cols, expand_factor = 2):
    galaxy_a = galaxy_coords[pair[0]]
    galaxy_b = galaxy_coords[pair[1]]
    pad_r = 0
    pad_c = 0
    for i in expand_rows:
        if min(galaxy_a[0], galaxy_b[0]) <= i <= max(galaxy_a[0], galaxy_b[0]):
            pad_r += (expand_factor-1)
    for i in expand_cols:
        if min(galaxy_a[1], galaxy_b[1]) <= i <= max(galaxy_a[1], galaxy_b[1]):
            pad_c += (expand_factor-1)

    return abs(galaxy_a[0] - galaxy_b[0]) + pad_r + abs(galaxy_a[1] - galaxy_b[1]) + pad_c


# Part 1
expanded_universe = expand_universe(universe_map)
galaxies = get_galaxies(expanded_universe)
galaxy_pairs = list(combinations(galaxies.keys(), 2))
total = 0
for i in galaxy_pairs:
    total += get_shortest_distance(i, galaxies)

print(total)

# Part 2
galaxies = get_galaxies(universe_map)
galaxy_pairs = list(combinations(galaxies.keys(), 2))
total = 0
x = []
fix = []
r, c = find_empty(universe_map)

for i in galaxy_pairs:
    # Had to rewrite the function to make it efficient
    total += get_shortest_distance_fixed(i, galaxies, r, c, 1000000)

print(total)




