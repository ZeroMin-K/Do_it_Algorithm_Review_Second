# 순수 재귀함수 구현

def recur(n: int) -> int:
    # 순수 재귀함수 recur 구현
    if n > 0:
        recur(n-1)
        print(n)
        recur(n-2)

x = int(input('정수값 입력: '))

recur(x)