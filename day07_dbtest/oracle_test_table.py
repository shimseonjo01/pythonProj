import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()

cursor.execute("select count(*) from all_tables where table_name = 'TEST'") # TEST테이블이 있으면 1 리턴, 없으면 0 리턴

if cursor == 0: # 테이블이 없으면 만든다.
    cursor.execute("create table test(id number(2))") 

cursor.execute("insert into test values(01)")
cursor.close()
conn.commit()
conn.close()
