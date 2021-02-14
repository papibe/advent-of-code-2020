import re

def solution(filename):
    # read file
    with open(filename, 'r') as fp:
        instructions = fp.read().splitlines()

    instructionRE = re.compile('^(\w\w\w) ([+-]\d+)$')

    operMemo = {}
    accumulator = 0
    i = 0
    while i < len(instructions):
        # parsing
        mg = instructionRE.match(instructions[i])
        opereration = mg[1]
        argument = int(mg[2])

        # we have been before
        if i in operMemo:
            return accumulator

        operMemo[i] = True  # remember being here

        if opereration == 'nop':
            pass

        elif opereration == "acc":
            accumulator += argument

        elif opereration == "jmp":
            i += argument
            continue

        i += 1  # go to next operation


if __name__ == "__main__":
    print(solution("./example1.txt"))   # 5
    print(solution("./input.txt"))
