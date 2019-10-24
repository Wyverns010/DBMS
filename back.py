import mysql.connector

class Database:

    def __init__(self): # was db before
        self.conn = mysql.connector.connect(
			user = "root",
			password = "root",
			host = "127.0.0.1",
			database = "fifa"
			)
        self.cur = self.conn.cursor();

    def insert_players(self,name,country,position,age,height,weight,rating):
        self.cur.execute("INSERT INTO PLAYERS VALUES (%s,%s,%s,%s,%s,%s,%s)",(name,country,position,int(age),int(height),int(weight),int(rating)))
        self.conn.commit()


    def insert_teams(self,name,country):
        self.cur.execute("INSERT INTO TEAMS VALUES (%s,%s)",(name,country))
        self.conn.commit()


    def insert_bookings(self,name,yellow,red):
        self.cur.execute("INSERT INTO BOOKINGS VALUES (%s,%s,%s)",(name,int(yellow),int(red)))
        self.conn.commit()


    def insert_goals(self,name,team,id,goals):
        self.cur.execute("INSERT INTO GOALS_MATCH VALUES (%s,%s,%s,%s)",(int(id),name,team,int(goals)))
        self.conn.commit()


    def insert_matches(self,id,t1,t2,loc,match_date):
        self.cur.execute("INSERT INTO MATCHES VALUES (%s,%s,%s,%s,%s)",(int(id),t1,t2,loc,match_date))
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

    def view_matches(self):
        self.cur.execute("SELECT * FROM MATCHES")
        rows=self.cur.fetchall()
        return rows

    def view_scorers(self):
        self.cur.execute("SELECT * FROM GOALS_MATCH")
        rows=self.cur.fetchall()
        return rows

    def view_score(self):
        self.cur.execute("SELECT * FROM GOALS")
        rows=self.cur.fetchall()
        return rows

    def view_bookings(self):
        self.cur.execute("SELECT * FROM BOOKINGS")
        rows=self.cur.fetchall()
        return rows

    def delete_player(self,name):
        self.cur.execute("DELETE FROM PLAYERS WHERE name=%s",(name,))
        self.conn.commit()

    def delete_team(self,name):
        self.cur.execute("DELETE FROM TEAMS WHERE name=%s",(name,))
        self.conn.commit()

    def delete_match(self,id):
        self.cur.execute("DELETE FROM MATCHES WHERE id=%s",(int(id),))
        self.conn.commit()

    def delete_booking(self,name):
        self.cur.execute("DELETE FROM BOOKINGS WHERE name=%s",(name,))
        self.conn.commit()


    def update_player(self,name,country,position,age,height,weight,rating):
        self.cur.execute("UPDATE PLAYERS SET country = %s, position = %s, age = %s, height = %s, weight = %s, rating = %s WHERE name=%s",(country,position,int(age),int(height),int(weight),int(rating),name))
        self.conn.commit()

    def update_team(self,name,country):
        self.cur.execute("UPDATE TEAMS SET country=%s WHERE name = %s",(country,name))
        self.conn.commit()

    def update_match(self,id,t1,t2,loc,match_date):
        self.cur.execute("UPDATE MATCHES SET team1=%s, team2=%s, location=%s, match_date=%s WHERE id=%s",(t1,t2,loc,match_date,int(id)))
        self.conn.commit()

    def update_booking(self,name,yellow,red):
        self.cur.execute("UPDATE BOOKINGS SET yellow_cards=%s, red_cards=%s WHERE PLAYER=%s",(int(yellow),int(red),name))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
