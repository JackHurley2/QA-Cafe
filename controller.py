# The controller contains functions that takes in data (such as Order Strings or ids) 
# and run the functions in the Service Object that interact with the DB
# The controller will typically convert String data into Order Objects that can be used with the Service functions

# The controller sends and collects data from the Service file, and pushes this data to the Runner which can display said data

# Not complete, but a suggestion of the process
def read_by_id(id):
    order = service.read_by_id(id)
    return order

  

import sqlite3 as sqlite

connection = sqlite.connect("new-db") # If it doesn't exist.. create it
local_cursor = connection.cursor() # .cursor() returns a cursor we can use 

admin_query = "SELECT * FROM sqlite_master"
create_query = "CREATE TABLE orders (order_id int NOT NULL, customer_name VARCHAR(20), size VARCHAR(10), drink BOOLEAN, PRIMARY KEY(order_id))"

def runQuery(query):
    data = local_cursor.execute(query) # our cursor should run our query
    return data

# def createQuery(query):
#     local_cursor.execute(query)
#     return True

# runQuery(create_query)

# fetchall() works like readlines(), reads the data from the file
# print(runQuery(admin_query).fetchall())

# Insert data into our table
# Insert data into ALL columns 
# insert_query = "INSERT into dogs VALUES(3, 'Tri Colour', 'Corgi', true)"
insert_query = "INSERT INTO dogs (colour, breed, bark) VALUES('Tri Colour', 'Corgi', true)"
select_query = "SELECT * FROM dogs"
runQuery(insert_query)
print(runQuery(select_query).fetchall())

# Sqlite ONLY persists data if it is commited
connection.commit()
