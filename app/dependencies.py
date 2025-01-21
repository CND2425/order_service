from pymongo import MongoClient
from app.adapters.db_adapter import MongoDBAdapter
from app.adapters.mq_adapter import RabbitMQAdapter
from app.config import Config
import requests
from fastapi import HTTPException

# MongoDB
client = MongoClient(Config.MONGO_URI)
db = client.order_management
order_collection = db.get_collection("orders")

# Adapters
db_adapter = MongoDBAdapter(order_collection)
mq_adapter = RabbitMQAdapter(Config.RABBITMQ_URL)

def get_db_adapter():
    return db_adapter

def get_mq_adapter():
    return mq_adapter

def verify_token_with_user_service(token: str):
    """
    Verifiziert ein JWT-Token durch den User-Service.
    """
    try:
        response = requests.post(
            "http://user-service:8003/token/verify",  # URL des User-Service-Endpunkts
            json={"token": token},
        )
        response.raise_for_status()
        return response.json()  # Enthält die decodierten Payload-Daten
    except requests.RequestException:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
