import sys


if __name__ == '__main__':
    number_list = [int(i) for i in sys.stdin.readline() if i != '\n']

    if sum(number_list) % 3 != 0 or 0 not in number_list:
        print(-1)
    else:
        number_list = sorted(number_list, key=lambda x: x, reverse=True)
        print(''.join(map(str, number_list)))

        