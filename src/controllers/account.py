from fastapi import APIRouter, Depends
from ..models.customer import Customer
from ..models.account import Account
from ..schemas.account import AccountSchema
from sqlalchemy.orm import Session
from ..database import get_db

accountRouter = APIRouter(
    prefix="/api/accounts",
    tags=["accounts"],
    responses={404: {"description": "Not found"}},
)

@accountRouter.get("/{customerID}")
async def get_customer_accounts(customerID: str, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.customerID == customerID).first()
    if not customer:
        return {"message": "Customer not found"}

    accounts = db.query(Account).filter(Account.customerID == customerID).all()
    return {"accounts": accounts}

@accountRouter.post("/{customerID}")
async def create_customer_account(customerID: str, account: AccountSchema, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.customerID == customerID).first()
    if not customer:
        return {"message": "Customer not found"}
    
    new_account = Account(
        customerID=customerID,
        accountID=account.accountID,
        accountType=account.accountType,
        accountBalance=account.accountBalance,
        accountDateOpened=account.accountDateOpened,
        accountStatus=account.accountStatus,
    )

    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return {"message": "Account created successfully", "account": new_account}

@accountRouter.delete("/{customerID}/{accountID}")
async def delete_customer_account(customerID: str, accountID: str, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.customerID == customerID).first()
    if not customer:
        return {"message": "Customer not found"}

    account = db.query(Account).filter(Account.accountID == accountID).first()
    if not account:
        return {"message": "Account not found"}

    db.delete(account)