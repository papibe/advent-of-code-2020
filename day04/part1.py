import re

def solution(filename):
    with open(filename, 'r') as fp:
        rawData = fp.read()

    passports = rawData.split("\n\n")

    regexs = [
        "byr:",
        "iyr:",
        "eyr:",
        "hgt:",
        "hcl:",
        "ecl:",
        "pid:",
    ]

    validPassports = 0
    for passport in passports:
        matchedFields = 0
        for line in passport.split("\n"):
            # check for all fields
            for regex in regexs:
                match = re.search(regex, line)

                if match is not None:   # count matches
                    matchedFields += 1

        # If all fields were matched, passport is valid
        if matchedFields == len(regexs):
            validPassports += 1

    return validPassports


if __name__ == "__main__":
    print(solution("./inputs/example1.txt"))
    print(solution("./inputs/input.txt"))
