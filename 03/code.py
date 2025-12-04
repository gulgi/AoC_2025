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

    # CODE
    num = 0
    batteries = 2
    if part == Part.Two:
        batteries = 12

    def f(s, start, left):
        for i in range(9, 0, -1):
            index = s.find(str(i), start+1, len(s)-left)
            if index != -1:
                return s[index], index

    for d in data:
        numbers = []
        index = -1

        left = batteries - 1
        for i in range(0, batteries):
            n, index = f(d, index, left)
            numbers.append(n)
            left -= 1
        #print("".join(numbers))
        num += int("".join(numbers))

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()
