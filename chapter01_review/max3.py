print('세정수 최댓값 계산')
a = int(input('정수 a값 입력: '))
b = int(input('정수 b값 입력: '))
c = int(input("정수 c값 입력: "))

maximum = a
if b > maximum:
    maximum = b
if c > maximum:
    maxinum = c

print(f'최댓값 {maximum}')
