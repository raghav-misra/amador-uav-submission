'''
One of the main tasks of our UAV is to visit all of the provided waypoints. 
    To do this, we need to tell our UAV which way to go. 
    Given an input of a newline-separated list of points in the form  x y 
    (where x and y are coordinates on a traditional 2D Cartesian grid), 
    output the distance (rounded to the nearest thousandth) to the next point. 
    (The last point should just have a distance of zero.)

Input Format: A file with a list of points (x, y) 
    separated by newlines. 

Output Format: A file with a list of distances to the next point separated by newlines. 
    The last distance should be 0.
'''

def dist_form(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def get_input():
    lines_raw = []
    with open("input.in", "r") as input_file:
        for ln in input_file.readlines():
            tmp = ln.split(" ")
            lines_raw.append({
                'x': round(float(tmp[0]), 3),
                'y': round(float(tmp[1].strip("\n")), 3)
            }) 
        print(lines_raw)

raw_input_data = get_input()