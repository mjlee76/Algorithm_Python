# 1. 아이디어
# - 2중 for문 => 값 1 && 방문x => BFS
# - BFS 돌면서 그림개수+1, 최대값을 갱신

# 2. 시간복잡도
# - BFS : O(V+E)
# - V : m*n
# - E : v*4

# 3. 자료구조
# - 그래프 전체 지도 : int[][]
# - 방문 : bool[][]
# - Queue(BFS)

import sys
input = sys.stdin.readline # 입출력 빠르게해주는 코드

n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)] #그래프지도
chk = [[False] * m for _ in range(n)] # 방문횟수

dy = [0,1,0,-1]
dx = [1,0,-1,0]
def bfs(y,x):
    rs = 1 # 넚이
    q = [(y,x)]
    while q:
        ey, ex = q.pop(0)
        for k in range(4): # 동서남북 4가지 방향
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    rs += 1
                    q.append((ny,nx))
    return rs

cnt = 0
maxv = 0
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            # 전체 그림 갯수를 +1
            cnt += 1
            # BFS > 그림 크기를 구해주고
            maxv = max(maxv, bfs(j,i))
            # 최댓값 갱신

print(cnt)
print(maxv)