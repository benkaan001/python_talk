import mysql.connector

connection = mysql.connector.connect(host = 'localhost', user='******', password='******', database='just_tech_news_java_db')
cursor = connection.cursor()

query='SELECT comment_text, post_id FROM comment'

cursor.execute(query)

print(cursor.fetchall())

cursor.close()
connection.close()

#### [('Hi', 3)]

