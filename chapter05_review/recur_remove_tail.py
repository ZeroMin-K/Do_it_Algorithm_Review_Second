# 비재귀적으로 재귀함수 구현(꼬리 재귀 제거)

def recur(n: int) -> int:
    # 꼬리 재귀를 제거한 recur() 함수
    while n > 0:
        recur(n-1)
        print(n)
        n = n - 2 
    