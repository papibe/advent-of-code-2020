import re

def solution(filename):
    # read file
    with open(filename) as fp:
        data = fp.readlines()

    validPasswords = 0
    
    # set up regular expresion to parse lines
    parseEx = re.compile('([0-9]+)-([0-9]+) (\w): (\w+)')

    for rule in data:
        # parse rule
        mg = parseEx.match(rule)    # matching group
        lower = int(mg[1])
        upper = int(mg[2])
        letter = mg[3]
        password = mg[4]

        occurrences = password.count(letter)

        if occurrences >= lower and occurrences <= upper:
            validPasswords += 1

    return validPasswords


if __name__ == "__main__":
    print(solution('./example1.txt'))
    print(solution('./input.txt'))
