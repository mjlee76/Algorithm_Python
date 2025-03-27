def solution(n, w, num):
    answer = 0
    # 높이
    h = n//w + 1
    # 박스 번호
    x = 1 
    
    storage = []
    
    for i in range(h):
        temp = []
        for j in range(w):
            if x <= n:
                temp.append(x)
                x += 1
            else:
                temp.append(0)
        
        if i % 2 == 0:
            storage.append(temp)
        else:
            temp.reverse()
            storage.append(temp)
            
    for i in range(len(storage)):
        for j in range(len(storage[0])):
            if storage[i][j] == num:
                d = i
                while d < h:
                    if storage[d][j] != 0: # 상자 존재하면 +1
                        answer += 1
                        d += 1
                    else:                  # 상자 없을때(0일때) break
                        break
            
    return answer