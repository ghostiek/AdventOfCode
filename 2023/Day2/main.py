# Star 1
import re
from re import Match
from typing import Optional

with open("data.txt", "r") as file:
    txt = file.read()


def tuple_to_dict(cubes: Optional[Match[str]]) -> dict:
    track = {"red": 0, "green": 0, "blue": 0}
    current_num = 0
    for cube in cubes.groups():
        # False on None
        if cube:
            if cube.isnumeric():
                current_num = int(cube)
            else:
                track[cube] = current_num
    return track


def is_possible_set(current_set: str) -> bool:
    max_cubes = {"red": 12, "green": 13, "blue": 14}
    cubes = re.search(
        r"(?:Game \d+:)? (\d+) (blue|red|green)(?:, )?(\d+)? ?(blue|red|green)?(?:, )?(\d+)? ?(blue|red|green)?",
        current_set)
    tracked_set = tuple_to_dict(cubes)

    for k in tracked_set.keys():
        if tracked_set[k] > max_cubes[k]:
            return False
    return True


def is_possible_game(sets: list[str]) -> bool:
    for current_set in sets:
        if not is_possible_set(current_set):
            return False
    return True


total = 0
games = txt.split("\n")
for game in games:
    game_id = int(re.search(r"^Game (\d+): ", game).groups()[0])
    sets = game.split(";")
    total += game_id if is_possible_game(sets) else 0

print(total)


# Part 2

def get_dict_from_set(current_set: str) -> dict:
    cubes = re.search(
        r"(?:Game \d+:)? (\d+) (blue|red|green)(?:, )?(\d+)? ?(blue|red|green)?(?:, )?(\d+)? ?(blue|red|green)?",
        current_set)
    tracked_set = tuple_to_dict(cubes)
    return tracked_set


def get_max_per_game(sets: list[str]):
    # we keep 1 instead of 0 because we're gonna need to multiply those later and we don't want it to be 0 when a ball
    # is missing
    track = {"red": 1, "green": 1, "blue": 1}
    for current_set in sets:
        current_set_values = get_dict_from_set(current_set)
        for color in track.keys():
            if current_set_values[color] > track[color]:
                track[color] = current_set_values[color]
    return track


def get_power(max_colors: dict) -> int:
    total = 1
    for val in max_colors.values():
        total *= val
    return total


total_power = 0
games = txt.split("\n")
for game in games:
    sets = game.split(";")
    # Get max num of occurrence per color
    max_colors = get_max_per_game(sets)
    total_power += get_power(max_colors)

print(total_power)
