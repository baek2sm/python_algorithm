class Stack:
    def __init__(self, *args):
        self.data = list(args)

    def __str__(self):
        return str(self.data)

    # 데이터 삽입
    def push(self, value):
        self.data.append(value)
        return self.data

    # 데이터 삭제
    def pop(self):
        if len(self.data) == 0:
            # 언더플로우 예외 처리
            return
        else:
            return self.data.pop(-1)

    # 마지막 원소 확인
    def peek(self):
        if len(self.data) == 0:
            # 언더플로우 예외 처리
            return
        else:
            last_index = len(self.data) - 1
            return self.data[last_index]

    # 비었는지 확인
    def is_empty(self):
        return not self.data


if __name__ == '__main__':
    # 스택 인스턴스 생성
    stack = Stack(1, 2)
    print(stack)

    # 데이터 삽입
    stack.push(3)
    print(stack)

    # 데이터 삭제
    stack.pop()
    stack.pop()
    print(stack)

    # 마지막 원소 확인
    print(stack.peek())

    # 비었는지 확인
    print(stack.is_empty())