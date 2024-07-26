import sys
input = sys.stdin.readline

N, X = map(int,input().split())
visitor = list(map(int,input().split()))
result = []
# X개를 더해주기
sum = 0
for i in range(X):
    sum += visitor[i]
    result.append(sum)
    
# 다음 인덱스 더해주고, 이전 인덱스 빼기
for i in range(X, N):
    sum += visitor[i]
    sum -= visitor[i-X]
    result.append(sum)
    
maxv = max(result)
count = 0
for i in result:
    if i == maxv:
        count += 1

if maxv == 0:
    print("SAD")
else: 
    print(f"{maxv}\n{count}")