# from collections import deque

# v = int(input())
# e = int(input())

# graph = [[] for _ in range(v+1)] #그래프 초기화
# visited = [ False for _ in range(v+1)]

# for _ in range(e):
#     a, b = map(int, input().split())
#     # graph[a] = graph[a]+[b]
#     # graph[b] = graph[b]+[a]
    
#     graph[a].append(b)
#     graph[b].append(a)

# def bfs(x):
#     q = deque([x])
#     visited[x] = True
#     count = 0
#     while q:
#         node = q.popleft()
#         for i in graph[node]:
#             if not visited[i]:
#                 visited[i] = True
#                 q.append(i)
#                 count += 1
#     return count

# print(bfs(1))

# # popleft() 개념
# a = deque([1, 2, 3, 4, 5])
# print(a)

# a.popleft()
# print(a)

# # 출력
# deque([1, 2, 3, 4, 5])
# deque([2, 3, 4, 5])

    
