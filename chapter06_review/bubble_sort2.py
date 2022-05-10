from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    # 버블 정렬
    n = len(a)
    for i in range(n-1):
        exchng = 0      # 패스에서 교환횟수
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j -1 ], a[j] = a[j], a[j-1]
                exchng += 1
        if exchng == 0:
            break