# 버블 정렬 알고리즘 구현(알고리즘 개선2)

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    # 버블 정렬
    n = len(a)
    k = 0
    while k < n-1:
        last = n - 1
        for j in range(n-1, k, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        k = last