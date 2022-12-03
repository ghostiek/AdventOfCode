import helper

# Part 1
with open("data.txt", "r") as file:
    txt = file.readlines()

txt = [elem.replace("\n", "") for elem in txt]

total = 0
for compartment in txt:
    fh, sh = helper.split_mid(compartment)
    same_char = helper.find_dupe(fh, sh)
    val = helper.get_score(same_char)
    total += val
print(total)

# Part 2
num_iter = int(len(txt)/3)
total = 0
for idx in range(num_iter):
    adjusted_idx = 3*idx
    same_char = helper.find_dupe2(txt[adjusted_idx], txt[adjusted_idx+1], txt[adjusted_idx+2])
    val = helper.get_score(same_char)
    total += val

print(total)
