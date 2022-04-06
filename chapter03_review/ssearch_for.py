# for문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    # 시뭔스a에서 key와 값이 같은 원소를 선형 검색

    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1