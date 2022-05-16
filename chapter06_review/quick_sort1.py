from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    #a[left] ~ a[right] 퀵정렬
    pl = left
    pr = right
    x = a[(left + right) // 2]

    while pl <= pr:
        while a[pl] < x:
            pl += 1
        while a[pr] > x:
            pr -= 1

        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: 
        qsort(a, left, pr)
    if pl < right:
        qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    # 퀵 정렬
    qsort(a, 0, len(a) -1)