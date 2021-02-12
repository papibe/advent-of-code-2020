import re

def solution(filename):
    # read file
    with open(filename) as fp:
        data = fp.readlines()

    validPasswords = 0

    # set up regular expresion to parse lines
    parseEx = re.compile('([0-9]+)-([0-9]+) (\w): (\w+)')

    for rule in data:
        # parse line
        mg = parseEx.match(rule)    # mg is the match group
        lower = int(mg[1])
        upper = int(mg[2])
        letter = mg[3]
        password = mg[4]

        char1 = password[lower-1]
        char2 = password[upper-1]

        # count with new interpretation of the rules
        if char1 == letter and char2 != letter:
            validPasswords += 1
        if char1 != letter and char2 == letter:
            validPasswords += 1

    return validPasswords


if __name__ == "__main__":
    print(solution('./example1.txt'))
    print(solution('./input.txt'))
