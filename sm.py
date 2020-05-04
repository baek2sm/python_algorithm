def search(a_list):
    result = 0
    t = 0
    for a in a_list:
        t += a
        if t <= a:
            t = a
        if t > result:
            result = t

    return result



if __name__ == '__main__':
    N = int(input())
    a_list = list(map(int, input().split()))
    answer = search(a_list)
    print(answer)