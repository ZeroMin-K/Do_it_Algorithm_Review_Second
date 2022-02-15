# 힙 정렬 알고리즘 구현(heapq.push, heapq.pop 사용)

import heapq
from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    # 힙 정렬
    heap = []

    for i in a:
        heapq.heappush(heap, i)
    for i in range(len(a)):
        a[i] = heapq.heappop(heap)