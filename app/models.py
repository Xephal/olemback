from pydantic import BaseModel

class User(BaseModel):
    id: str
    username: str
    email: str
    password: str

class BankAccount(BaseModel):
    id: str
    name: str
    type: str
    balance: float
    userId: str
    lowBalanceThreshold: float

class Transaction(BaseModel):
    id: str
    accountId: str
    date: str
    type: str
    amount: float
    targetAccountId: str = None

class LoginHistory(BaseModel):
    id: str
    userId: str
    date: str

