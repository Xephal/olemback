import sqlite3

DB_NAME = 'database.db'

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Enables dict-like access
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,
        username TEXT,
        email TEXT,
        password TEXT
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bankAccounts (
        id TEXT PRIMARY KEY,
        name TEXT,
        type TEXT,
        balance REAL,
        userId TEXT,
        lowBalanceThreshold REAL
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id TEXT PRIMARY KEY,
        accountId TEXT,
        date TEXT,
        type TEXT,
        amount REAL,
        targetAccountId TEXT
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS loginHistory (
        id TEXT PRIMARY KEY,
        userId TEXT,
        date TEXT
    );
    """)
    conn.commit()
    conn.close()

