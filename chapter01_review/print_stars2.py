print('* 출력')

n = int(input('몇개 출력?:'))
w = int(input('몇개마다 줄바꿈? : '))

for _ in range(n//w):
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)
