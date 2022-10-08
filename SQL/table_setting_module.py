import pymysql
class setting_tb:
    def DB_connection():
        print('DB 테스트')
        print(' DB 연결 시작')
        try:
            #CONFIG 파일 읽어오기
            db_config = {}
            with open('./db_config', 'r') as  f:
                for l in f.readlines():
                    key, value = l.rstrip().split('=')
                    if key == 'port':
                        db_config[key] = int(value)
                    else:
                        db_config[key] = value
            print(db_config)
            conn = pymysql.connect(
                **db_config
            )
            print('DB접속 성공')
            return conn
        except:
            print('DB접속 실패')
        
    def insert_tb(conn, table, column, tuple):
        try:
            with conn.cursor() as cursor:
                column_len = ','.join(['%s'] * len(column))
                column_str = ','.join(column)
                sql = f'INSERT INTO `{table}`({column_str}) VALUES({column_len})'
                cursor.execute(sql, tuple)
                conn.commit()
                print('하나 넣기 성공')
                return True
        except Exception as e:
            print(e)
            print('하나 넣기 실패')
            return False

    def insert_tb_many(conn, table, column, data_list):
        try:
            with conn.cursor() as cursor:
                column_len = ','.join(['%s'] * len(column))
                column_str = ','.join(column)
                sql = f'INSERT INTO `{table}`({column_str}) VALUES({column_len})'
                print(sql)
                cursor.executemany(sql, data_list)
                conn.commit()
                print('많이 넣기 성공')
                return True
        except:
            print('많이 넣기 실패')
            return False       

    def select_tb(conn,table,  column = '*'):
        try:
            with conn.cursor() as cursor:
                column_str = ','.join(column)
                sql = f'SELECT {column_str} FROM `{table}`'
                print(sql)
                cursor.execute(sql)
                conn.commit()
                print('셀렉트 성공')
                return True
        except Exception as e:
            print(e)
            print('셀렉트 실패')
            return False
    
    def update_tb(conn, table, set_column, set_value,where_value, where_column= 'id'):
        try:
            with conn.cursor() as cursor:
                #set_column_str = ','.join(set_column)
                #set_value_str = ','.join(set_value)
                sql = f'UPDATE `{table}` SET `{set_column}`=%s WHERE `{where_column}`=%s'
                print(sql)
                cursor.execute(sql,(set_value,where_value) )
                conn.commit()
                print('업데이트 성공')
                return True
        except:
            print('업데이트 실패')
            return False

    def del_tb(conn, table, where_value, where_column = 'id'):
        try:
            with conn.cursor() as cursor:
                sql = f'DELETE FROM `{table}` WHERE `{where_column}`={where_value}'
                cursor.execute(sql)
                conn.commit()
                print('삭제 성공')
                return True
        except:
            print('삭제 실패')
            return False

    def db_close(conn):
        print('연결 해제')
        conn.close()
