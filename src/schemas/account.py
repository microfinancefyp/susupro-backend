
from pydantic import BaseModel

class AccountSchema(BaseModel):
    accountID: str
    accountBalance: int
    accountType: str
    accountStatus: str
    accountDateOpened: str
    customerID: str