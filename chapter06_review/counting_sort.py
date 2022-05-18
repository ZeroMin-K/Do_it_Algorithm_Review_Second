from typing import MutableSequence

def fsort(a: MutableSequence, max: int) -> None:
    # 도수 정렬(배열의 원소값은 0이상 max이하)
    n = len(a)          # 정렬한 배열 a
    f = [0] * (max + 1)     # 누적 도수 분포표 배열 f
    b = [0] * n             # 작업용 배열b

    for i in range(n):
        f[a[i]] += 1       
    for i in range(1, max+1): 
        f[i] += f[i-1]
    for i in range(n-1, -1, -1): 
        f[a[i]] -= 1
        b[f[a[i]]] = a[i]
    for i in range(n):
        a[i] = b[i]

def counting_sort(a: MutableSequence) -> None:
    # 도수 정렬
    fsort(a, max(a))