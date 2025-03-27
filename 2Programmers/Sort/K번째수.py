def find(array, st, en, tar):
    
    temp = []
    for i in range(st-1, en):
        temp.append(array[i])
        
    temp.sort()
    
    return temp[tar-1]

def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        st = commands[i][0]
        en = commands[i][1]
        tar = commands[i][2]
        answer.append(find(array, st, en, tar))
    
    return answer