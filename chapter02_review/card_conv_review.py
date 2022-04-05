def card_conv(x: int, r: int) -> str:
    # 정수값x를 r진수로 변환한뒤 그 수를 나타내는 문자열로 반환

    d = ''      # 변환후의 문자열
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x % r]       # 해당하는 문자를 꺼내 결합
        x //= r

    return d[::-1]              # 역순으로 반환