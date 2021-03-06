# 고정길이 큐 클래스(FixedQueue) 사용

from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Menu', ['인큐', '디큐', '피크', '검색', '덤프', '종료'])

def select_menu() -> Menu:
    # 메뉴 선택
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

q = FixedQueue(64)

while True:
    print(f'현재 데이터 개수: {len(q)} / {q.capacity} ')
    menu = select_menu()

    if menu == Menu.인큐:
        x = int(input('인큐할 데이터 입력: '))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print('큐가 가득 참')

    elif menu == Menu.디큐:
        try:
            x = q.deque()
            print(f'디큐한 데이터: {x}')
        except FixedQueue.Empty:
            print('큐 비어있음')

    elif menu == Menu.피크:
        try:
            x = q.peek()
            print(f'피크한 데이터 {x}')
        except FixedQueue.Empty:
            print('큐 비어있음')

    elif menu == Menu.검색:
        x = int(input('검색할 값 입력: '))
        if x in q:
            print(f'{q.count(x)} 개 포함, 맨 앞의 위치 {q.find(x)}')
        else:
            print('검색할 찾을 수 없음')
    
    elif menu == Menu.덤프:
        q.dump()

    else:
        break