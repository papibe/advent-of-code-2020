def splitCups(cups, current):
    newcups = []
    pickup = []

    currentIndex = cups.index(current)
    while len(pickup) < 3:
        popIndex = (currentIndex+1)% len(cups)
        pickup.append(cups.pop(popIndex))
        currentIndex = cups.index(current)
    return (cups, pickup)


def getDestination(currentcup, cups):
    currentIndex = cups.index(currentcup)
    while True:
        currentcup -= 1
        if currentcup < 0:
            return cups.index(max(cups))
        else:
            if currentcup in cups:
                return cups.index(currentcup)
    return None


def solution(inputStr, moves):
    cups = [int(c) for c in inputStr]
    ncups = len(cups)

    currentIndex = 0
    for i in range(moves):
        current = cups[currentIndex]
        cups, pickup = splitCups(cups, current)
        destinationIndex = getDestination(current, cups)

        # reemsable cups
        cups[destinationIndex+1:destinationIndex+1] = pickup
        currentIndex = cups.index(current)
        currentIndex = (currentIndex + 1) % ncups

    # form final output
    index = (cups.index(1) + 1) % len(cups)
    result = []
    for i in range(len(cups)-1):
        result.append(str(cups[index]))
        index = (index + 1) % len(cups)
    return ''.join(result)


if __name__ == "__main__":
    print(solution("389125467", 10))    # 92658374
    print(solution("389125467", 100))   # 67384529
    print(solution("614752839", 100))
