# Star 1
with open("data.txt", "r") as file:
    txt = file.read()

import re

lines = txt.split("\n")
line_nums=[]
for line in lines:
    line_num = ""
    for char in line:
        if char.isnumeric():
            line_num += char

    if len(line_num) == 1:
        line_nums.append(int(line_num[0]+line_num[0]))
    elif len(line_num) > 1:
        line_nums.append(int(line_num[0] + line_num[-1]))

print(sum(line_nums))

# Star 2

# get first number

valid_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] + list(map(str, range(1,10)))


def get_first_digit(x):
    output = ""
    valid_options = []
    valid_digit = []
    for digit in valid_digits:
        idx = x.find(digit)
        if idx != -1:
            valid_options.append(idx)
            valid_digit.append(digit)
    if len(valid_options) > 0:
        argpos = valid_options.index(min(valid_options))
        output = valid_digit[argpos]
    return output

def get_last_digit(x): #func is min or max
    output = ""
    valid_options = []
    valid_digit = []
    for digit in valid_digits:
        idx = x.rfind(digit)
        if idx != -1:
            valid_options.append(idx)
            valid_digit.append(digit)
    if len(valid_options) > 0:
        argpos = valid_options.index(max(valid_options))
        output = valid_digit[argpos]
    return output

def text_to_num(x):
    if x == "":
        return x
    if not x[0].isnumeric():
        x = valid_digits[valid_digits.index(x)+9]
    return x
lines = txt.split("\n")
line_nums=[]
for line in lines:
    line_num = ""
    line_num+= text_to_num(get_first_digit(line))
    line_num+= text_to_num(get_last_digit(line))

    if len(line_num) == 1:
        line_nums.append(int(line_num[0]+line_num[0]))
    elif len(line_num) > 1:
        line_nums.append(int(line_num[0] + line_num[-1]))

print(sum(line_nums))
print()
