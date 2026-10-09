import pymysql
conn=pymysql.connect(
    host='localhost',
    user='root',
    password='Lallu1004@',
    database='aug2026',
)



cursor=conn.cursor()

#sql="insert into empoloyee values(1,'arun',25000,'dev')"
#sql="insert into empoloyee values(2,'arjun',30000,'dev')"
#sql="insert into empoloyee values(3,'aravind',35000,'HR')"
#sql="insert into empoloyee values(4,'anoop',40000,'HR')"
#sql="insert into empoloyee values(5,'arjun',50000,'finance')"
#sql="create table empoloyee(id int primary key,name varchar(20),salary int,department varchar(20))"
sql="select * from empoloyee"
cursor.execute(sql)

row=cursor.fetchone()                     #fetchall: it is used to fetch all table 
print(row)                                  #fetchmany: it is used to print specific table   
#for i in row:                               #fetchone: it is used to print only first table from the data base
    #print(i[0],i[1],i[2],i[3])

conn.commit()
conn.close()

