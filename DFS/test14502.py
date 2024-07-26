# n, m = map(int, input().split)
# graph = [list(map(int, input().split())) for _ in range(n)]
# temp = [[0]*m for _ in range(n)]

# dy = [0, 1, 0, -1]
# dx = [1, 0, -1, 0]

# # DFS로 바이러스 확산 함수
# def virus(y, x):
#     for k in range(4):
#         ny = y + dy[k]
#         nx = x + dx[k]
#         if 0<=ny<n and 0<=nx<m:
#             if temp[ny][nx] == 0:
#                 temp[ny][nx] = 2
#                 virus(ny,nx)
                
# # 현재 맵에서 안전 영역의 크기 계산
# def get_score():
#     score = 0
#     for j in range(n):
#         for i in range(m):