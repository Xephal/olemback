from fastapi import APIRouter, HTTPException
from app.database import get_connection
from app.models import BankAccount

router = APIRouter()

@router.get('/')
def get_bank_accounts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM bankAccounts')
    accounts = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return accounts

@router.post('/')
def create_bank_account(account: BankAccount):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO bankAccounts (id, name, type, balance, userId, lowBalanceThreshold) VALUES (?, ?, ?, ?, ?, ?)',
        (account.id, account.name, account.type, account.balance, account.userId, account.lowBalanceThreshold),
    )
    conn.commit()
    conn.close()
    return {'message': 'Bank account created successfully'}

@router.get('/{account_id}')
def get_bank_account(account_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM bankAccounts WHERE id = ?', (account_id,))
    account = cursor.fetchone()
    conn.close()
    if not account:
        raise HTTPException(status_code=404, detail='Bank account not found')
    return dict(account)

