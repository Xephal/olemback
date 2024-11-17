from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import users, bank_accounts, transactions, login_history
from app.database import create_tables

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],  # FrontEnd Address (http-server / live-server )
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(users.router, prefix='/users', tags=['Users'])
app.include_router(bank_accounts.router, prefix='/bankAccounts', tags=['Bank Accounts'])
app.include_router(transactions.router, prefix='/transactions', tags=['Transactions'])
app.include_router(login_history.router, prefix='/loginHistory', tags=['Login History'])

@app.on_event('startup')
def startup_event():
    create_tables()

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Banking Backend"}
