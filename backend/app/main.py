from fastapi import Depends, FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import Annotated
from . import models
from .config.database import engine, get_db
from .routes.cart import router as cart_router
from .routes.auth import router as auth_router
from .routes.health import router as health_router
from .routes.products import router as products_router

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:3000",
    # "http://52.53.186.174",
]

app = FastAPI(
    title="CircuitCart Backend",
    description="shitty ass website to sell tech components",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/", tags=["System"], description="Provides a welcome message and confirms that the API is running.")
def read_root():
    return {"message": "Welcome to the CircuitCart"}

# Create a versioned router for API versioning.
v1_router = APIRouter(prefix="/api/v1")

# Include all individual routers under the versioned router.
v1_router.include_router(cart_router)
v1_router.include_router(auth_router)
v1_router.include_router(health_router)
v1_router.include_router(products_router)

# Include the versioned router in the main app.
app.include_router(v1_router)