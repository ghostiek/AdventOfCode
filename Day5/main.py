import helper

# Part 1
with open("data_instructions.txt", "r") as file:
    instructions = file.readlines()

instructions = [elem.replace("\n", "") for elem in instructions]

state = [
    ["C", "Q", "B"],
    ["Z", "W", "Q", "R"],
    ["V", "L", "R", "M", "B"],
    ["W", "T", "V", "H", "Z", "C"],
    ["G", "V", "N", "B", "H", "Z", "D"],
    ["Q", "V", "F", "J", "C", "P", "N", "H"],
    ["S", "Z", "W", "R", "T", "G", "D"],
    ["P", "Z", "W", "B", "N", "M", "G", "C"],
    ["P", "F", "Q", "W", "M", "B", "J", "N"]
]

"""
state = [
    ["N", "Z"],
    ["D", "C", "M"],
    ["P"]
]"""


for instruction in instructions:
    quantity, source, destination = helper.get_instruction(instruction)
    items = state[source][:quantity]
    for val in items:
        state[destination].insert(0, val)
    state[source] = state[source][quantity:]

result = ""
for letters in state:
    result += letters[0]

print(result)

"""state = [
    ["N", "Z"],
    ["D", "C", "M"],
    ["P"]
]"""

state = [
    ["C", "Q", "B"],
    ["Z", "W", "Q", "R"],
    ["V", "L", "R", "M", "B"],
    ["W", "T", "V", "H", "Z", "C"],
    ["G", "V", "N", "B", "H", "Z", "D"],
    ["Q", "V", "F", "J", "C", "P", "N", "H"],
    ["S", "Z", "W", "R", "T", "G", "D"],
    ["P", "Z", "W", "B", "N", "M", "G", "C"],
    ["P", "F", "Q", "W", "M", "B", "J", "N"]
]

for instruction in instructions:
    print("")
    quantity, source, destination = helper.get_instruction(instruction)
    items = reversed(state[source][:quantity])
    for val in items:
        state[destination].insert(0, val)
    state[source] = state[source][quantity:]
    print("")

result = ""
for letters in state:
    result += letters[0]

print(state)
print(result)