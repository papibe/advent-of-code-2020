import re

def solution(filename):

    def canContain(bag, myBag, bagmap):
        if bag == myBag:
            return False

        for inner in bagmap[bag]:
            if inner == myBag:
                return True
            if canContain(inner, myBag, bagmap):
                return True

        return False


    # read file
    with open(filename, 'r') as fp:
        data = fp.read().splitlines()

    # rules
    noinner = re.compile('^(\w+ \w+) bags contain no other bags')
    mainbag = re.compile('^(\w+ \w+) bags contain(.*)$')
    innerbags = re.compile(' (\w+) (\w+ \w+) bag')

    bagmap = {}

    for line in data:
        # simpler case: no inners
        mg = noinner.match(line)
        if mg is not None:
            bag = mg[1]
            bagmap[bag] = []
            continue

        # nested bags
        mg = mainbag.match(line)    # main bag (outer)
        bag = mg[1]
        restOfLine = mg[2]

        # parse rest of the line with inner bags
        oline = restOfLine.split(',')
        inners = []
        for inner in oline:
            mg = innerbags.match(inner)
            innerBag = mg[2]
            inners.append(innerBag)

        bagmap[bag] = inners

    count = 0
    for bag in bagmap:
        if canContain(bag, 'shiny gold', bagmap):
            count += 1

    return count


if __name__ == "__main__":
    print(solution("./inputs/example1.txt"))   # 4
    print(solution("./inputs/input.txt"))
