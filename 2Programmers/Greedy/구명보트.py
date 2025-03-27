def solution(people, limit):
    count = 0
    people.sort()
    left, right = 0, len(people) - 1
    
    while left <= right:
        if people[left] + people[right] <= limit:
            count += 1
            left += 1
            right -= 1
        else:
            count += 1
            right -= 1
    
    return count

# 구명보트에 최대 2명 탈 수 있음 & 무게 제한 있음, 무인도 사람들을 구출할 수 있는 최소 보트 개수 구하기

# people 리스트에는 사람들의 몸무게가 담겨있음

# 제일 무게 작은 사람과 제일 무게 큰 사람을 같이 태울 수 있는가?
 
# while 문으로 left가 right보다 작아지지 않을 때까지 반복문

# 둘다 태울수 있으면(<=limit) count 1 증가 후, left 1 증가 & right 1 감소

# 무게가 초과되면 무거운사람부터 태우기 -> count 1증가 후, right만 1 감소