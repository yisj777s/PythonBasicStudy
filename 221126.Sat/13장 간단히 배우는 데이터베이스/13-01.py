import sqlite3

con=None
con=sqlite3.connect("yjuDB")
# con.execute("CREATE TABLE userTable(id char(4), username char(10), email char(30), birthyear int, )") 
con.execute("INSERT INTO userTable VALUES('Lee','Leesj','Leesj@naver.com',1996)")
con.execute("INSERT INTO userTable VALUES('Lee2','Leesj2','Leesj2@naver.com',1997)")
con.execute("INSERT INTO userTable VALUES('Lee3','Leesj3','Leesj3@naver.com',1998)")

con.commit()
con.close()