# 8퀸 문제 알고리즘 구현

from turtle import Turtle


pos = [0] * 8           # 각 열에 배치한 퀸의 위치
flag_a = [False] * 8    # 각 행에 퀸을 배치했는지 체크
flag_b = [False] * 15   # 대각선 방향(좌하향, 우상향)으로 퀸 배치했는지 체크 
flag_c = [False] * 15   # 대각선 방향(우하향, 좌상샹)으로 퀸 배치햇는지 체크

def put() -> None:
    # 각 열에 배치한 퀸의 위치 출력
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:
    # i열의 알맞은 위치에 퀸 배치
    for j in range(8):
        if (    not flag_a[j]           # j행에 퀸이 배치되지 않았다면
            and not flag_b[i + j]       # 대각선 방향으로 퀸이 배치되지 않았다면
            and not flag_c[i - j + 7]): 
            pos[i] = j
            if i == 7:
                put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                set(i + 1)      # 다음열에 퀸 배치 
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False

set(0)