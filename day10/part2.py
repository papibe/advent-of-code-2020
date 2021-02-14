class Node:

    def __init__(self, index):
        self.index = index
        self.count = 0
        self.children = []

    def add(self, node):
        self.children.append(node)

    def hit(self):
        self.count += 1


def solution(filename):
    # read file
    with open(filename, 'r') as fp:
        data = fp.read().splitlines()

    adapters = [int(number) for number in data]
    adapters.sort()

    adapters.insert(0, 0)    # insert representation of the wall at the begining
    adapters.append(adapters[-1] + 3)     # append representation of the device

    # for initial charger (wall both index an value 0)
    wallNode = Node(0)
    wallNode.hit()

    # BFS init steps
    queue = []
    visited = []
    queue.append(wallNode)

    # for memoization
    memo = {}
    memo[0] = wallNode

    # BFS style navegation
    while queue:
        chargerNode = queue.pop(0)

        index = chargerNode.index
        charger = adapters[index]

        i = index + 1
        for i in range(i, len(adapters)):
            adapter = adapters[i]
            diff = adapter - charger
            if diff <= 3:
                if i in memo:
                    chargerNode.add(memo[i])
                else:
                    nnode = Node(i)
                    chargerNode.add(nnode)
                    memo[i] = nnode

                    queue.append(memo[i])

                memo[i].count += chargerNode.count

            # since adapters are sorted, once pass diff 3 we can stop searching
            else:
                break

    device_index = len(adapters) - 1
    device_node = memo[device_index]
    return device_node.count

if __name__ == "__main__":
    print(solution("./inputs/example1.txt"))   # 8
    print(solution("./inputs/example2.txt"))   # 19208
    print(solution("./inputs/input.txt"))
