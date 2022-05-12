from typing import MutableSequence

def binary_insertion_sort(a: MutableSequence) -> None:
    # 이진 삽입 정렬
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0                  # 검색 범위의 맨 앞 원소 인덱스 
        pr = i - 1              # 검색 범위의 맨 끝 원소 인덱스 

        while True:
            pc = (pl + pr) // 2         # 검색 범위의 가운데 원소 인덱스
            if a[pc] == key:            # 검색 성공
                break
            elif a[pc] < key:
                pl = pc + 1             # 검색 범위를 뒤쪽 절반으로 좁힘
            else:
                pr = pc - 1             # 검색 범위를 앞쪽 절반으로 좁힘
            if pl > pr:
                break
        
        pd = pc + 1 if pl <= pr else pr + 1     # 삽입 해야할 위치의 인덱스 

        for j in range(i, pd, -1):
            a[j] = a[j-1]   
        a[pd] = key 