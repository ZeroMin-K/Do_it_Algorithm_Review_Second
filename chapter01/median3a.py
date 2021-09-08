def med3(a, b, c):
    # a, b, c의 중앙값을 구하여 반환
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or ( a < b and c > b):
        return b
    return c

print('세 정수의 중앙값 계산')
a = int(input('정수 a 값 입력: '))
b = int(input('정수 b 값 입력: '))
c = int(input('정수 c 값 입력: '))

print(f'중앙값 {med3(a, b, c)}')
