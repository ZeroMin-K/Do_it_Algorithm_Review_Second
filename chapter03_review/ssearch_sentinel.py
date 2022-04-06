# 선형 검색 알고리즘을 보초법으로 수정

from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    # 시퀀스 seq에서 key와 일치하는 원소를 선형검색(보초법)
    a = copy.deepcopy(seq)      # seq복사 
    a.append(key)               # 보초 key 추가

    i = 0
    while True: 
        if a[i] == key:
            break
        i += 1

    return -1 if i == len(seq) else i