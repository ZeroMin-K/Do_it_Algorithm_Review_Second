# 양의 정수 n의 팩토리얼 계산

def factorial(n: int) -> int:
    # 양의 정수 n의 팩토리얼값을 재귀적으로 계산
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1