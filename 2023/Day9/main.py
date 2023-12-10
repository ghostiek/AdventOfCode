import re

# Part 1
with open("data.txt", "r") as file:
    txt = file.read()

info = txt.split("\n")


def get_diff(seq):
    return [y - x for x, y in zip(seq, seq[1:])]


def predict(seq):
    first_elem = 0
    last_elem = 0
    alternate_op = 1
    while sum(seq) != 0:
        first_elem += alternate_op*seq[0]
        alternate_op *= -1
        last_elem += seq[-1]
        seq = get_diff(seq)
    return first_elem, last_elem


pt1_total = 0
pt2_total = 0
for line in info:
    x = list(map(int, line.split(" ")))
    first, last = predict(x)
    pt1_total += last
    pt2_total += first

print(pt1_total)
print(pt2_total)
