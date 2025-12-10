from tqdm import tqdm
from functools import lru_cache
import numpy as np
import math
from enum import Enum
import sys

class Part(Enum):
    One = 1,
    Two = 2

def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False

    # Read in file
    file = open("test.txt" if test else "input.txt")
    data = file.read().splitlines()
    points = []
    for d in data:
        points.append( tuple(map(int, d.split(','))) )
    if part == part.One:
        points.sort(key=lambda x : x[0]) # and not have to think about x0 < x1
    num_points = len(points)

    # CODE
    def area(p0, p1):
        width = 1 + p1[0] - p0[0]
        height = 0
        if p0[1] < p1[1]:
            height = 1 + p1[1] - p0[1]
        else:
            height = p0[1] - p1[1]
        return width * height

    num = 0
    if part == part.One:
        for i in range(0, num_points-1):
            for j in range(i+1, num_points):
                new_area = area(points[i], points[j])
                #print(f"{points[i]} {points[j]} => {new_area}")
                if new_area > num:
                    num = new_area
    else:
        for i in range(0, num_points-1):
            for j in range(i+1, num_points):
                new_area = area(points[i], points[j])
                #print(f"{points[i]} {points[j]} => {new_area}")
                if new_area > num:
                    num = new_area

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()
