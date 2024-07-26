# 1. 아이디어
# - 요청예산 합이 총 예산보다 작으면 제일큰 요청예산 출력
# - 요청예산 합이 총 예산보다 크면
#   => 시작: 0, 끝: 최대요청예산 의 mid구해서
#   => for 돌면서 mid와 비교
#   => mid가 크면 --> sum에 값 더하고
#   => mid가 작으면 --> sum에 mid만 더해서
  
#   => sum이 총예산보다 작거나 같으면 --> start를 mid+1
#   => sum이 총예산보다 크면 --> end를 mid-1

import sys
input = sys.stdin.readline

N = int(input())
budget_req_list = list(map(int, input().split()))
budget = int(input())
st, en = 0, max(budget_req_list)

while st <= en:
    sum = 0
    mid = (st+en)//2
    
    for each_budget_req in budget_req_list:
        if each_budget_req <= mid:
            sum += each_budget_req
        else:
            sum += mid
        
    if sum <= budget:
        st = mid + 1
    else: 
        en = mid - 1
        
print(en)
        

    