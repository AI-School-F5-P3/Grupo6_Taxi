import sqlite3

def create_connection_database(): 
	"""Create a database connection"""
	try:
		with sqlite3.connect("taximetro.db") as con:
			cur = con.cursor()
			cur.execute("""CREATE TABLE IF NOT EXISTS trip (
				id INTEGER PRIMARY KEY,
			begin_date TEXT,
			end_date TEXT,
			total REAL
			)""")
			con.commit()
	except sqlite3.Error as e:
		print("Error: ", e)
	return con

def add_trip_database(start_time, end_time, total):
	con = create_connection_database()
	cur = con.cursor()
	query = "INSERT INTO trip(begin_date, end_date, total) VALUES(?, ?, ?)"
	cur.execute(query, (start_time, end_time, total))
	con.commit()