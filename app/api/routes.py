from fastapi import APIRouter, HTTPException, Depends, Request
from app.dependencies import get_db_adapter, get_mq_adapter, verify_token_with_user_service
from app.core.use_cases import OrderUseCases
from app.core.models import OrderModel

router = APIRouter()

@router.get("/orders/me")
async def get_user_orders(email: str, db_adapter=Depends(get_db_adapter)):
    """
    Gibt alle Bestellungen des Benutzers anhand der E-Mail-Adresse zurück.
    """
    if not email:
        raise HTTPException(status_code=400, detail="Email is required")

    try:
        # Abrufen der Bestellungen aus der Datenbank
        orders = list(db_adapter.collection.find({"customer_name": email}))

        # Entferne das `_id`-Feld
        for order in orders:
            order.pop("_id", None)

        return orders
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving orders: {str(e)}")



@router.post("/orders/", response_model=OrderModel)
async def create_order(order: OrderModel, db_adapter=Depends(get_db_adapter), mq_adapter=Depends(get_mq_adapter)):
    use_cases = OrderUseCases(db_adapter, mq_adapter)
    return await use_cases.create_order(order.dict())

@router.get("/orders/")
async def list_orders(db_adapter=Depends(get_db_adapter)):
    use_cases = OrderUseCases(db_adapter, None)
    return await use_cases.list_orders()

@router.get("/orders/{id}")
async def get_order(id: str, db_adapter=Depends(get_db_adapter)):
    use_cases = OrderUseCases(db_adapter, None)
    order = await use_cases.get_order(id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.get("/")
async def root():
    """
    Test-Endpunkt, um sicherzustellen, dass die API läuft.
    """
    return {"message": "Order Service is running"}
