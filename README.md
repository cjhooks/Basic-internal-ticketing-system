# Basic Ticketing System

This is a simple ticketing system built using Python, Flask, and SQLite. It allows users to create, view, and update tickets via a web interface. This project demonstrates foundational skills in web development, database management, and Python programming.

## Features

- **Create Tickets**: Users can submit tickets with a title, description, and priority level.
- **View Tickets**: Displays all tickets in a table format, showing their details and current status.
- **Update Tickets**: Allows updating the status of tickets (e.g., Open, Resolved).
- **Persistent Storage**: Tickets are stored in an SQLite database.

## Technologies Used

- **Python**: The primary programming language.
- **Flask**: A lightweight web framework for routing and rendering templates.
- **SQLite**: A lightweight database for storing ticket data.
- **HTML/CSS**: For creating the user interface.

## File Structure

```
/basic_ticketing_system
├── basic_ticketing_system.py  # Main Flask application
├── templates/
│   └── index.html            # HTML template for the app
└── tickets.db                # SQLite database
```

## Setup and Usage

### Prerequisites

- Python 3 installed on your system.
- Flask installed (`pip install flask`).

### Steps to Run

1. Clone this repository or download the project files.
2. Navigate to the project directory:
   ```bash
   cd basic_ticketing_system
   ```
3. Run the application:
   ```bash
   python basic_ticketing_system.py
   ```
4. Open your web browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

## Code Breakdown

Here is a detailed explanation of the code to help you understand its functionality:

### 1. **Imports**
```python
from flask import Flask, request, render_template
import sqlite3
import os
```
- **`Flask`**: Creates the web application.
- **`request`**: Handles incoming HTTP requests (e.g., form submissions).
- **`render_template`**: Loads HTML templates.
- **`sqlite3`**: Manages the SQLite database.
- **`os`**: Interacts with the operating system for file management.

### 2. **Flask App Initialization**
```python
app = Flask(__name__)
```
Creates the Flask app instance. The `__name__` parameter ensures Flask knows where to find resources.

### 3. **Database Initialization**
```python
def initialize_database():
    connection = sqlite3.connect("tickets.db")
    cursor = connection.cursor()

    # Create the tickets table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        priority TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)
    connection.commit()
    connection.close()
```
- Connects to `tickets.db` and creates a `tickets` table if it doesn’t exist.
- Columns:
  - **`id`**: Auto-incrementing primary key.
  - **`title`**: Title of the ticket.
  - **`description`**: Details about the ticket.
  - **`priority`**: Priority level (e.g., High, Medium, Low).
  - **`status`**: Status of the ticket (e.g., Open, Resolved).

### 4. **Routes**
#### Home Route
```python
@app.route("/")
def index():
    connection = sqlite3.connect("tickets.db")
    cursor = connection.cursor()

    # Retrieve all tickets from the database
    cursor.execute("SELECT * FROM tickets")
    tickets = cursor.fetchall()
    connection.close()

    return render_template('index.html', tickets=tickets)
```
- **`@app.route("/")`**: Defines the home page route.
- Fetches all tickets from the database and passes them to `index.html` for rendering.

#### Add Ticket Route
```python
@app.route("/add", methods=["POST"])
def add_ticket():
    title = request.form["title"]
    description = request.form["description"]
    priority = request.form["priority"]

    connection = sqlite3.connect("tickets.db")
    cursor = connection.cursor()

    # Insert a new ticket into the database
    cursor.execute("INSERT INTO tickets (title, description, priority, status) VALUES (?, ?, ?, ?)",
                   (title, description, priority, "Open"))
    connection.commit()
    connection.close()

    return "Ticket created successfully! <a href='/'>Go back</a>"
```
- Handles form submissions to create a new ticket.
- Inserts the ticket details into the database with a default status of `Open`.

#### Update Ticket Route
```python
@app.route("/update/<int:ticket_id>", methods=["POST"])
def update_ticket(ticket_id):
    new_status = request.form["status"]

    connection = sqlite3.connect("tickets.db")
    cursor = connection.cursor()

    # Update the ticket's status in the database
    cursor.execute("UPDATE tickets SET status = ? WHERE id = ?", (new_status, ticket_id))
    connection.commit()
    connection.close()

    return "Ticket updated successfully! <a href='/'>Go back</a>"
```
- Updates the status of a ticket based on its ID.

### 5. **Running the App**
```python
if __name__ == "__main__":
    app.run(debug=True)
```
- Starts the Flask development server with debugging enabled.

## Future Enhancements

- Add authentication to secure ticket management.
- Implement filtering and sorting for tickets.
- Improve the UI with CSS frameworks like Bootstrap.
- Expand the database schema to include timestamps and user information.


## License
This project is open-source and available under the MIT License.

