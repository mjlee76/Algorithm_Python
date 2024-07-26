# 1. 아이디어
# - 한점 시작, 모든 거리 : 다익스트라 사용
# - 간선, 인접리스트 저장
# - 거리배열 무한대 초기화
# - 시작점 : 거리배열 0, 힙에 넣어주기
# - 1에서 시작해 임의의 두정점 지나서(v1 -> v2) or (v2 -> v1) 
#   마지막 V까지 최단거리 구하기
#   - 1에서 v1까지 최단 + v1에서 v2까지 최단 + v2에서 V까지 최단
#   - 1에서 v2까지 최단 + v2에서 v1까지 최단 + v1에서 V까지 최단
#       - 시작점을 넣어 각 정점까지의 최단거리 구하는 배열 만드는 함수생성해
#       - 위의 각 값을 구하기
# - 힙에서 빼면서 다음수행
#     - 최신값인지 먼저 확인
#     - 간선을 타고간 비용이 더 작으면 갱신
    
# 2. 시간복잡도
# - 다익스트라 : O(ElgV)
# - E : 2e5
# - V : 8e2, lgV ~= 10
# - ElgV ~= 2e6 -> 2억보다 작음

import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())

edge = [[] for _ in range(V+1)]

for i in range(E):
    a, b, c = map(int,input().split())
    edge[a].append([c, b])
    edge[b].append([c, a])
    
def dijkstra(start):
    dist = [INF] * (V+1)
    heap = []
    dist[start] = 0
    heapq.heappush(heap, (0, start))
    
    while heap:
        ew, ev = heapq.heappop(heap)
        if ew != dist[ev]:
            continue
        for nw, nv in edge[ev]:
            if dist[nv] > dist[ev] + nw:
                dist[nv] = dist[ev] + nw
                heapq.heappush(heap, (dist[nv], nv))

    return dist

v1, v2 = map(int, input().split())
dist_start1 = dijkstra(1)
dist_startv1 = dijkstra(v1)
dist_startv2 = dijkstra(v2)

v1_to_v2_path = dist_start1[v1] + dist_startv1[v2] + dist_startv2[V]
v2_to_v1_path = dist_start1[v2] + dist_startv2[v1] + dist_startv1[V]

result = min(v1_to_v2_path, v2_to_v1_path)
result = min(v1_to_v2_path, v2_to_v1_path)
if result < INF:
    print(result)
else: print(-1)
    
    