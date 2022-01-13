from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]

    return maximum

if __name__ == '__main__':
    print('배열의 최댓값 계산')
    num = int(input('원소 수 입력: '))
    x = [None] * num 

    for i in range(num):
        x[i] = int(input(f'x[{i}]값 입력: '))

    print(f'최댓값 {max_of(x)}')
