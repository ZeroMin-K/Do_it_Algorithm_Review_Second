# while문으로 작성한 선형 검색알고리즘

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    # 시퀀스a에서 key와 값이 같은 원소를 선형 검색(while문)

    i = 0

    while True:
        if i == len(a):
            return -1       # 검색 실패
        if a[i] == key:
            return i        # 검색 성공 - 현재 검사한 배열의 인덱스 반환
        i += 1