from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    # 버블정렬(스캔범위제한)
    n = len(a)
    k = 0
    while k < n-1:
        last = n - 1
        for j in range(n-1, k, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        k = last 