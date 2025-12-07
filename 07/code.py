from tqdm import tqdm
from functools import lru_cache
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

    start_x = data[0].find('S')
    last_beams = set()
    last_beams.add( start_x )

    width = len(data[0])
    height = len(data)

    # CODE
    num = 0
    if part == Part.One:
        for y in range(1, height):
            beams = set()
            for beam in last_beams:
                thing = data[y][beam]
                if thing == '.':
                    beams.add(beam)
                elif thing == '^':
                    if beam > 0:
                        beams.add(beam-1)
                    if beam < width-1:
                        beams.add(beam+1)
                    num += 1
            last_beams = beams.copy()
    else:
        @lru_cache(maxsize=None)
        def func(x, y):
            if y == height-1:
                return 1
            thing = data[y][x]
            if thing == '.':
                return func(x, y+1)
            num = 0
            if x > 0:
                num += func(x-1, y+1)
            if x < width-1:
                num += func(x+1, y+1)
            return num

        num = func( start_x, 0)

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()
