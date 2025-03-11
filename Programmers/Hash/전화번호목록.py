def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)+1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
        else:
            return True
        
# phone_book의 전화번호 중 어떤 번호가 다른번호의 접두사일 경우(ex: 119는 1199345에 접두사로 존재) -> false 아니면 true

# phone_book을 정렬하여 앞과 뒤를 비교하면 쉬움.

# 비교할때는 접두사인지 찾는것이므로 startswith함수 이용  *참고: 접미사는 endswith()사용

def solution(phone_book):
    phone_dict = {num: True for num in phone_book}
    
    for num in phone_book:
        prefix = ""
        for digit in num:
            prefix += digit
            if prefix in phone_dict and prefix != num: # phone_dict을 탐색해야함(해시탐색:O(1))
                return False                           # phone_book을 탐색하면(일일이탐색:O(N))
    
    return True

# 이건 더 빠른 방법인 해시(딕셔너리) 이용

# phone_dict -> 전화번호->key, True->값 으로 하는 dictionary 선언

# 전화번호를 분해하여 prefix에 한개씩 저장하면서 phone_dict에 있고 & prefix가 num이 아니라면 return false