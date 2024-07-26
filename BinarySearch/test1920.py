#  1. 아이디어
#  - N개의 숫자를 정렬
#  - M개를 for 돌면서, 이진탐색
#  - 이진탐색 안에서 마지막에 데이터 찾으면 1출력, 아니면 0출력
 
#  2. 시간복잡도
#  - N개 입력값 정렬 = O(NlogN)
#  - M개를 N개중에서 탐색 = O(M * lgN)
#  - 총합 : O((N+M)lgN) > 가능
 
#  3. 자료구조
#  - N개 숫자 : int[]
#  - M개 숫자 : int[]

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

nums.sort() # 정렬해야 이진탐색 가능

def search(st, en, target):
    if st == en:
        # 정렬된 수중 target과 같은값이 없을수도 있으므로
        if nums[st] == target: 
            print(1)
        else: 
            print(0)
        return
    
    mid = (st + en) // 2
    if nums[mid] < target:
        search(mid+1, en, target)
    else:
        search(st, mid, target)

for each_target in target_list:
    search(0, N-1, each_target)
    
