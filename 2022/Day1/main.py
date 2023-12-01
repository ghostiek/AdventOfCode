# Star 1
with open("data.txt", "r") as file:
    txt = file.read()

elves = txt.split("\n\n")
elves_cals = [element.split("\n") for element in elves]

final_cals = []
for elf in elves_cals:
    final_cals.append(sum(list(map(int, elf))))
print(max(final_cals))

# Star 2

final_cals.sort(reverse=True)
print(sum(final_cals[:3]))