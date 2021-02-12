def solution(filename):

    def inverse(a, b):
        """
        Calculate the inverse of a in module b
        """
        return pow(a, -1, b)


    def CRT_solution(remainders, moduli):
        """
        Applies the Chinese remainder theorem solution formula
        """
        N = 1
        for modulo in moduli:
            N *= modulo

        Ni = []
        for modulo in moduli:
            Ni.append(N//modulo)

        total = 0
        for i in range(len(moduli)):
            total += remainders[i] * Ni[i] * inverse(Ni[i], moduli[i])

        return total % N


    # read data from file
    with open(filename, 'r') as fp:
        data = fp.read().splitlines()

    # parse data
    rawBuses = data[1].split(',')
    buses = [(ts, int(bus)) for ts, bus in enumerate(rawBuses) if bus != 'x']

    adjustment = buses[-1][0]   # last timestamp

    # make a list of remainders and mods (buses)
    remainders = [(adjustment - ts) for ts, bus in buses]
    buses = [bus for ts, bus in buses]

    # Chinese remainder theorem function
    result = CRT_solution(remainders, buses)

    return result - adjustment


if __name__ == "__main__":
    print(solution("./inputs/example1.txt"))
    print(solution("./inputs/example2.txt"))
    print(solution("./inputs/example3.txt"))
    print(solution("./inputs/example4.txt"))
    print(solution("./inputs/example5.txt"))
    print(solution("./inputs/example6.txt"))
    print(solution("./inputs/input.txt"))
