from fastapi import FastAPI
from app.routers import inventory, calculations

app = FastAPI(
    title="BlueScope Steel Inventory API",
    description="Inventory management system for steel products",
    version="0.1.0"
)

# Include routers
app.include_router(inventory.router)
app.include_router(calculations.router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to BlueScope Steel Inventory API",
        "docs": "/docs",
        "version": "0.1.0"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
