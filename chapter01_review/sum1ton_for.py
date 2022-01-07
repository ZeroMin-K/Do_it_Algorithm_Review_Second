print('1부터 n까지 정수의 합 계산')
n = int(input('n값 입력: '))

sum = 0
for i in range(1, n+1):
    sum += i

print(f'1부터 {n}까지 정수의 합 {sum}')
