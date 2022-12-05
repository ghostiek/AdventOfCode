import helper

# Part 1
with open("data.txt", "r") as file:
    txt = file.readlines()

txt = [elem.replace("\n", "") for elem in txt]

total = 0
for pair in txt:
    elves = pair.split(",")
    elf1 = elves[0]
    elf2 = elves[1]
    set1 = helper.get_ranges_set(elf1)
    set2 = helper.get_ranges_set(elf2)
    if set1.issuperset(set2) or set2.issuperset(set1):
        total+=1

print(total)

# Part 2

total = 0
for pair in txt:
    elves = pair.split(",")
    elf1 = elves[0]
    elf2 = elves[1]
    set1 = helper.get_ranges_set(elf1)
    set2 = helper.get_ranges_set(elf2)
    if len(set1.intersection(set2)) > 0:
        total+=1

print(total)

