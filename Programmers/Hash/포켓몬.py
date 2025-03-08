def solution(nums):
    
    dict = {}
    for num in nums:
        dict[num] = True  #여기에서 num이 키값값
        
    half = len(nums) / 2
    
    if len(dict) <= half:
        return len(dict)
    else:
        return half
    
# 배열에 저장된 숫자중 반만 가질수 있을때 최대로 가질수있는 숫자 종류 갯수 구하기
    
# 해시(딕셔너리) 이용

# nums = [3,1,2,3]

# 해시(딕셔너리)를 이용해서 총 숫자 종류 갯수 먼저 구함

# dict = {3:True, 1:True, 2:True}
# -> "딕셔너리는 같은 키값을 가지지 못함"을 이용해서 중복을 제거하여 종류갯수를 알수있음

# 반보다 종류갯수가 작으면 종류갯수 return, 많으면 반 return


###### 쉬운 방법 #######

# 해시(딕셔너리)로 배열의 중복제거할필요 없이

# set(nums) => 이게 중복제거된 배열임, {3, 1, 2}가 됨