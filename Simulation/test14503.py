# 1. 아이디어
# - 특정 조건 만족하는 한 계속이동 => While (조건x -> break)
# - 4방향 탐색 먼저 수행(for) -> 빈칸있을 경우 이동
# - 4방향 탐색 안될 경우 -> 뒤로 한칸가서 반복(밑으로)
# - 후진 불가능 할 경우 -> 종료

# 2. 시간복잡도
# - while문 최대: N * M * 4(4방향: 상수라 생략가능)
# - 각 칸에서 4방향 연산 수행

# 3. 자료구조
# - map : int[][]
#   ==> 0 : 청소X , 1 : 벽 , 2 : 청소O
# - 내 위치, 방향 : int(y), int(x), int(d:방향), int(count)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
y, x, d = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(N)]
cnt = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while 1:
    if map[y][x]==0:
        map[y][x] = 2
        cnt += 1
        
    # switch로 인해 4방향중 청소할곳이 없으면 true로 안바뀜으로써
    # 조건부여 가능 
    switch = False
    # 4방향 탐색
    for i in range(1, 5):
        ny = y + dy[d-i]
        nx = x + dx[d-i]
        if 0<=ny<N and 0<=nx<M:
            if map[ny][nx] == 0: 
                # 그 방향으로 회전한 다음 한 칸을 전진후 청소 진행
                d = (d-i+4)%4 # 이건 배열크기를 초과하는 음수값 방향을 다시 양수로 변환(@@외우자!@@)
                y = ny
                x = nx
                switch = True
                break # break뒤에 28,29라인 실행(청소진행하고 cnt += 1 진행)
    
    # 4방향 모두 있지 않은경우
    if switch == False:
        # 뒤쪽이 막혀있는지 확인
        ny = y - dy[d] # 뒤로 이동한 좌표
        nx = x - dx[d] # 뒤로 이동한 좌표
        if 0<=ny<N and 0<=nx<M:
            #벽이라면
            if map[ny][nx] == 1:
                break # 탐색 종료(while문 빠져나가기)
            else:
                y = ny
                x = nx
        # 범위 벗어난 경우도 종료
        else:
            break

print(cnt)
        
        
            
            