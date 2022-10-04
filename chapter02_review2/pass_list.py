# 리스트에서 임의의 원소값 업데이트

def change(lst, idx, val):
    # list[idx]의 값을 val로 업데이트
    lst[idx] = val

x = [11, 22, 33, 44, 55]
print('x=', x)

index = int(input('업데이트할 인덱스: '))
value = int(input('새로운 값 입력: '))

change(x, index, value)
print(f'x = {x}')