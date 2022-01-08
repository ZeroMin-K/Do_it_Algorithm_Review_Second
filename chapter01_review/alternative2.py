print('+와 -를 번갈아 출력')
n = int(input('몇 개 출력?: '))

for _ in range(n // 2):
    print('+-', end='')

if n % 2:
    print('+', end='')

print()
