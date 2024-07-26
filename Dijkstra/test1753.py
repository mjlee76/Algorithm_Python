# 1. 아이디어
# - 한점시작, 모든거리 : 다익스트라 사용
# - 간선, 인접리스트 저장
# - 거리배열 무한대 초기화
# - 시작점 : 거리배열 0, 힙에 넣어주기
# - 힙에서 빼면서 다음의 것들 수행
#     - 최신값인지 먼저 확인
#     - 간선을 타고간 비용이 더 작으면 갱신
    
# 2. 시간복잡도
# - 다익스트라 : O(ElgV)
#     - E : 3e5
#     - V : 2e4, lgV ~= 20(큰걸로 선택)  #2^10 ~= 10^3, 2^20 ~= 10^6
#     - ElgV = 6e6 -> 2억보다 작음
    
# 3. 변수
# - 힙 : (비용, 노드번호)
# - 거리 배열 : 비용 : int[]
# - 간선 저장, 인접리스트 : (비용, 노드번호)[]

import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
K = int(input())

# 인접 리스트 생성
# edge[0]을 빈상태로 추가하여 1번노드가 edge[1]이 되어
# 표현이 쉽도록 하기 위해 (V+1)개 만큼 생성
edge = [ [] for _ in range(V+1) ]

# 거리 배열 생성
dist = [INF] * (V+1)

for i in range(E):
    u, v, w = map(int, input().split())
    edge[u].append([w, v])
    
# 시작점 초기화
dist[K] = 0
heap = [[0,K]]

while heap:
    ew, ev = heapq.heappop(heap)
    if dist[ev] != ew: continue
    for nw, nv in edge[ev]:
        # 현재 nv까지의 비용보다 
        # ew(현재ev까지의 비용) +nw(nv까지 추가될 새비용)
        # 이 작다면 갱신
        if dist[nv] > ew + nw:
            dist[nv] = ew + nw
            heapq.heappush(heap, [dist[nv], nv])

for i in range(1, V+1):
    if dist[i] == INF: print("INF")
    else: print(dist[i])
    
