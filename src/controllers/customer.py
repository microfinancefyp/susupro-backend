
from fastapi import APIRouter, Depends
from ..models.customer import Customer
from ..models.account import Account
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.customer import CustomerSchema

customerRouter = APIRouter(
    prefix="/api/customers",
    tags=["customers"],
    responses={404: {"description": "Not found"}},
)

@customerRouter.get("/")
async def get_all_customers(db: Session = Depends(get_db)):
    result = db.query(Customer).all()
    return result

@customerRouter.get("/balance/{customerID}")
async def get_customer_balance(customerID: str, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.customerID == customerID).first()
    accounts = db.query(Account).filter(Account.customerID == customerID).all()
    
    if customer is None:
        return {"message": "Customer not found"}
    else:
        balance = 0
        for account in accounts:
            balance += account.accountBalance
        return {"customerID": customer.customerID, "customerName": customer.customerName, "Total balance": balance}
    return 

@customerRouter.post("/")
async def create_customer(customer: CustomerSchema, db: Session = Depends(get_db)):
    new_customer = Customer(
        customerID=customer.customerID,
        customerName=customer.customerName,
        customerAccountNo=customer.customerAccountNo,
        customerLocation=customer.customerLocation,
        customerDateOfBirth=customer.customerDateOfBirth,
        customerNextofKin=customer.customerNextofKin,
        customerNextofKinPhone=customer.customerNextofKinPhone,
        customerPhone=customer.customerPhone,
        customerDailyRate=customer.customerDailyRate,
        agentID=customer.agentID
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

@customerRouter.delete("/{customer_id}")
async def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.customerID == customer_id).first()
    if customer:
        db.delete(customer)
        db.commit()
        return {"message": "Customer deleted successfully"}
    else:
        return {"message": "Customer not found"}