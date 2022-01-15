from re import S


def sum_1ton(n):
    s = 0
    while n > 0:
        s += n
        n -= 1

    return s

x = int(input('x의 값 입력: '))
print(f'1부터 {x}까지 정수의 합 {sum_1ton(x)}')