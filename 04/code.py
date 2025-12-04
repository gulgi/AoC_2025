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
    ranges = []
    file = open("test.txt" if test else "input.txt")
    data = file.read().splitlines()

    # pad data to skip loads of ifs
    data = [' ' + d + ' ' for d in data]
    data.insert(0, ' '*len(data[0]))
    data.append(' '*len(data[0]))

    width = len(data[0])
    height = len(data)

    def can_be_moved(data, x, y):
        if data[y][x] != '@':
            return False
        rolls  = data[y-1].count('@', x-1, x+2)
        rolls += data[y  ].count('@', x-1, x+2)
        rolls += data[y+1].count('@', x-1, x+2)
        return rolls < 5

    # CODE
    num = 0
    if part == Part.One:
        for y in range(1, height-1):
            for x in range(1, width-1):
                if can_be_moved(data, x, y):
                    num += 1
    else:
        data2 = data.copy()
        while True:
            data = data2.copy()
            old_num = num
            for y in range(1, height-1):
                for x in range(1, width-1):
                    if can_be_moved(data, x, y):
                        num += 1
                        data2[y] = data2[y][0:x] + 'x' + data2[y][x+1:]
            if old_num == num:
                break

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()
