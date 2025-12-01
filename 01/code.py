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
    numbers = []
    file = open("test.txt" if test else "input.txt")
    for l in file.readlines():
        number = int(l[1:-1])
        if l[0] == 'L':
            number *= -1
        numbers.append(number)

    current = 50

    # CODE
    num = 0
    if part == Part.One:
        for n in numbers:
            current += n
            current = current % 100
            if current == 0:
                num += 1
    else:
        for n in numbers:
            before = current
            num += (abs(n) // 100)

            fixed_n = abs(n) % 100
            if n < 0:
                fixed_n = -fixed_n
            current += fixed_n

            if before != 0 and (current <= 0 or current >= 100):
                num += 1
            current = current % 100

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()
