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
    data = file.read()
    index = -1
    while True:
        index2 = data.find('-', index+1)
        num1 = int(data[index+1:index2])
        index = data.find(',', index2+1)
        num2 = int(data[index2+1:index])
        ranges.append([num1, num2])
        if index == -1:
            break

    # CODE
    num = 0
    if part == Part.One:
        for start,end in ranges:
            n = start
            while n <= end:
                n_str = str(n)
                len_n = len(n_str)
                len_n2 = len_n//2
                if len_n % 2 != 0:
                    n += 1
                    continue

                if n_str[0:len_n2] == n_str[len_n2:]:
                    num += n
                n += 1
    else:
        for start,end in ranges:
            n = start
            while n <= end:
                n_str = str(n)
                len_n = len(n_str)
                for r in range(1, len_n):
                    if len_n % r != 0:
                        continue
                    s = n_str[0:r]
                    count = n_str.count(s)
                    if count == len_n//r:
                        num += n
                        break
                n += 1

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()
