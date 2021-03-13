class Node:
    def __init__(self, cup):
        self.cup = cup
        self.next = None

class CList():
    """
    Circular list
    """
    def __init__(self):
        self.head = None
        self.last = None    # previous to head

    def insertFirst(self, cup):
        node = Node(cup)
        self.head = node
        self.last = node
        node.next = node
        return node

    def insert(self, cup):
        node = Node(cup)
        node.next = self.head
        self.last.next = node
        self.last = node
        return node

class CupsGame():
    """AoC day 23 part 2 Cups Game"""

    def __init__(self):
        self.clist = CList()
        self.mapa = {}
        self.pickupMapa = {}
        self.maxValue = None

    def insertFirst(self, cup):
        cnode = self.clist.insertFirst(cup)
        self.mapa[cup] = cnode

    def insert(self, cup):
        cnode = self.clist.insert(cup)
        self.mapa[cup] = cnode

    def setMax(self, maxValue):
        self.maxValue = maxValue

    def pickup(self):
        pickupL = []
        phead = self.clist.head.next
        for i in range(3):
            pickupL.append(phead)
            self.pickupMapa[phead.cup] = True
            phead = phead.next
        self.clist.head.next = phead
        return pickupL


    def _getMax(self):
        candidate = self.maxValue
        while True:
            if candidate not in self.pickupMapa:
                return self.mapa[candidate]
            candidate -= 1


    def destination(self):
        current = self.clist.head.cup

        while True:
            current -= 1
            if current <= 0:
                # return max
                return self._getMax()
            elif current not in self.pickupMapa:
                return self.mapa[current]
        return None


    def print(self):
        self.clist.print()


    def insertPickup(self, destination, pickup):
        destNext = destination.next
        destination.next = pickup[0]
        pickup[2].next = destNext
        # clean pickupMapa
        self.pickupMapa = {}


    def moveHead(self):
        self.clist.last = self.clist.head
        self.clist.head = self.clist.head.next


def playgame(s, moves):
    cups = CupsGame()
    current = int(s[0])
    cups.insertFirst(current)

    for i in range(1, len(s)):
        cupsn = int(s[i])
        cups.insert(cupsn)

    for i in range(len(s)+1, 1_000_000 + 1):
        cups.insert(i)

    cups.setMax(1_000_000)

    for i in range(moves):
        pickup = cups.pickup()

        destination = cups.destination()

        cups.insertPickup(destination, pickup)
        cups.moveHead() # set current to next

    nodeOne = cups.mapa[1]
    first = nodeOne.next.cup
    second = nodeOne.next.next.cup
    return first * second


if __name__ == "__main__":
    print(playgame('389125467', 10_000_000))   # 149245887792
    print(playgame('614752839', 10_000_000))
