def solution(players, callings):
    
    players_dict = {player:idx for idx,player in enumerate(players)}
    
    for call in callings:
        idx = players_dict[call]
        
        # 딕셔너리로 call의 idx를 찾아 player의 위치를 swap
        players[idx], players[idx-1] = players[idx-1], players[idx]
        
        # 딕셔너리 업데이트
        players_dict[players[idx]] = idx
        players_dict[players[idx-1]] = idx-1
    
    return players


# 이름 불린사람이 앞사람과 자리교체해서 이름 다 불리고난 다음 사람 순서출력 문제

# 인덱스로 접근해서 위치 바꾸면 O(N)시간복잡도 발생 -> 시간초과

# 딕셔너리 이용({가:0, 나:1, 다:2})

# 딕셔너리는 해시테이블 기반이라 특정 키값을 해시함수에 넣어서 해당 메모리 주소로 바로 찾아감!

# 위 코드에서 플레이어의 위치를 바꿨으면 딕셔너리도 업데이트 해줌줌 