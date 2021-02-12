def solution(filename):

    with open(filename, 'r') as fp:
        data = fp.read().splitlines()

    # parsing data
    eTimestamp = int(data[0])
    sline = data[1].split(',')
    buses = [int(bus) for bus in sline if bus != 'x']


    # start checking timestamps from the earliest 
    timeStamp = eTimestamp
    while True:
        for bus in buses:
            if (timeStamp % bus) == 0:
                wait = timeStamp - eTimestamp
                return wait * bus

        timeStamp += 1


if __name__ == "__main__":
    result = solution("./inputs/example1.txt")
    print(result)

    result = solution("./inputs/input.txt")
    print(result)
