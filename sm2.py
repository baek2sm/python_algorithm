def search(group_list, stat_list):
    result = 0
    for group in group_list:
        l, r = 100000000, 1
        t, b = 1, 100000000
        for i in group:
            if l > stat_list[i-1][0]:
                l = stat_list[i-1][0]
            if r < stat_list[i-1][0]:
                r = stat_list[i-1][0]
            if t < stat_list[i-1][1]:
                t = stat_list[i-1][1]
            if b > stat_list[i-1][1]:
                b = stat_list[i-1][1]
        width = r - l
        height = t - b
        r_round = (width+height)*2
        if r_round > result:
            result = r_round
    return result


if __name__ == '__main__':
    N, M = map(int, input().split())
    n_list = [tuple(map(int, input().split())) for _ in range(N)]
    m_list = [set(map(int, input().split())) for _ in range(M)]

    group_list = [{i} for i in range(1, N+1)]
    for m in m_list:
        index = -1
        delete_index = []
        for i in range(len(group_list)):
            if m & group_list[i]:
                if index == -1:
                    group_list[i] |= m
                    index = i
                else:
                    group_list[index] |= group_list[i]
                    delete_index.append(i)
                    index = -1
                    break

        for _ in range(len(delete_index)):
            i = delete_index.pop()
            group_list.pop(i)

    answer = search(group_list, n_list)
    print(answer)
