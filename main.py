from fastapi import FastAPI
from routes import router  # Import API routes

app = FastAPI(title="User Management API")

# Include all routes
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Welcome to User Management API"}
