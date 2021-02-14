import re

instructionRE = re.compile('^(\w\w\w) ([+-]\d+)$')

def execute(program, i, n, accumulator, changed, visited):

    # edge case: we reach beyond the end of the program
    if i > n:
        return (True, accumulator)

    # edge case: it's a loop
    if i in visited:
        return (False, accumulator)

    visited.append(i)

    mg = instructionRE.match(program[i])
    operation = mg[1]
    argument = int(mg[2])

    if operation == "acc":
        return execute(program, i+1, n, accumulator + argument, changed, visited)

    # already changed, so not change atm
    elif changed:
        if operation == 'nop':
            return execute(program, i+1, n, accumulator, changed, visited)
        elif operation == "jmp":
            return execute(program, i+argument, n, accumulator, changed, visited)

    # not changed yet
    else:
        if operation == 'nop':
            (rc, ac) = execute(program, i+1, n, accumulator, False, visited)
            if rc:
                return (True, ac)

            # replace operation
            (rc, ac) = execute(program, i+argument, n, accumulator, True, visited[:])
            if rc:
                return (True, ac)

            return (False, -1)

        elif operation == 'jmp':
            (rc, ac) = execute(program, i+argument, n, accumulator, False, visited)
            if rc:
                return (True, ac)

            # replace operation
            (rc, ac) = execute(program, i+1, n, accumulator, True, visited[:])
            if rc:
                return (True, ac)

            return (False, -1)


def solution(filename):
    # read file
    with open(filename, 'r') as fp:
        data = fp.read().splitlines()

    program = data
    visited = []
    accumulator = 0

    i = 0   # initial instruction
    n = len(program) - 1    # last instruction
    changed = False

    rc, accumulator = execute(program, i, n, accumulator, changed, visited)

    if rc:
        return accumulator
    else:
        return None


if __name__ == "__main__":
    print(solution("./example1.txt"))   # 8
    print(solution("./input.txt"))
