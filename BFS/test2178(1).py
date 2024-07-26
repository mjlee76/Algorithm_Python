import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
map = [list(map(int, ' '.join(input().split()))) for _ in range(N)]


dy = [0,1,0,-1]
dx = [1,0,-1,0]

q = deque([(0, 0)])
while q:
    ey, ex = q.popleft()
    for k in range(4):
        ny = ey + dy[k]
        nx = ex + dx[k]
        if 0<=ny<N and 0<=nx<M:
            if map[ny][nx] == 1:
                 q.append((ny, nx))
                 map[ny][nx] = map[ey][ex] + 1
                 
print(map[N-1][M-1])