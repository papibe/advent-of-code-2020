import re

def solution(filename):

    def countBags(bag, bagmap):
        count = 0
        for inner, n in bagmap[bag]:
            icount = countBags(inner, bagmap)
            count += (n * icount) + n

        return count


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
            n = int(mg[1])
            innerBag = mg[2]
            inners.append((innerBag, n))

        bagmap[bag] = inners

    nbags = countBags('shiny gold', bagmap)

    return nbags


if __name__ == "__main__":
    print(solution("./inputs/example1.txt"))   # 32
    print(solution("./inputs/example2.txt"))   # 126
    print(solution("./inputs/input.txt"))
