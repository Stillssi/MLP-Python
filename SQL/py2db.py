import pymysql
class Py2DB:
    pass
def func():
    pass
#여기도 실행은 됨, 안쓰는게 좋음
#print('hello1')
#만약 이 파일을 실행할 경우 실행할 코드
if __name__ == '__main__':
    print('DB 테스트')
    print(' DB 연결 시작')
    try:
        conn = pymysql.connect(
            host = 'database-1.cgwshzcvqc9b.ap-northeast-2.rds.amazonaws.com',
            port = 3306,
            user = "Stillssi",
            password= "maesan10528",
            database= 'study',
            charset= 'utf8mb4'
        )
        print('DB접속 성공')
        
        #데이터 삽입, 한개만(INSERT)
        try:
            with conn.cursor() as cursor:
                sql = """INSERT INTO `Students`(`name`,`email`,`phone`, `major`)
                VALUES(%s,%s,%s,%s)"""
                print(sql)
                cursor.execute(sql,('신향아', '213123@naver.com','01021321323', "소프트웨어학부"))
            #한개 넣고 주석처리 해야 또 안들어감  
                conn.commit()   
        except:
            print('데이터 삽입 실패')    
        

        #데이터 삽입 여러개(INSERT MANY)
        try:
            with conn.cursor() as cursor:
                sql = """INSERT INTO `Students`(`name`,`email`,`phone`, `major`)
                VALUES(%s,%s,%s,%s)"""

                #sql = ','.join(['%s']*column_len)
                cursor.executemany(sql,[('이슬기','aa@aa.aa', '010XXXXXXXX', '전자공학과'),
                ('신정운', 'bb@bb.bb', '010********', '교육학과')
                ])
                conn.commit()
        except:
            print('데이터 다량 삽입 실패')
        

        # SELECT 
        try:
            with conn.cursor() as cursor:
                sql = '''SELECT * FROM Students
                '''
                cursor.execute(sql, )
                result = cursor.fetchall()
            print(result)
        except:
            print('SELECT 실패')

        #UPDATE
        with conn.cursor() as cursor:
            sql = "UPDATE `student` SET `id = %s"
            cursor.execute(sql, ('1,'))
            conn.commit()
        #연결 해제   
        print('연결 해제')
        conn.close()
    
    
    except:
        print('DB접속 실패')

