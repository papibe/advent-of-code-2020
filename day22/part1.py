def solution(filename):

    def parseDeck(filename):
        with open(filename, 'r') as fp:
            data = fp.read()

        rawDeck1, rawDeck2 = data.split('\n\n')
        deck1 = rawDeck1.splitlines()
        deck2 = rawDeck2.splitlines()

        return list(map(int, deck1[1:])), list(map(int, deck2[1:]))


    deck1, deck2 = parseDeck(filename)

    while deck1 and deck2:
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        if card1 > card2:
            winner = deck1
            topcard = card1
            bottomcard = card2
        else:
            winner = deck2
            topcard = card2
            bottomcard = card1

        winner.append(topcard)
        winner.append(bottomcard)

    winner.reverse()

    return sum([card * (i + 1) for i, card in enumerate(winner)])

if __name__ == "__main__":

    print(solution("./inputs/example1.txt"))    # 306
    print(solution("./inputs/input.txt"))
