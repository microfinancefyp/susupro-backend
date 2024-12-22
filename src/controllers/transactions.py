
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models.transaction import Transaction
from ..models.customer import Customer
from ..models.account import Account
from ..schemas.transaction import TransactionSchema
from fastapi import HTTPException
from ..database import get_db


transactionRouter = APIRouter(
    prefix="/api/transactions",
    tags=["transactions"],
    responses={404: {"description": "Not found"}}
)

@transactionRouter.get("/")
async def get_transactions(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()
    return [row._asdict() for row in transactions]

@transactionRouter.get("/{transaction_id}")
async def get_transaction(transaction_id: str, db: Session = Depends(get_db)):
    transaction = db.query(Transaction).filter(Transaction.transactionID == transaction_id).first()
    return transaction

@transactionRouter.get("/agent/{agentID}")
async def get_customer_transactions(agentID: str, db: Session = Depends(get_db)):
    transactions = db.query(Transaction).filter(Transaction.agentID == agentID).all()
    return {"transactions": transactions}



@transactionRouter.get("/customer/{customer_id}")
async def get_customer_transactions(customer_id: str, db: Session = Depends(get_db)):
    transactions = (
        db.query(Transaction)
        .filter(Transaction.customerID == customer_id)
        .all()
    )

    if not transactions:
        raise HTTPException(status_code=404, detail="No transactions found for the specified customer")
    
    customer = db.query(Customer).filter(Customer.customerID == customer_id).first()

    # Prepare the response
    response = {
        "message": "Customer transactions retrieved successfully",
        "customerID": customer_id,
        "customerName": customer.customerName,
        "transactions": [
            {
                "transactionID": transaction.transactionID,
                "transactionType": transaction.transactionType,
                "transactionAmount": transaction.transactionAmount,
                "transactionDate": transaction.transactionDate,
                "agentName": transaction.agents,
                "agentID": transaction.agentID,
            }
            for transaction in transactions
        ],
    }

    return response



@transactionRouter.post("/")
async def create_transaction(transaction: TransactionSchema, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.customerID == transaction.customerID).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    # Validate that the account exists and belongs to the customer
    account = db.query(Account).filter(
        Account.accountID == transaction.accountID,
        Account.customerID == transaction.customerID
    ).first()
    
    if not account:
        raise HTTPException(
            status_code=404, 
            detail=f"Account with ID {transaction.accountID} not found for Customer {transaction.customerID}"
        )
    
    # Create a new transaction
    new_transaction = Transaction(
        transactionID=transaction.transactionID,
        transactionType=transaction.transactionType,
        transactionAmount=transaction.transactionAmount,
        transactionDate=transaction.transactionDate,
        accountID=transaction.accountID,
        customerID=transaction.customerID,
        agentID=transaction.agentID
    )
    
    # Update the account balance
    if transaction.transactionType == "deposit":
        account.accountBalance += transaction.transactionAmount
    elif transaction.transactionType == "withdrawal":
        if account.accountBalance < transaction.transactionAmount:
            raise HTTPException(status_code=400, detail="Insufficient balance")
        account.accountBalance -= transaction.transactionAmount
    
    # Save to the database
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    
    return {
        "message": "Transaction completed successfully",
        "transaction": new_transaction
    }
