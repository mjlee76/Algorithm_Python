def solution(n, times):
    answer = 0
    
    st = 1
    en = max(times) * n
    
    while st <= en:
        mid = (st + en) // 2
        people = 0
        
        for time in times:
            people += mid // time
            
            if people >= n:
                break
        
        if people >= n:
            answer = mid
            en = mid - 1
        else:
            st = mid + 1
            
    return answer