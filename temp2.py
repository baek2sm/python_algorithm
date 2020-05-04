import sys


# 행의 개수가 홀수일 때 경로 탐색
def find_path_for_h_odd(r, c):
    route = str()
    for i in range(r):
        for j in range(c):
            # 짝수 행이면서 마지막 칸은 아닐 때
            if i % 2 == 0 and j != c - 1:
                route += 'R'
            # 마지막이 아닌 짝수 행의 마지막 칸일 때
            elif i % 2 == 0 and i != r - 1:
                route += 'D'
            # 홀수 행이면서 마지막 칸은 아닐 때
            elif j != c - 1:
                route += 'L'
            # 마지막이 아닌 홀수 행의 마지막 칸일 때
            elif i != r - 1:
                route += 'D'
    return route


# 열의 개수가 홀수일 때 경로 탐색
def find_path_for_v_odd(r, c):
    route = str()
    for j in range(c):
        for i in range(r):
            # 짝수 열이면서 마지막 칸은 아닐 때
            if j % 2 == 0 and i != r - 1:
                route += 'D'
            # 마지막이 아닌 짝수 열의 마지막 칸일 때
            elif j % 2 == 0 and j != c - 1:
                route += 'R'
            # 홀수 열이면서 마지막 칸은 아닐 때
            elif j % 2 == 1 and i != r - 1:
                route += 'U'
            # 마지막이 아닌 홀수 열의 마지막 칸일 때
            elif j % 2 == 1 and j != c - 1:
                route += 'R'
    return route


# 행, 열의 개수가 모두 짝수일 때
def find_path_for_even(x, y, r, c):
    route = str()
    for i in range(r):
        for j in range(c):
            if i == x:

                continue

            # 짝수 행이면서 마지막 칸은 아닐 때
            if i % 2 == 0 and j != c - 1:
                route += 'R'
            # 마지막이 아닌 짝수 행의 마지막 칸일 때
            elif i % 2 == 0 and i != r - 1:
                route += 'D'
            # 홀수 행이면서 마지막 칸은 아닐 때
            elif j != c - 1:
                route += 'L'
            # 마지막이 아닌 홀수 행의 마지막 칸일 때
            elif i != r - 1:
                route += 'D'

    return route


if __name__ == '__main__':
    r, c = map(int, sys.stdin.readline().split())
    mat = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

    # 행의 개수가 홀수일 때
    if r % 2 == 1:
        answer = find_path_for_h_odd(r, c)
    # 열의 개수가 홀수일 때
    if c % 2 == 1:
        answer = find_path_for_v_odd(r, c)
    else:
        x, y = 0, 1
        for i in range(r):
            for j in range(c):
                print('현재 값:', mat[x][y])
                if (i + j) % 2 != 0 and mat[x][y] > mat[i][j]:
                    print(i, j)
                    x, y = i, j

        answer = find_path_for_even(x, y, r, c)

    print(answer)


