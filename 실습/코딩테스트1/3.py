def solution(n):
    answer = ''
    #3진법
    number_dict ={
        1 : '1',
        2: '2',
        0: '4'
    }
    while n!=0:
        나머지 = n%3
        answer = number_dict[나머지]+ answer
        if n%3 == 0:
            n = n//3 -1
        else:
            n = n//3
            
    return answer


a = solution(6)
print(a)