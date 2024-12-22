
from pydantic import BaseModel

class TransactionSchema(BaseModel):
    transactionID: str
    transactionType: str
    transactionAmount: int
    transactionDate: str
    agentID: str
    customerID: str
    accountID: str