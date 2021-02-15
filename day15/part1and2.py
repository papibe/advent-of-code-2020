def solution(numbers, nPlays):

    memo = {}
    for i, number in enumerate(numbers):
        memo[number] = i+1

    lastSpoken = numbers[len(numbers)-1]
    del memo[lastSpoken]    # we add lastSpoken in next iteration

    for _turn in range(len(numbers), nPlays):
        turn = _turn + 1

        if lastSpoken in memo:
            spoken = turn - 1 - memo[lastSpoken]
        else:
            spoken = 0

        memo[lastSpoken] = turn - 1
        lastSpoken = spoken

    return spoken

if __name__ == "__main__":

    # part 1 examples
    print(2020, solution([0,3,6], 2020))   # 436.
    print(2020, solution([1,3,2], 2020))   # 1.
    print(2020, solution([2,1,3], 2020))   # 10.
    print(2020, solution([1,2,3], 2020))   # 27.
    print(2020, solution([2,3,1], 2020))   # 78.
    print(2020, solution([3,2,1], 2020))   # 438.
    print(2020, solution([3,1,2], 2020))   # 1836.

    # part 1 main puzzle
    print(2020, solution([11,18,0,20,1,7,16], 2020))

    # part 2 examples
    print(30000000, solution([0,3,6], 30000000))   # 175594
    print(30000000, solution([1,3,2], 30000000))   # 2578
    print(30000000, solution([2,1,3], 30000000))   # 3544142
    print(30000000, solution([1,2,3], 30000000))   # 261214
    print(30000000, solution([2,3,1], 30000000))   # 6895259
    print(30000000, solution([3,2,1], 30000000))   # 18
    print(30000000, solution([3,1,2], 30000000))   # 362

    # part 2 main puzzle
    print(30000000, solution([11,18,0,20,1,7,16], 30000000))
