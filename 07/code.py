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

    last_beams = set()
    last_beams.add( data[0].find('S') )

    last_beams2 = []
    last_beams2.append( data[0].find('S') )

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
        for y in tqdm(range(1, height)):
            beams2 = []
            for beam in last_beams2:
                thing = data[y][beam]
                if thing == '.':
                    beams2.append(beam)
                elif thing == '^':
                    if beam > 0:
                        beams2.append(beam-1)
                    if beam < width-1:
                        beams2.append(beam+1)
            last_beams2 = beams2.copy()
        num = len(beams2)

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()
