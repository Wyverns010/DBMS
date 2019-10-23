import mysql.connector
class Database:

    def __init__(self, db):
        self.conn = mysql.connector.connect(
			user = "root",
			password = "root",
			host = "127.0.0.1",
			database = "fifa"
			)
    def insert_players(self,name,country,position,age,height,weight,rating):
        self.cur.execute("INSERT INTO PLAYERS VALUES (%s,%s,%s,%s,%s,%s,%s)",(name,country,position,age,height,weight,rating))
        self.conn.commit()

    # def insert_goals(self,id,goals):
    #     self.cur.execute("INSERT INTO GOALS VALUES (%s,%s)",(id,goals))
    #     self.conn.commit()

	    
    def insert_teams(self,name,country,captain):
        self.cur.execute("INSERT INTO TEAMS VALUES (NULL,%s,%s,%s,%s,%s,%s,%s)",(name,country,position,age,height,weight,rating))
        self.conn.commit()

	    
    def insert_bookings(self,name,yellow,red):
        self.cur.execute("INSERT INTO BOOKINGS VALUES (%s,%s,%s)",(name,int(yellow),int(red)))
        self.conn.commit()

	    
    def insert_goals(self,id,name,team,goals):
        self.cur.execute("INSERT INTO GOALS_MATCH VALUES (%s,%s,%s,%s)",(id,name,team,int(goals)))
        self.conn.commit()

	    
    def insert_match(self,id,t1,t2,loc,match_date):
        self.cur.execute("INSERT INTO MATCHES VALUES (%s,%s,%s,%s,%s)",(id,t1,t2,loc,match_date))
        self.conn.commit()

	    
    def insert_players(self,name,country,position,age,height,weight,rating):
        self.cur.execute("INSERT INTO PLAYERS VALUES (NULL,%s,%s,%s,%s,%s,%s,%s)",(name,country,position,age,height,weight,rating))
        self.conn.commit()

	    
	    

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
