from fastapi import APIRouter, HTTPException
from app.database import get_connection
from app.models import User

router = APIRouter()

@router.get('/')
def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return users

@router.post('/')
def create_user(user: User):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO users (id, username, email, password) VALUES (?, ?, ?, ?)',
        (user.id, user.username, user.email, user.password),
    )
    conn.commit()
    conn.close()
    return {'message': 'User created successfully'}

@router.get('/{user_id}')
def get_user(user_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return dict(user)

