from tqdm import tqdm
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
    split = data.index('')
    ok,ingredients = data[:split],list(map(int, data[split+1:]))
    ok_ranges = []
    for i in ok:
        ok_ranges.append( list(map(int, i.split('-'))) )

    ok_ranges.sort()

    # CODE
    num = 0
    if part == Part.One:
        for i in ingredients:
            for range_min,range_max in ok_ranges:
                if i >= range_min and i <= range_max:
                    num += 1
                    break
    else:
        index = 0
        for range_min,range_max in ok_ranges:
            if range_min > index:
                num += range_max - range_min + 1
                index = range_max
            elif range_max <= index:
                pass
            else:
                num += range_max - (index + 1) + 1
                index = range_max

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()
