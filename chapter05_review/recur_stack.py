# 스택으로 재귀함수 구현

from stack import Stack

def recur(n: int) -> int:
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)
            n = n - 1
            continue
        if not s.is_emtpy():
            n = s.pop()
            print(n)
            n = n - 2
            continue
        break