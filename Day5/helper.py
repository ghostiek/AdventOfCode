import re

def get_instruction(instruction):
    tmp = re.search(r"move (\d+) from (\d+) to (\d+)", instruction)
    grp = tmp.groups()
    quantity = int(grp[0])
    source = int(grp[1]) - 1
    destination = int(grp[2]) - 1
    return quantity, source, destination
