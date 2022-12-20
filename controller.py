# The controller contains functions that takes in data (such as Order Strings or ids) 
# and run the functions in the Service Object that interact with the DB
# The controller will typically convert String data into Order Objects that can be used with the Service functions

# The controller sends and collects data from the Service file, and pushes this data to the Runner which can display said data

# Not complete, but a suggestion of the process
#def read_by_id(id):
 #   order = service.read_by_id(id)
  #  return order
import sqlite3 as sqlite

connection = sqlite.connect("orders") # If it doesn't exist.. create it
local_cursor = connection.cursor() # .cursor() returns a cursor we can use 

admin_query = "SELECT * FROM sqlite_master"
create_query = "CREATE TABLE orders (order_id integer primary key autoincrement, customer_name VARCHAR(20), main VARCHAR(20), size VARCHAR(10), sauce VARCHAR(20), drink VARCHAR(15))"

def runQuery(order):
    data = local_cursor.execute(order) # our cursor should run our query
    return data

# Insert data into table
insert_query = "INSERT INTO orders (customer_name, main, size, sauce, drink) values('name','main','size','sauce','drink')"
select_query = "SELECT * FROM orders"
#runQuery(create_query)
print(runQuery(select_query).fetchall())

def insertOrder(order):
    query = f"insert into orders (customer_name, main, size, sauce, drink) values('{order[0]}','{order[1]}','{order[2]}','{order[3]}','{order[4]}')"
    runQuery(query)

connection.commit()
