
from fastapi import APIRouter, Depends
from ..database import get_db
from sqlalchemy.orm import Session
from ..models.admin import Admin
from ..schemas.admin import AdminSchema, ReturnSchema

adminRouter = APIRouter(
    prefix="/api/admin",
    tags=["admin"],
    responses={404: {"description": "Not found"}}
)

@adminRouter.get("/")
async def get_admins(db: Session = Depends(get_db)):
    admins = db.query(Admin).all()
    return admins

@adminRouter.get("/{adminID}")
async def get_admin(adminID: str, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.adminID == adminID).first()
    new_admin = ReturnSchema(
        adminID=admin.adminID,
        adminName=admin.adminName,
        adminEmail=admin.adminEmail,
        adminPhone=admin.adminPhone
    )
    return new_admin

@adminRouter.post("/")
async def create_admin(admin: AdminSchema, db: Session = Depends(get_db)):
    db.add(admin)
    db.commit()
    db.refresh(admin)