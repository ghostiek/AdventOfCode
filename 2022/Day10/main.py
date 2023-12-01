import numpy as np

# Part 1
with open("data.txt", "r") as file:
    txt = file.readlines()

txt = [elem.replace("\n", "") for elem in txt]


def get_cycle_result(txt, max_cycle):
    logged_values = []
    x = 1
    i=0
    idx=0
    while i < max_cycle:
        if txt[idx] == "noop":
            logged_values.append(0)
            i += 1
        elif txt[idx].startswith("addx"):
            value = txt[idx].split(" ")[-1]
            i += 2
            if i <= max_cycle - 1:
                logged_values.append(0)
                logged_values.append(int(value))
            else:
                logged_values.append(0)
        idx += 1
    result = (x + sum(logged_values)) * max_cycle
    return result, logged_values

total = 0
sprite = np.array([1, 2, 3])
letters = ""

result, vals = get_cycle_result(txt, 20)
total += result

result, vals = get_cycle_result(txt, 60)
total += result

result, vals = get_cycle_result(txt, 100)
total += result

result, vals = get_cycle_result(txt, 140)
total += result


result, vals = get_cycle_result(txt, 180)
total += result


result, vals = get_cycle_result(txt, 220)
total += result
print(total)


result, vals = get_cycle_result(txt, 240)



final_str = ""
for i in range(240):
    if (i + 1)%40 in sprite:
        final_str += "#"
    else:
        final_str += "."
    if (i + 1) % 40==0:
        final_str += "\n"
    sprite += vals[i]
print(final_str)



print(total)
