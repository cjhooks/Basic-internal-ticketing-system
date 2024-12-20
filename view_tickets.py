import sqlite3

# Connect to the database
connection = sqlite3.connect("tickets.db")

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Query to view all records in the 'tickets' table
cursor.execute("SELECT * FROM tickets")

# Fetch and print all rows
rows = cursor.fetchall()
if rows:
    print("ID | Title | Description | Priority | Status")
    print("-" * 50)
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
else:
    print("No tickets found.")

# Close the connection
connection.close()
