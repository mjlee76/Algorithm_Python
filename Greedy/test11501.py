import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    m = list(map(int,input().split()))
    m.reverse()
    max = m[0]
    sum = 0
    
    for i in range(1, N):
        if max < m[i]:
            max = m[i]
            continue
        sum += max-m[i]
    
    print(sum)
            
    
    



            
        
        

