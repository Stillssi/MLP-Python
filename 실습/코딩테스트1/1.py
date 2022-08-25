def solution(lottos, win_nums):
    answer = []
    cnt = 0 
    zero = 0
    for lotto in lottos:
        if lotto == 0:
            zero += 1
        else:
            if lotto in win_nums:
                cnt +=1
            ''' 
            위에 코드랑 같음
            for win_num in win_nums:
                if lotto == win_num:
                    cnt += 1
'''
    answer.append(7-(cnt+zero))
    if 7-cnt >= 6:
        answer.append(6)
    else:
        answer.append(7-cnt)

    return answer

'''
best_rank = min(7-(cnt+zero),6)
worst_rank = min(7-cnt ,6) 
''' 