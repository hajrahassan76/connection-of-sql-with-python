import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:C:\C:\Users\S1\Downloads\instantclient-basic-windows.x64-19.11.0.0.0dbru\instantclient_19_11
 
try:
    con = cx_Oracle.connect('scott/tiger@localhost:1521/orcl')
 
except cx_Oracle.DatabaseError as er:
    print('There is an error in the Oracle database:', er)
 
else:
    try:
        cur = con.cursor()
 
        # fetchall() is used to fetch all records from result set
        cur.execute('select * from emp')
        rows = cur.fetchall()
        print(rows[2])
 
        # fetchmany(int) is used to fetch limited number of records from result set based on integer argument passed in it
        cur.execute('select * from emp')
        rows = cur.fetchmany(3)
        print(rows)
		for i in rows:
		print ("empno:",i[0])
		print("ename:",i[1])
		print("job:",i[2])
		print("mgr:",i[3])
		print("hiredate:",i[4])
		print("sal:",i[5])
		print("comm:",i[6])
		print("deptno:",i[7])
        # fetchone() is used fetch one record from top of the result set
 #       cur.execute('select * from emp')
  #      rows = cur.fetchone()
   #     print(rows)
 
    except cx_Oracle.DatabaseError as er:
        print('There is an error in the Oracle database:', er)
 
    except Exception as er:
        print('Error:'+str(er))
 
    finally:
        if cur:
            cur.close()
 
finally:
    if con:
        con.close()