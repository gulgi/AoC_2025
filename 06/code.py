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
    numbers,signs = data[0:-1], [d.split() for d in data[-1:]][0]
    filtered_numbers = [d.split() for d in numbers]

    columns = len(signs)
    actual_width = len(numbers[0])
    height = len(numbers)
    results = columns*[1]

    def func_and_startvalue(sign):
        func = lambda a, b : a * b
        if sign == '+':
            func = lambda a, b : a + b
            return func, 0
        return func, 1

    # CODE
    num = 0
    if part == Part.One:
        for x in range(0, columns):
            func, results[x] = func_and_startvalue(signs[x])
            for y in range(0, height):
                results[x] = func(results[x], int(filtered_numbers[y][x]))
    else:
        column = 0
        func, results[column] = func_and_startvalue(signs[column])

        for x in range(0, actual_width):
            this_number = ""
            for y in range(0, height):
                if numbers[y][x] != ' ':
                    this_number += numbers[y][x]
            if this_number == "":
                column += 1
                func, results[column] = func_and_startvalue(signs[column])
            else:
                results[column] = func(results[column], int(this_number))
    num = sum(results)

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()
