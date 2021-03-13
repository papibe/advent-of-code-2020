def solution(filename):

    def parseDeck(filename):
        with open(filename, 'r') as fp:
            data = fp.read()

        rawDeck1, rawDeck2 = data.split('\n\n')
        deck1 = rawDeck1.splitlines()
        deck2 = rawDeck2.splitlines()

        return list(map(int, deck1[1:])), list(map(int, deck2[1:]))


    def regularPlay(card1, card2, deck1, deck2):
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

        return winner

    def score(deck):
        total = 0
        for i, card in enumerate(deck):
            total += card * (len(deck) - i)
        return total


    def getDeckID(deck):
        return ','.join([str(i) for i in deck])


    def remember(d1, d2, memo):
        id1 = getDeckID(d1)
        id2 = getDeckID(d2)
        if id1 in memo:
            memo[id1].append(id2)
        else:
            memo[id1] = [id2]

        if id2 in memo:
            memo[id2].append(id1)
        else:
            memo[id2] = [id1]


    def hasBeenHereBefore(d1, d2, memo):
        id1 = getDeckID(d1)
        id2 = getDeckID(d2)

        if (id1 not in memo) or (id2 not in memo):
            return False

        if (id2 in memo[id1]) and (id1 in memo[id2]):
            return True

        return False


    def newGame(deck1, deck2, memoplays):
        winner = None

        while deck1 and deck2:

            if hasBeenHereBefore(deck1, deck2, memoplays):
                winner = deck1
                return winner

            remember(deck1, deck2, memoplays)

            # draw cards
            card1 = deck1.pop(0)
            card2 = deck2.pop(0)

            # count remaining cards
            rcards1 = len(deck1)
            rcards2 = len(deck2)

            if (rcards1 >= card1) and (rcards2 >= card2):
                # Recursive Combat
                newdeck1 = deck1[:card1]
                newdeck2 = deck2[:card2]

                sgWinner = newGame(newdeck1, newdeck2, {})
                if sgWinner == newdeck1:
                    deck1.append(card1)
                    deck1.append(card2)
                    winner = deck1
                else:
                    deck2.append(card2)
                    deck2.append(card1)
                    winner = deck2
            else:
                # Standard play
                winner = regularPlay(card1, card2, deck1, deck2)

        return winner


    # main ---------------------------------------------------------------------
    deck1, deck2 = parseDeck(filename)

    winner = newGame(deck1, deck2, {})

    return score(winner)

if __name__ == "__main__":

    print(solution("./inputs/example1.txt"))   # 291
    print(solution("./inputs/temp2.txt"))  # 105
    print(solution("./inputs/input.txt"))
