# 유클리드 호제법으로 최대공약수 계산

def gcd(x: int, y: int) -> int:
    # 정수값 x, y의 최대 공약수 반환
    if y == 0:
        return x
    else:
        return gcd(y, x % y)