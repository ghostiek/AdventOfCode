# Star 1
import re

with open("data.txt", "r") as file:
    txt = file.read()

cards = txt.split("\n")

# Part 1

def sanitize_list(x: list[str]) -> list[int]:
    return [int(i) for i in x if i != '']

def score_line(winning_nums, nums):
    score = 0
    num_matches = 0
    for num in nums:
        if num in winning_nums:
            num_matches += 1
            if score == 0:
                score = 1
            else:
                score *= 2
    return score, num_matches

total_score = 0
all_matches = []
for card in cards:
    x = re.search(r"^Card\s*\d+: ([\d\s]+) \| ([\d\s]+)$", card)
    winning_numbers = x.groups()[0].split(" ")
    numbers = x.groups()[1].split(" ")

    winning_numbers = sanitize_list(winning_numbers)
    numbers = sanitize_list(numbers)
    game_score, num_matches = score_line(winning_numbers, numbers)
    all_matches.append(num_matches)
    total_score += game_score

print(total_score)

# Part 2

def get_scratch(scratch_dict, match_idx):
    current_match = all_matches[match_idx]
    scratch_dict[match_idx] = scratch_dict.get(match_idx, 0) + 1
    while match_idx < len(all_matches) - 1 and current_match > 0:
        scratch_dict = get_scratch(scratch_dict, match_idx+1)
        match_idx += 1
        current_match -= 1
    return scratch_dict


scratch_dict = {}
for match_idx in range(len(all_matches)):
    scratch_dict = get_scratch(scratch_dict, match_idx)

print(sum(scratch_dict.values()))
