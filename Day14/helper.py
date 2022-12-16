def parse_line(path):
    return [parse_coordinates(coords) for coords in path.split(" -> ")]


def parse_coordinates(coords):
    coords = coords.split(",")
    return coords[0], coords[1]


def create_rocks(coords):
    rock_lines = []
    for idx in range(1, len(coords)):
        start_coord = (int(coords[idx-1][0]), int(coords[idx-1][1]))
        end_coord = (int(coords[idx][0]), int(coords[idx][1]))

        x_range = end_coord[0] - start_coord[0]
        y_range = end_coord[1] - start_coord[1]

        x_diff = range(0, x_range) if x_range >= 0 else range(x_range, 0)
        y_diff = range(0, y_range) if y_range >= 0 else range(y_range, 0)
        if x_range == 0:
            for y in y_diff:
                rock_lines.append((start_coord[0], start_coord[1]+y))
            rock_lines.append(end_coord)
            rock_lines.append(start_coord)
        if y_range == 0:
            for x in x_diff:
                rock_lines.append((start_coord[0]+x, start_coord[1]))
            rock_lines.append(end_coord)
            rock_lines.append(start_coord)
    return list(set(rock_lines))
