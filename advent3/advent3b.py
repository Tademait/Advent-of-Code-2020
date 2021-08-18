with open("advent3/input.txt", "r") as f:
    values = f.readlines()
width = len(values[0]) - 1  # subtract the newline character
horisontal_pos = 0
trees_hit = 0
vertical_pos = 0
product = 1
# possible use for a generator with range(,,slope[1])
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for slope in slopes:
    for row in values:
        if vertical_pos % slope[1] != 0:
            vertical_pos += 1
            continue
        if row[horisontal_pos % width] == "#":
            trees_hit += 1
        horisontal_pos += slope[0]
        vertical_pos += 1
    print(f"You'll encounter {trees_hit} trees on your way.")
    product = product * trees_hit
    trees_hit = 0
    vertical_pos = 0
    horisontal_pos = 0
print(f"The product of all the encountered trees is: {product}")
