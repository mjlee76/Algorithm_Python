def dfs(graph, v , visited):
    visited[v] = True  
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def solution(n, computers):
    count = 0
    visited = [False] * (n + 1)
    graph = [[] for _ in range(n+1)]
    for i in range(0, n):
        for j in range(0, n):
            if computers[i][j] == 1 and i != j:
                graph[i+1].append(j+1)
    
    for i in range(1, n+1):
        if visited[i] == False:
            dfs(graph, i, visited)
            count += 1
    return count

# DFS 이용해서 풀기

# computers를 인접리스트 형식(graph)으로 보기쉽게 변환함. 이때 i != j 조건을 줘서 i번노드의 인접리스트에 같은 i가 들어가지 않게하기.

# 재귀를 이용해서 dfs함수 선언

# 본 함수에서 반복문을 돌며 방문하지 않은 노드를 발견할때 마다 dfs 실행하여 방문 처리하고, count를 1씩 올림