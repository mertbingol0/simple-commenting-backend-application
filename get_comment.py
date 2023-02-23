import sqlite3

def getComment():

	conn = sqlite3.connect('comment.db')
	cursor = conn.cursor()

	select_comments = """SELECT * FROM comment"""
	
	cursor.execute(select_comments)
	comments = cursor.fetchall()

	return comments