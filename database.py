%%writefile database.py
import sqlite3

# connect to database
conn = sqlite3.connect("health.db")
cursor = conn.cursor()

# medication table
cursor.execute("""
CREATE TABLE IF NOT EXISTS medication(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
time TEXT
)
""")

# fitness table
cursor.execute("""
CREATE TABLE IF NOT EXISTS fitness(
id INTEGER PRIMARY KEY AUTOINCREMENT,
steps INTEGER,
calories INTEGER
)
""")

conn.commit()

print("Database created successfully")
