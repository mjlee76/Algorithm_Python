def dfs(adj, node, visited):
    visited[node] = True
    count = 1
    for i in adj[node]:
        if visited[i] == False:
            count += dfs(adj, i, visited)
    
    return count
        
        
def solution(n, wires):
    
    adj = [[] for _ in range(n+1)]
    for a, b in wires:
        adj[a].append(b)
        adj[b].append(a)
    #print(f'adj:{adj}')

    min_diff = n-1
    for a, b in wires:
        adj[a].remove(b)
        adj[b].remove(a)
        #print(f'remove:({a},{b})')
        visited = [False] * (n+1)
        wire1 = dfs(adj, a, visited)
        wire2 = n - wire1
        #print(f'[구역1: {wire1}, 구역2: {wire2}]')
        if min_diff > abs(wire1-wire2):
            min_diff = abs(wire1-wire2)
        adj[a].append(b)
        adj[b].append(a)
    
    return min_diff

# 전력망 wires가 주어질때 하나의 간선을 무작위로 끊어 나누어진 두 전력망의 노드개수의 최소값을 구하는 문제

# wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]가 이런식으로 주어지고, 노드의 개수 n 이 주어짐

# wires를 돌면서 인접 리스트를 만듬 ->
# adj[1] = [3]
# adj[2] = [3]
# adj[3] = [1, 2, 4]
# adj[4] = [3, 5, 6, 7]
# adj[5] = [4]
# adj[6] = [4]
# adj[7] = [4, 8, 9]
# adj[8] = [7]
# adj[9] = [7]

# 이렇게 만들어지면 다시 wires를 돌면서 하나씩 간선을 끊어봄(remove사용)

# 끊어진 인접 리스트와 탐색 시작할 노드 a, 방문여부(visited)를 dfs로 구현

# dfs함수 -> 처음 노드를 방문처리후 해당 노드와 연결된 노드를 탐색함 -> 방문하지 않은 연결된 노드가 있을 시 재귀를 이용해 count를 늘려줌.

# 이렇게 되면 나눠진 전력망 중 한개의 노드 갯수가 나오는데 이거랑 전체 노드수의 차를 계산해 min_diff보다 작다면 저장

# 다음 간선 끊기 작업에 들어가기전 다시 append를 통해 원래 인접리스트(adj)로 복구

# 최소값 min_diff를 리턴