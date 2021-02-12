import re

def solution(filename):

    n = 1068781

    buses = [7, 13, 59, 31, 19]
    disp = [0, 1, 4, 6, 7]

    N = 1
    for bus in buses:
        N *= bus

    Ni = []
    for bus in buses:
        Ni.append(N//bus)

    E1 = 0
    for i in range(len(buses)):
        E1 += Ni[i]


    E2 = 0
    for i in range(len(buses)):
        E2 += disp[i]*Ni[i]


    print(N)
    print(Ni)
    print(E1)
    print(E2)
    k = (n*E1 + E2)//N
    print('k=', k)

    print('n(k)', (N*k -E2)/E1)

    k = 0
    while True:
        sol1 = (N*k -E2) // E1
        sol = (N*k -E2)
        if (sol % E1) == 0:
            print('modi', k, sol)
            # break
        if sol1 == n:
            print('arrived', k, sol1)
            break
        # print(k)
        k += 1



if __name__ == "__main__":
    solution("./mytemp.txt")
