print('a부터 b까지 정수의 합 계산')
a = int(input('정수 a 입력: '))
b = int(input('정수 b 입력: '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b +1):
    sum += i

print(f'{a}부터 {b}까지 정수의 합: {sum}')
