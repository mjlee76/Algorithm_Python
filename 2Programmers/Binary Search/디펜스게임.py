def solution(n, k, enemy):
    
    answer = 0
    st = 0
    en = len(enemy)
    
    while st <= en:
        mid = (st + en) // 2
        round = enemy[:mid]
            
        round.sort(reverse = True)
        remaining = round[k:]
        
        total = sum(remaining)
        if total <= n:
            answer = mid
            st = mid + 1
        else: 
            en = mid - 1
                        
    return answer