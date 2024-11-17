from fastapi import APIRouter, HTTPException
from app.database import get_connection
from app.models import LoginHistory

router = APIRouter()

@router.get('/')
def get_login_history():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM loginHistory')
    history = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return history

@router.post('/')
def create_login_entry(entry: LoginHistory):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO loginHistory (id, userId, date) VALUES (?, ?, ?)',
        (entry.id, entry.userId, entry.date),
    )
    conn.commit()
    conn.close()
    return {'message': 'Login entry created successfully'}

