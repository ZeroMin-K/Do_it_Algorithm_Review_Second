# 10 진수 정수값을 입력받아 2 ~ 36 진수로 변환하여 출력

def card_conv(x: int, r: int) -> str:
    # 정수값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열 반환

    d = ''       # 변환 후 문자열
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x % r]       # 해당하는 문자 꺼내 결합
        x //= r
        
    return d[::-1]              # 역순으로 반환 