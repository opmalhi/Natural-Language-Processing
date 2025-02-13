from fastapi import FastAPI
from routes import webhook_routes

app = FastAPI()

app.include_router(webhook_routes.webhook_router)

