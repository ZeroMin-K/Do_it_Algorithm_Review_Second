# 왼쪽 아래가 직각인 이등변 삼각형으로 * 출력

print('왼쪽 아래가 직각인 이등변 삼각형 출력')
n = int(input('짧은 변의 길이 출력: '))

for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()
