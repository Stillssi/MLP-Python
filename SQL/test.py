from table_setting_module import setting_tb

if __name__ == '__main__':
    conn = setting_tb.DB_connection()
    #setting_tb.insert_tb(conn, 'Students', ('name','email','phone', 'major'), ('신향아1', 'safasdf@naver.com','01012312332', "소프트웨어학부"))
    #setting_tb.insert_tb_many(conn, 'Students', ('name','email','phone', 'major'),[('이슬기2','aa@aa.aa', '010XXXXXXXX', '전자공학과'),
                #('신정운3', 'bb@bb.bb', '010********', '교육학과')])
    #setting_tb.select_tb(conn, 'Students')
    #setting_tb.update_tb(conn, 'Students', 'email' , 'acs@aa.cc', 3 ,'id')
    #setting_tb.del_tb(conn, 'Students', 1, where_column = 'id')
    setting_tb.db_close(conn)