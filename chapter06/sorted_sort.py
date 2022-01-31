# sorted()함수를 사용하여 정렬

import numpy


print('sorted()함수 사용하여 정렬')
num = int(input('원소 수 입력: '))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

# 배열x 오름차순 정렬
x = sorted(x)
print('오름차순으로 정렬')
for i in range(num):
    print(f'x[{i}] = {x[i]}')

x = sorted(x, reverse = True)
print('내림차순으로 정렬')
for i in range(num):
    print(f'x[{i}] = {x[i]}')