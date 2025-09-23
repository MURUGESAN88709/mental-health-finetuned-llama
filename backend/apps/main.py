from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.apps.api.v1 import routes

app = FastAPI(title="LLaMA Serving App")

# Mount static folder for HTML, CSS, JS
app.mount("/static", StaticFiles(directory="backend/static"), name="static")

# Include API routes
app.include_router(routes.router)
