from fastapi import APIRouter, HTTPException
from app.database import get_connection
from app.models import Transaction

router = APIRouter()

@router.get('/')
def get_transactions():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions')
    transactions = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return transactions

@router.post('/')
def create_transaction(transaction: Transaction):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO transactions (id, accountId, date, type, amount, targetAccountId) VALUES (?, ?, ?, ?, ?, ?)',
        (transaction.id, transaction.accountId, transaction.date, transaction.type, transaction.amount, transaction.targetAccountId),
    )
    conn.commit()
    conn.close()
    return {'message': 'Transaction created successfully'}

@router.get('/{account_id}')
def get_transactions_by_account(account_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions WHERE accountId = ?', (account_id,))
    transactions = [dict(row) for row in cursor.fetchall()]
    conn.close()
    if not transactions:
        raise HTTPException(status_code=404, detail='No transactions found for this account')
    return transactions

