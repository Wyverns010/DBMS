import mysql.connector

class Database:

    def __init__(self): # was db before
        self.conn = mysql.connector.connect(
			user = "root",
			password = "root",
			host = "127.0.0.1",
			database = "fifa"
			)

    def insert_players(self,name,country,position,age,height,weight,rating):
        self.cur.execute("INSERT INTO PLAYERS VALUES (%s,%s,%s,%s,%s,%s,%s)",(name,country,position,age,height,weight,rating))
        self.conn.commit()

	    
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

	    
    def insert_playsfor(self,team,name):
        self.cur.execute("INSERT INTO PLAYS_FOR VALUES (%s,%s)",(team,name))
        self.conn.commit()

	    
	    

    def view_players(self):
        self.cur.execute("SELECT * FROM PLAYERS")
        rows=self.cur.fetchall()
        return rows

    def view_teams(self):
        self.cur.execute("SELECT * FROM TEAMS")
        rows=self.cur.fetchall()
        return rows

    def view_scorers(self):
        self.cur.execute("SELECT * FROM GOALS")
        rows=self.cur.fetchall()
        return rows

    def view_bookings(self):
        self.cur.execute("SELECT * FROM BOOKINGS")
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