# 1. 아이디어
# - DP이용
# - 점화식: An = max(An, An + An-1) 이용
#   -->여기에서 An-1은 memorization 이용!
#   An-1에 처음부터 An-1까지의 합을 저장해놓음!
#   그러면 일일이 합할필요없이 현재값과 이전값만 더하면 합계산 가능
# - max사용 이유는 
#   현재까지 더한 모든값이 현재값보다 작으면 필요가 없기 때문

import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int,input().split()))

for i in range(1, n):
    m[i] = max(m[i], m[i] + m[i-1])
    
print(max(m))