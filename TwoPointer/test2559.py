# 1. 아이디어
# - 투포인터를 사용
# - 처음에 k개의 값을 구함
# - for문: 다음 인덱스의 값을 더하고, 앞의 값을 뺌
# - 이때 최대값을 갱신

# 2. 시간복잡도
# - 숫자 개수만큼 for : O(N) = 1e5(십만) < 2억 

# 3. 자료구조
# - 전체 정수 배열: int[] 
#   @ -100 ~ 100 인 모든수 => int가능 (파이썬)
# - k개를 합한 수: int[]
#   @ 100 * 1e5 = 1e7 => int가능 (파이썬)
# - 최대값 : int

import sys
input = sys.stdin.readline

N, K = map(int,input().split())
nums = list(map(int,input().split()))

# K개를 더해주기
sum = 0
for i in range(K):
    sum += nums[i]
maxv = sum

# 다음인덱스 더해주고, 이전인덱스 빼주기
for i in range(K, N):
    sum += nums[i]
    sum -= nums[i-K]
    maxv = max(maxv, sum)
    
print(maxv)