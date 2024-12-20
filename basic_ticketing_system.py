from flask import Flask, request, render_template
import sqlite3
import os

# Set the working directory to the folder containing the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, request, render_template
import sqlite3


app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            priority TEXT NOT NULL,
            status TEXT DEFAULT 'Open'
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

@app.route('/')
def index():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tickets")
    tickets = cursor.fetchall()
    conn.close()
    return render_template('index.html', tickets=tickets)

@app.route('/create-ticket', methods=['POST'])
def create_ticket():
    title = request.form['title']
    description = request.form['description']
    priority = request.form['priority']

    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tickets (title, description, priority) VALUES (?, ?, ?)", (title, description, priority))
    conn.commit()
    conn.close()

    return 'Ticket created successfully! <a href="/">Go back</a>'

@app.route('/update-ticket/<int:ticket_id>', methods=['POST'])
def update_ticket(ticket_id):
    status = request.form['status']

    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tickets SET status = ? WHERE id = ?", (status, ticket_id))
    conn.commit()
    conn.close()

    return 'Ticket updated successfully! <a href="/">Go back</a>'

if __name__ == '__main__':
    app.run(debug=True)
