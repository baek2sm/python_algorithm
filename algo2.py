import sys


def greedy(length, numb_list):
    result = 0

    # 양수일 때
    i, last_numb = 0, 0
    numb_list = sorted(numb_list, reverse=True)
    while i < length and numb_list[i] > 1:
        if i % 2 == 0:
            last_numb = numb_list[i]
        else:
            result += last_numb * numb_list[i]
            last_numb = 0
        i += 1
    result += last_numb + numb_list.count(1)

    # 양수가 아닐 때
    i, last_numb = 0, 0
    numb_list = sorted(numb_list)
    while i < length and numb_list[i] <= 0:
        if i % 2 == 0:
            last_numb = numb_list[i]
        else:
            result += last_numb * numb_list[i]
            last_numb = 0
        i += 1
    result += last_numb

    return result


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    numb_list = [int(sys.stdin.readline()) for _ in range(n)]
    answer = greedy(n, numb_list)
    print(answer)