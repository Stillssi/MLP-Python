#딕셔너리 순회 
blood_types = {'A':40, 'B':10, 'AB':20, 'O':30}
count=0
for key in blood_types:
    value= blood_types[key]
    count=count+value

print('총 검사인원은',count, '명 입니다')
#-----
blood_types = {'A':40, 'B':10, 'AB':20, 'O':30}
count=0
for value in blood_types.values():
    count=count+value

print('총 검사인원은',count,'명입니다')


#컨테이너 구축
book_title =  [
    'great', 'expectations', 'the', 'adventures', 
    'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 
    'hamlet', 'adventures', 'of', 'huckleberry', 'fin']
book_infos={}

for key in book_title:
    if key in book_infos:
        book_infos[key] += 1
    else:
        book_infos[key]=1
print(book_infos)


#선초기화
book_infos={}

for key in book_title:
    book_infos[key]=0

print(book_infos)

for key in book_title:
    book_infos[key] +=1

print(book_infos)
#------
book_infos={}

for key in book_title:
    book_infos[key]=book_title.count(key)

print(book_infos)
#-----
book_infos={}

for key in book_title:
    #get메소드 default 값을 0으로 주면, key값이 존재하지 않은 시 0반환
    book_infos[key] = book_infos.get(key,0)+1
print(book_infos)



# 도전! 최대 & 최소 찾기(min & max 쓰지 않고!)
my_list = [3, 2, 10, 2, 4]
max_value=-1e9

for i in my_list:
    if i > max_value:
        max_value = i
print(max_value)

min_value=1e9

for i in my_list:
    if i < min_value:
        min_value = i      

print(min_value)
#--------------------------------------
for i in my_list:
    for j in range(i+1):
        if my_list[i] > my_list[j]:
            num=my_list[i]
            my_list[i]=my_list[j]
            my_list[j]=num
print(my_list)

for i in range(0,4,1):
        if my_list[i+1] > my_list[i]:
            a = my_list[i+1]

print('max:', a)

for i in range(0,4,1):
        if my_list[i+1] < my_list[i]:
            b = my_list[i+1]

print('min:', b)

#연습 while문 작성하기
while True:
    user_input = input('입력: ')
    if user_input == '안녕':
        print("안녕?")
        break
    

#[실습] 합
user_input = int(input('숫자를 입력하시오: '))
sum_value = 0


while user_input>0:
    sum_value += user_input
    user_input-=1
print(sum_value) 

#[응용] 한자리 씩 출력하기
user_input = int(input('숫자를 입력하시오: '))

while(user_input > 0):
    a = user_input%10
    user_input = user_input//10
    print(a)

#[연습]for문작성하기
chars = input('문자를 입력하세요 : ')
for i in chars:
    print(i, end="\n")

#[실습]for문과 if문 작성하기
i=30
while(i>0):
    if i%2 != 0:
        print(i)
    i-=1

#[연습]break 활용하기
rice = ['보리', '보리', '보리', '쌀', '보리']
for i in rice:
    if i == '보리':
        print(i)
    else:
        print(i)
        print("잡았다!")
        break
    
#[연습]continue문 작성하기
ages = [10, 23, 8, 30, 25, 31]
for i in ages:
    if i>=20:
        print(i,'살은 성인입니다.')
    else:
        continue

#[연습]for-else 활용하기
a=0
numbers = [1, 3, 7, 9]
for i in numbers:
    if i ==4:
        print('True')
        a = 1 
        break
    else:
        continue
if a==0:
    print('False')