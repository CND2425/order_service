class OrderUseCases:
    def __init__(self, db_adapter, mq_adapter):
        self.db_adapter = db_adapter
        self.mq_adapter = mq_adapter

    async def create_order(self, order):
        # Bestellung erstellen
        created_order = await self.db_adapter.create_order(order)
        # Nachricht an RabbitMQ senden
        for item in order["items"]:
            await self.mq_adapter.publish_order_update(product_id=item["product_id"], quantity=item["quantity"])
        return created_order

    async def get_order(self, id):
        return await self.db_adapter.get_order(id)

    async def list_orders(self):
        return await self.db_adapter.list_orders()

    async def update_order(self, id, updates):
        return await self.db_adapter.update_order(id, updates)

    async def delete_order(self, id):
        return await self.db_adapter.delete_order(id)

    async def list_orders_by_email(self, email):
        """
        Gibt alle Bestellungen eines Benutzers basierend auf der E-Mail zurück.
        """
        return await self.db_adapter.get_orders_by_email(email)
