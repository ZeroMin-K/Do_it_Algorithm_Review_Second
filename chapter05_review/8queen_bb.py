# 행과 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열

pos = [0] * 8       # 각 열에서 퀸의 위치
flag = [False] * 8      # 각 행에 퀸을 배치햇는지 체크

def put() -> None:
    # 각 열에 배치한 퀸의 위치 출력
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:
    # i열에 알맞은 위치에 퀸배치
    for j in range(8):
        if not flag[j]:         # j행에 퀸을 배치하지 않았으면
            pos[i] = j          # 퀸을 j행에 배치
            if i== 7:           # 모든 열에 퀸 배치 완료
                put()
            else:
                flag[j] = True
                set(i+1)        # 다음열에 퀸 배치
                flag[j] = False

set(0)
