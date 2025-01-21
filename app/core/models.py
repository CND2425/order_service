from pydantic import BaseModel, Field
from typing import Optional, List

class OrderItemModel(BaseModel):
    product_id: str = Field(..., description="The ID of the product")
    quantity: int = Field(..., ge=1, description="The quantity of the product ordered")
    price: float = Field(..., gt=0, description="The price per unit of the product")

class OrderModel(BaseModel):
    id: Optional[str] = Field(alias="_id", default=None)
    customer_name: str = Field(..., description="Name of the customer")
    items: List[OrderItemModel] = Field(..., description="List of items in the order")
    total_price: float = Field(..., ge=0, description="Total price for the order")
    status: str = Field(..., description="The status of the order (e.g., pending, shipped, delivered)")
