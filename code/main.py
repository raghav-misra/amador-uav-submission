# Square root for distance formula:
from math import sqrt

# Retrieve and parse the input from "input.in":
def get_input():
    lines_raw = []
    with open("input.in", "r") as input_file:
        for ln in input_file.readlines():
            tmp = ln.split(" ")
            lines_raw.append({
                'x': float(tmp[0]),
                'y': float(tmp[1].strip("\n"))
            }) 
        return lines_raw

# Calculate the distance between two points passed as dictionaries, e.g. {'x': [...], 'y': [...]}:
def dist_form(point1, point2): 
    return sqrt((point1['x'] - point2['x']) ** 2 + (point1['y'] - point2['y']) ** 2)

# Finds distance between each pair of points in the parsed input
def dist_iterator(points):
    final_string = ""
    for i in range(1, len(points)):
        res = dist_form(points[i - 1], points[i])
        final_string = f"{final_string}\n{round(res, 3)}".strip().strip("\n")
    return f"{final_string}\n0.0".strip("\n")

# Open the output file:
with open('output.out', 'w') as writer:
    # Retrieve the output:
    writable = dist_iterator(get_input())
    # Write it to 'output.out'
    writer.write(writable)
    # Print the output to the screen:
    print(writable)