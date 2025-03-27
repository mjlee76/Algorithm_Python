def solution(participant, completion):
    hash_dict = {}
    sumHash = 0
    
    for part in participant:
        hash_dict[hash(part)] = part
        sumHash += hash(part)
        
    for com in completion:
        sumHash -= hash(com)
        
    return hash_dict[sumHash]

# 참가자(participant) 중 완주하지못한 선수를 찾는 문제(completion->완주자 목록)

# hash_dict을 선언한 후

# 참가자를 for문으로 돌면서 hash(part)로 참가자의 해시값을 키로 사용

# 모든 참가자의 해시값(키)은 중복되지 않음으로 이걸 전부 합함 -> sumHash

# 모든 완주자를 for문으로 돌면서 sumHash에서 hash(com)을 전부 빼주면 완주하지 못한 사람의 해시값만 남음

# return -> hash_dict의 키값이 sumHash인 사람은 완주하지 못한 사람