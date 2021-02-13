import re

def solution(filename):

    def checkBYR(s_byr):
        byr = int(s_byr)
        return 1920 <= byr <= 2020


    def checkIYR(s_iyr):
        iyr = int(s_iyr)
        return 2010 <= iyr <= 2020


    def checkEYR(s_eyr):
        eyr = int(s_eyr)
        return 2020 <= eyr <= 2030


    def checkHGT(hgt):
        if hgt.endswith('cm'):
            height = int(hgt[:-2])
            return 150 <= height <= 193

        if hgt.endswith('in'):
            height = int(hgt[:-2])
            return 59 <= height <= 76

        return False


    def checkHCL(hcl):
        mg = re.match('^#[0-9a-f]{6}$', hcl)
        return mg is not None


    def checkECL(ecl):
        mg = re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', ecl)
        return mg is not None


    def checkPID(pid):
        mg = re.match('^[0-9]{9}$', pid)
        return mg is not None


    # main ---------------------------------------------------------------------
    with open(filename, 'r') as fp:
        rawData = fp.read()

    passports = rawData.split("\n\n")

    regexs = {
        "byr": "byr:([^\s]+)",
        "iyr": "iyr:([^\s]+)",
        "eyr": "eyr:([^\s]+)",
        "hgt": "hgt:([^\s]+)",
        "hcl": "hcl:([^\s]+)",
        "ecl": "ecl:([^\s]+)",
        "pid": "pid:([^\s]+)",
    }

    checkFunctions = {
        "byr": checkBYR,
        "iyr": checkIYR,
        "eyr": checkEYR,
        "hgt": checkHGT,
        "hcl": checkHCL,
        "ecl": checkECL,
        "pid": checkPID,
    }

    validPassports = 0
    for passport in passports:
        matchedFields = 0
        values = {}
        for line in passport.split("\n"):
            # check for all fields
            for field, regex in regexs.items():
                mg = re.search(regex, line)

                # count save matches
                if mg is not None:
                    matchedFields += 1
                    values[field] = mg[1]  # field value

        # If all fields were matched, passport is _potentially_ valid
        if matchedFields == len(regexs):

            # Apply a validation function to each field's value
            for field, checkFunction in checkFunctions.items():
                if not checkFunction(values[field]):
                    break
            else:
                validPassports += 1

    return validPassports


if __name__ == "__main__":
    print(solution("./inputs/example1.txt"))   # 2
    print(solution("./inputs/example2.txt"))   # 0
    print(solution("./inputs/example3.txt"))   # 4
    print(solution("./inputs/input.txt"))
