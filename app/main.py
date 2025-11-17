from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.user_router import router as user_router
from app.config.database import Base, engine
import os

app = FastAPI(
    title="Your API",
    version="1.0.0"
)

# CORS (adjust for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables automatically (use Alembic in production)
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(user_router)

@app.get("/")
def home():
    return {"message": "API is running", "status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 8000))
    )