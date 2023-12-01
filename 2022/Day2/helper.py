def replace_map(row, dictionary):
    for key, value in dictionary.items():
        row = row.replace(key, value)
    return row