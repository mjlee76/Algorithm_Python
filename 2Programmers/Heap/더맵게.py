import heapq

def solution(scoville, K):
    count = 0
    
    heapq.heapify(scoville)
    
    while len(scoville)>1:
        first = heapq.heappop(scoville)
        
        if first < K:
            count += 1
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, first + (second * 2))
        else:
            break
            
    if scoville[0] < K:
        return -1
    else:
        return count
    

# 우선순위 힙을 이용 -> O(logN), 최악의 경우: O(NlogN)


# 반환할 결과값 count를 선언하고 최소힙 기능을 가지고 있는 heapq Module을 사용하여 스코빌 지수를 힙의 형태로 만들어줍니다.
 
 
# 스코빌 지수가 1개 남을 때까지 while loop을 돌려줍니다.
 
 
# 3. '가장 맵지 않은 음식의 스코빌 지수'를 heappop 함수를 통해 꺼낸 뒤 first 변수에 담아줍니다.
 
 
# first 변수에 담긴 값이 K 이상이면 종료합니다. 그렇지 않으면 5번으로 넘어갑니다.
 
 
# 섞은 횟수를 1 증가시키고, '두 번째로 맵지 않은 음식의 스코빌 지수'를 꺼내 second 변수에 담아줍니다.
 
 
# '특별한 방법으로 섞기'를 연산하고 다시 스코빌 지수에 힙의 형태로 담아줍니다. 이후 다시 3번으로 이동합니다.


# scoville의 최소값이 K보다 작을 경우 -1, 아닐 경우 count 값을 리턴해줍니다.