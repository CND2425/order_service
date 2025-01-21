from bson import ObjectId
from pymongo import ReturnDocument
import asyncio

class MongoDBAdapter:
    def __init__(self, collection):
        self.collection = collection

    async def create_order(self, order):
        # Set a unique ID for the order if not provided
        if "id" not in order or not order["id"]:
            order["id"] = str(ObjectId())
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, self.collection.insert_one, order)
        created_order = await loop.run_in_executor(
            None, self.collection.find_one, {"_id": result.inserted_id}
        )
        if created_order:
            created_order["_id"] = str(created_order["_id"])  # ObjectId in String umwandeln
        return created_order

    async def get_orders_by_email(self, email):
        """
        Findet alle Bestellungen für eine bestimmte Benutzer-E-Mail.
        """
        orders = await self.collection.find({"customer_email": email}).to_list(length=None)
        for order in orders:
            order["_id"] = str(order["_id"])  # ObjectId in String umwandeln
        return orders

    async def get_order(self, id):
        loop = asyncio.get_event_loop()
        order = await loop.run_in_executor(
            None, self.collection.find_one, {"_id": ObjectId(id)}
        )
        if order:
            order["_id"] = str(order["_id"])  # ObjectId in String umwandeln
        return order

    async def list_orders(self):
        loop = asyncio.get_event_loop()
        cursor = await loop.run_in_executor(None, self.collection.find)
        orders = await loop.run_in_executor(None, list, cursor)
        for order in orders:
            order["_id"] = str(order["_id"])  # ObjectId in String umwandeln
        return orders

    async def update_order(self, id, updates):
        loop = asyncio.get_event_loop()
        updated_order = await loop.run_in_executor(
            None,
            self.collection.find_one_and_update,
            {"_id": ObjectId(id)},
            {"$set": updates},
            return_document=ReturnDocument.AFTER,
        )
        if updated_order:
            updated_order["_id"] = str(updated_order["_id"])  # ObjectId in String umwandeln
        return updated_order

    async def delete_order(self, id):
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, self.collection.delete_one, {"_id": ObjectId(id)})
        return result.deleted_count  # Anzahl der gelöschten Dokumente zurückgeben
