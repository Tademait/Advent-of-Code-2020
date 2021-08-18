with open("input.txt", "r") as f:
    values = f.readlines()
width = len(values[0]) - 1  # subtract the newline character
horisontal_pos = 0
trees_hit = 0
for row in values:
    if row[horisontal_pos % width] == "#":
        trees_hit += 1
    horisontal_pos += 3
print(f"You'll encounter {trees_hit} trees on your way.")
