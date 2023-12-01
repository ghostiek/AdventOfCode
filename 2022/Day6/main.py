with open("data.txt", "r") as file:
    txt = file.read()


def find_idx(txt, slider_len):
    final_idx = 0
    for idx in range(len(txt) - slider_len):
        if len(set(txt[idx:idx + slider_len])) == slider_len:
            final_idx = idx
            break
    return final_idx+slider_len


# Part 1
part1 = find_idx(txt, 4)
print(part1)

# Part 2
part2 = find_idx(txt, 14)
print(part2)
