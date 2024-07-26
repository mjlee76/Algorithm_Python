# # 1. 아이디어
# # 2중 for문: 값==1 && 방문x -> BFS

# # 2. 시간복잡도
# # BFS => O(V+E)
# # V=n*m
# # E=v*4
# # O= 5(n*m) =50000 가능

# # 3. 자료구조
# # -그래프지도: int[][]
# # -방문: bool[][]
# # - Queue(BFS) 



# import sys
# from collections import deque
# input = sys.stdin.readline

# N,M = map(int, input().split())
# map = [list(int(char) for char in input().strip()) for _ in range(N)]
# # chk = [[False]*m for _ in range(n)]


# def bfs(y,x):
#     dy = [0,1,0,-1]
#     dx = [1,0,-1,0]
    
#     q = deque()
#     q.append((y,x))
#     # cnt = 1
#     # q = [(y,x)]
#     while q:
#         y, x = q.pop(0)
#         for k in range(4):
#             ny = ey + dy[k]
#             nx = ex + dx[k]
#             if 0<=ny<N and 0<=nx<M:
#                 if map[ny][nx]==1: #and chk[ny][nx]==False:
#                     #chk[ny][nx]=True
#                     #cnt += 1
#                     map[ny][nx] = map[y][x] + 1
#                     q.append((ny,nx))
#     # return cnt
#     return map[M-1][N-1]
                    
# print(bfs(0,0))
# print(map)

# # minv = float('inf')
# # for j in range(n):
# #     for i in range(m):
# #         if map[j][i] == 1 and chk[j][i] == False:
# #             chk[j][i] = True
# #             result = bfs(j, i)
# #             for k in chk:
# #                 print(k)
# #             minv = min(minv, result)
# #             print(result)
            
# # print(minv)
