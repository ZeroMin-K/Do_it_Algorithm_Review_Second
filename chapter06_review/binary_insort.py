from typing import MutableSequence
import bisect

def binary_insertion_sort(a: MutableSequence) -> None:
    # 이진삽입 정렬
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)