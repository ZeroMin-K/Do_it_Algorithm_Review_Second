def med3(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

print('세 정수의 중앙 값 계산')
a = int(input('정수 a 값 입력: '))
b = int(input('정수 b 값 입력: '))
c = int(input('정수 c 값 입력: '))

print(f'중앙값은 {med3(a, b, c)}')
