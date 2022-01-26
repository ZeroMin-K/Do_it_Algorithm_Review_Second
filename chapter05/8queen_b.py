# 각 ㅕㅇㄹ에 퀸을 1개 배치하는 좋바을 재귀적으로 나열

pos = [0] * 8       # 각 열에서 퀸의 위치 출력

def put() -> None:
    # 각 열에 배치한 퀸의 위치 출력
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:
    # i열에 퀸 배치
    for j in range(8):
        pos[i] = j      # 퀸을 j행에 배치
        if i == 7:      # 모든 열에 퀸 배치 종료
            put()
        else:
            set(i +1)   # 다음열에 퀸 배치

set(0)