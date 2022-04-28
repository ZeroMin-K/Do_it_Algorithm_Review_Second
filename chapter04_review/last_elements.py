n = int(input('정수 몇개 저장할지?: '))
a = [None] * n      # 입력받은 값 저장 배열

cnt = 0     # 정수를 입력받은 개수 
while True:
    a[cnt % n] = int(input((f'{cnt + 1} 번째 정수 입력: ')))
    cnt += 1

    retry = input(f'계속? (Y .. yes/ N.. no): ')
    if retry in {'N', 'n'}:
        break

i = cnt - n 
if i < 0: i = 0

while i < cnt:
    print(f'{i + 1} 번째 = {a[i % n]}')
    i += 1