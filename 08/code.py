from tqdm import tqdm
from functools import lru_cache
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

    num_points = len(points)
    connections = []
    if True: #part == Part.One:
        for i in range(0, num_points-1):
            for j in range(i+1, num_points):
                dist = math.dist(points[i], points[j])
                connections.append((dist, i, j))
        connections.sort(key=lambda x: x[0])

    num_boxes = 10 if test else 1000
    if part == Part.Two:
        num_boxes = len(connections)
    # CODE

    circuits = []
    num = 0
    for connection in connections[:num_boxes]:
        _, i, j = connection
        s = set()
        s.add(i)
        s.add(j)
        hits = 0
        indices = []
        for index in range(0, len(circuits)):
            if len(s & circuits[index]) > 0:
                circuits[index] = s.union(circuits[index])
                hits += 1
                indices.append(index)
        if hits == 0:
            circuits.append(s)
        elif hits > 1:
            indices.sort(reverse=True)
            num_indices = len(indices)
            combined = set()
            for i in indices[:-1]:
                combined = combined.union(circuits[i])
                del circuits[i]
            circuits[indices[-1]] = combined.union(circuits[indices[-1]])

        if part == Part.Two:
            if len(circuits[0]) == num_points:
                num = points[i][0] * points[j][0]
                break

    if part == part.One:
        circuits.sort(key=lambda x: len(x), reverse=True)
        num = 1
        for circuit in circuits[0:3]:
            num *= len(circuit)

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()
