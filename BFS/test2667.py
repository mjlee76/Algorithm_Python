# from collections import deque

# n = int(input())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int,input())))
# chk = [[False]*n for _ in range(n)]

# dy = [0, 1, 0 ,-1]
# dx = [1, 0, -1, 0]

# def bfs(y, x):
#     q = deque()
#     q.append((y,x))
#     size = 0
#     count = 1
    
#     while q:
#         ey, ex = q.popleft()
#         for k in range(4):
#             ny = ey + dy[k]
#             nx = ex + dx[k]
#             if 0<=ny<n and 0<=nx<n:
#                 if graph[ny][nx]==1 and chk[ny][nx]==False:
#                     chk[ny][nx] = True
#                     size += 1
#                     q.append((ny,nx))
#     return size

# cnt = []
# for j in range(n):
#     for i in range(n):
#         if graph[j][i] == 1 and chk[j][i] == False:
#             cnt.append(bfs(j, i))

# cnt.sort()
# print(len(cnt))
# for i in range (len(cnt)):
#     print(cnt[i])
            
    
