from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    # 셸 정렬 (h * 3 + 1의 수열 사용)
    n = len(a)
    h = 1

    while h < n // 9:
        h = h * 3 + 1

    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 3