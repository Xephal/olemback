import sqlite3

def clear_database():
    conn = sqlite3.connect("database.db")  # Connect to the database
    cursor = conn.cursor()

    # Fetch all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Disable foreign key checks temporarily
    cursor.execute("PRAGMA foreign_keys = OFF;")

    # Clear all data from each table
    for table in tables:
        table_name = table[0]
        if table_name != "sqlite_sequence":  # Skip SQLite's internal sequence table
            cursor.execute(f"DELETE FROM {table_name};")
            print(f"Cleared data from table: {table_name}")

    # Re-enable foreign key checks
    cursor.execute("PRAGMA foreign_keys = ON;")

    conn.commit()
    conn.close()
    print("Database cleared successfully.")

clear_database()
