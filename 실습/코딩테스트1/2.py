def solution(id_list, report, k):
    answer = []
    report_user = set([])
    reported_user = []
    신당한사람 = []
    declaration_dict={id:0 for id in id_list}

    for i in range(len(id_list)):
        for j in range(len(id_list)):
            if id_list[i]+" "+id_list[j] in report:
                declaration_dict.values(id_list[i])+=1
                '''
                report_user.add(id_list[i])
                reported_user.append(id_list[j])
                '''
                
    report_user = list(report_user) 
    
    for i in range(len(id_list)):
        if reported_user.count(id_list[i]) >= k:
            신당한사람.append(id_list[i])
    
  
    for i in range(len(report_user)):
        for j in range(len(신당한사람)):
            if report_user[i]+" "+신당한사람[j] in report:
                declaration_dict[report_user[i]] += 1
                
    for value in declaration_dict.values():
      answer.append(value)
    return answer


def solution(id_list,report,k):
    answer =[]
    report_info = {}
    mail_info = {}

    for user in id_list:
        report_info[user] = set()
        mail_info[user] = 0

    
    for report_detail in report:
        신고한, 신고당한 = report_detail.split()
        report_info[신고당한].add(신고한)

    for key in report_info:
        if len(report_info[key]) >= k:
            for user in report_info[key]:
                mail_info[user]+=1

    for user in id_list:
        answer.append(mail_info[user])
    
    return answer