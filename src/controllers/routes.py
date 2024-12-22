
from fastapi import APIRouter
from .auth import authRouter
from .agents import agentRouter
from .customer import customerRouter
from .account import accountRouter
from .transactions import transactionRouter

allRoutes = APIRouter()
allRoutes.include_router(authRouter)
allRoutes.include_router(agentRouter)
allRoutes.include_router(customerRouter)
allRoutes.include_router(accountRouter)
allRoutes.include_router(transactionRouter)