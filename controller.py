# The controller contains functions that takes in data (such as Order Strings or ids) 
# and run the functions in the Service Object that interact with the DB
# The controller will typically convert String data into Order Objects that can be used with the Service functions

# The controller sends and collects data from the Service file, and pushes this data to the Runner which can display said data

# Not complete, but a suggestion of the process
def read_by_id(id):
    order = service.read_by_id(id)
    return order

  
import runner
import sqlite3 as sqlite

connection = sqlite.connect("new-db") # If it doesn't exist.. create it
local_cursor = connection.cursor() # .cursor() returns a cursor we can use 

admin_query = "SELECT * FROM sqlite_master"
create_query = "CREATE TABLE orders (order_id int NOT NULL, customer_name VARCHAR(20), size VARCHAR(10), drink BOOLEAN, PRIMARY KEY(order_id))"

def runQuery(query):
    data = local_cursor.execute(query) # our cursor should run our query
    return data



# Insert data into table
insert_query = "INSERT INTO orders (order_id i, customer_name, size), drink) VALUES[]"
select_query = "SELECT * FROM orders"
runQuery(insert_query)
print(runQuery(select_query).fetchall())

connection.commit()
