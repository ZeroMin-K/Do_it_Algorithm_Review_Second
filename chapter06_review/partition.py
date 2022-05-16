# 배열을 두그룹으로 나누기

from typing import MutableSequence

def partition(a: MutableSequence) -> None:
    # 배열을 나누어 출력
    n = len(a)
    pl = 0      # 왼쪽 커서
    pr = n - 1  # 오른쪽 커서
    x = a[n//2] # 피벗

    while pl <= pr:
        while a[pl] < x:
            pl += 1
        while a[pr] > x:
            pr -= 1
        
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1