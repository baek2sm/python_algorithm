def search(N, st):
    result_list = []
    for i in range(N):
        counter = 0
        for s, e in st:
            if s < st[i][0] < e and e < st[i][1]:
                counter += 1
            elif s < st[i][0] and st[i][1] < e:
                counter += 1
        result_list.append(counter)

    return result_list


if __name__ == '__main__':
    N = int(input())
    skill_time = [tuple(map(int, input().split())) for _ in range(N)]
    answer_list = search(N, skill_time)
    for answer in answer_list:
        print(answer)