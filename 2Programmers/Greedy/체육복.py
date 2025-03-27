def solution(n, lost, reserve):
    
    common = []
    for num in lost:
        if num in reserve:
            common.append(num)
    
    for num in common:
        lost.remove(num)
        reserve.remove(num)
        
    count = n - len(lost)
    lost.sort()
    reserve.sort()
    
    for num in lost:
        if (num-1) in reserve:
            count += 1
            reserve.remove(num-1)
        elif (num+1) in reserve:
            count += 1
            reserve.remove(num+1)
    
    return count