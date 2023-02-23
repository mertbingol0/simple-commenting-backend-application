import sqlite3

def send_comment(username, email, comment):
	
	conn = sqlite3.connect('comment.db')
	cursor = conn.cursor()

	create_table = """CREATE TABLE IF NOT EXISTS comment (username, email, comment)"""
	insert_comment = """INSERT INTO comment (username, email, comment) VALUES (?,?,?)"""

	cursor.execute(create_table)
	cursor.execute(insert_comment, (username, email, comment))
	conn.commit()