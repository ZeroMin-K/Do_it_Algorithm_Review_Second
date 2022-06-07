n = int(input('* 몇개 출력?: '))
w = int(input('몇개 마다 줄바꿈?: '))

for i in range(n):
    print('*', end='')
    if i % w == w-1:
        print()

if n % w:
    print()


for _ in range(n // w):
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)