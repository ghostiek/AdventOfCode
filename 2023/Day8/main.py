import re
from math import lcm
# Part 1
with open("data.txt", "r") as file:
    txt = file.read()

info = txt.split("\n")

instructions = info[0]

network = info[2:]

network_dict = {}
for i in network:
    #elems = re.search(r"^([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)$", i).groups()
    elems = re.search(r"^([A-Z1-9]+) = \(([A-Z1-9]+), ([A-Z1-9]+)\)$", i).groups()
    network_dict[elems[0]] = elems[1:]

current_element = "AAA"
counter = 0
instruction_idx = -1
while current_element != "ZZZ":
    counter += 1
    instruction_idx = instruction_idx + 1 if (instruction_idx + 1) < len(instructions) else 0
    current_instruction = 0 if instructions[instruction_idx] == "L" else 1
    current_element = network_dict[current_element][current_instruction]

print(counter)


# Part 2

def check_nodes(node):
    return node[2]!='Z'


current_nodes = [i for i in network_dict.keys() if i[2] == "A"]
numerator = []
for node in current_nodes:
    counter = 0
    instruction_idx = -1
    loop = True
    while check_nodes(node):
        counter += 1
        instruction_idx = instruction_idx + 1 if (instruction_idx + 1) < len(instructions) else 0
        current_instruction = 0 if instructions[instruction_idx] == "L" else 1
        node = network_dict[node][current_instruction]
    numerator.append(counter)


result = lcm(*numerator)
print(result)