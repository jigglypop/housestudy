# 3
# 5
# 13101
# 10101
# 10101
# 10101
# 10021
# 5
# 10031
# 10111
# 10101
# 10101
# 12001
# 5
# 00013
# 01110
# 21000
# 01111
# 00000

def DFS(sy, sx):
    
    global r
    # 변수선언부

    if M[sy][sx] == 3:
        r = 1
        return
    # 종료조건부   
    
    Q.append((sy, sx))
    for i in range(4):
        ny = sy + dy[i]
        nx = sx + dx[i]
        if 0 <= ny < N and 0 <= nx < N and M[ny][nx] != 1 and (ny, nx) not in Q:
            DFS(ny, nx)

    # 반복부

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input())) for _ in range(N)]
    # 초기설정


    for y in range(N):
        for x in range(N):
            if M[y][x] == 2:
                sy, sx = y, x   
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    # 시작점 찾기

    Q = []
    r = 0
    DFS(sy, sx)
    print(f'#{tc} {r}')
