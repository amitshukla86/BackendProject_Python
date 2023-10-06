# connecting to MYSQL DB

import mysql.connector
from utilities.commonFunctions import *
from utilities.configurations import getConnection


# creating the connection
conn = getConnection()
# executing the query
cursor = conn.cursor()
cursor.execute('select * from books')

# Fetching the results from the cursor
allrows = cursor.fetchall()
print(allrows)

# reading data from table query and getting distinct book list and count of each type of book
booklist = []
booklist1 = []
bookcount = {}
for rows in allrows:
    booklist1.append(rows[1])
    if rows[1] not in booklist:
        booklist.append(rows[1])

for book in booklist1:
    bookcount[book] = booklist1.count(book)
print("List of all books in DB - " + str(booklist1))
print("Distinct books in DB - " + str(booklist))
print("Count of each distinct book in DB - " + str(bookcount))

# executing update queries
query = 'update books set aisle = %s where bookid = %s'
data = ("250", "21")
cursor.execute(query, data)
conn.commit()

# executing delete queries
query1 = 'delete from books where bookid = 21'
cursor.execute(query1)
conn.commit()

# Closing the connection
conn.close()
