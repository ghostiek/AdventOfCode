import re
import math

with open('data.txt', 'r') as f:
    txt = f.read()

lines = txt.split('\n')

times = list(map(int, re.findall(r"(\d+)", lines[0])))
distance = list(map(int, re.findall(r"(\d+)", lines[1])))

# only variable that changes here

"""
Analytic Solution
Defined variables:
time_button_pressed = x
record_time = times[0]
x1 = distance[0]
t1 = record_time - time_button_pressed
v0 = time_button_pressed

# Formula, substitutions and quadratic equation
x1 < v0*t1
x1 < time_button_pressed*record_time - time_button_pressed^2
time_button_pressed^2 - time_button_pressed*record_time + x1 < 0
x^2 - bx + c
(record_time +- sqrt(record_time^2 - 4*x1))/2 = 0
"""

def get_bounds(record_time, x1):
    upper_bound = (record_time + math.sqrt(record_time**2 - 4*x1))/2
    lower_bound = (record_time - math.sqrt(record_time**2 - 4*x1))/2
    return math.floor(lower_bound)+1, math.ceil(upper_bound) - 1

final = 1
for idx in range(len(times)):
    current_time = times[idx]
    current_distance = distance[idx]
    lb, ub = get_bounds(current_time, current_distance)
    final *= (ub-lb+1)

print(final)

# Part 2
new_time = int("".join(list(map(str, times))))
new_dist = int("".join(list(map(str, distance))))

lb, ub = get_bounds(new_time, new_dist)
print(ub-lb+1)