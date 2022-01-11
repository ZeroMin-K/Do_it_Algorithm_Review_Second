print('1부터 n까지 정수의 합 계산')

while True:
    n = int(input('n값 입력: '))
    if n > 0:
        break
sum = 0
i = 1

for i in range(1, n+1):
    sum += i
    i += 1

print(f'1부터 {n}까지 정수의 합 {sum}')
