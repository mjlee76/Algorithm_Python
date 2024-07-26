# 1. 아이디어
# - MST 기본문제, 외우기
# - 간선을 인접리스트에 집어넣기
# - 힙에 시작점 넣기
# - 힙이 빌때까지 다음작업을 반복
#     - 힙의 최소값 꺼내서, 해당 노드 방문 안했다면
#         - 방문표시, 해당 비용 추가, 연결된 간선들 힙에 넣어주기
        
# 2. 시간복잡도
# - MST : O(ElgE)

# 3. 자료구조
# - 간선 저장 되는 인접리스트 : (무게, 노드번호)
# - 힙 : (무게, 노드번호)
# - 방문 여부: bool[]
# - MST 결과값 : int

import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())

# 인접리스트 생성
# V+1 : 인덱스 번호를 편하게 사용하기위해
edge = [[] for _ in range(V+1)]

# 방문여부 확인 리스트(chk) 생성
chk = [False] * (V+1)

# 결과값 생성
rs = 0

for i in range(E):
    a, b, c = map(int, input().split())
    # 인접리스트에 간선비용과 연결된노드 추가
    # MST는 edge가 양방향이기 때문에 양방향 추가
    edge[a].append([c,b])
    edge[b].append([c,a])

print(edge)
# heap에 시작점 넣기 
heap = [[0,1]]

while heap:
    #heapq:라이브러리 -> import필요
    w, each_node = heapq.heappop(heap)
    if chk[each_node] == False:
        chk[each_node] = True
        rs += w
        for next_edge in edge[each_node]:
            # next_edge[1]인 이유:
            # next_edge[0]:무게값이고
            # next_edge[1]:노드번호 이기때문
            if chk[next_edge[1]] == False:
                heapq.heappush(heap, next_edge)

print(rs)
    
    