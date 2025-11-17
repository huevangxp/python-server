from fastapi import FastAPI
from app.routers.user_router import router as user_router
from app.config.database import Base, engine

app = FastAPI()

# Create tables automatically
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(user_router)

@app.get("/")
def home():
    return {"message": "API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="10.2.10.12", port=8000)
