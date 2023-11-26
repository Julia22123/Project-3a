import sqlite3

# open a connection to a database file named database.db, which will be created once this script is run
connection = sqlite3.connect("database.db")

# open the schema.sql file and execute its contents using the executescript() method that executes multiple SQL statements at once, 
# this will create the posts table.
with open("schema.sql") as database_schema:
    connection.executescript(database_schema.read())

# create a cursor object which allows us to process rows in a database.
cur = connection.cursor()


# use the cursor’s execute() method to execute the INSERT SQL statements to data to the data table
cur.execute("INSERT INTO data (Symbol, Name, Sector) VALUES (?, ?, ?)", ("", "", ""))

# commit the changes to the database and close the connection
connection.commit()
connection.close() 
