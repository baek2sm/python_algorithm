import sys


def greedy(length, numb_list):
    result = 0
    # 양수일 때 처리
    for i in range(0, length, 2):
        # 이번 원소가 음수 또는 0이면
        if numb_list[i] <= 0:
            break
        # 다음 원소가 없으면
        elif i+1 == length:
            result += numb_list[i]
        # 다음 원소도 양수면
        elif numb_list[i+1] > 0 and not numb_list[i+1] == 1:
            result += numb_list[i] * numb_list[i+1]
        elif numb_list[i+1] == 1:
            result += numb_list[i] + numb_list[i+1]
        # 다음 원소가 양수가 아니게 되면
        elif numb_list[i] > 0 and not numb_list[i + 1] > 0:
            result += numb_list[i]
            break

    # 음수 또는 0일 때 처리
    for i in range(length-1, -1, -2):
        # 이번 원소가 양수면
        if numb_list[i] > 0:
            break
        # 다음 원소가 없으면
        elif i == 0:
            result += numb_list[i]
        # 다음 원소도 음수 또는 0이면
        if numb_list[i-1] < 0:
            result += numb_list[i] * numb_list[i-1]
        # 다음 원소가 양수가 되면
        if numb_list[i-1] > 0:
            result += numb_list[i]

    return result


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    numb_list = [int(sys.stdin.readline()) for _ in range(n)]
    numb_list = sorted(numb_list, reverse=True)
    answer = greedy(n, numb_list) if n != 1 else numb_list[0]
    print(answer)