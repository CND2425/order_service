import pika
import json


class RabbitMQAdapter:
    def __init__(self, rabbitmq_url):
        self.rabbitmq_url = rabbitmq_url

    async def publish_order_update(self, product_id, quantity):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.rabbitmq_url))
        channel = connection.channel()
        channel.queue_declare(queue='order_updates', durable=True)

        message = json.dumps({"product_id": product_id, "quantity": quantity})
        channel.basic_publish(exchange='', routing_key='order_updates', body=message)

        print(f"Published message to RabbitMQ: {message}")
        connection.close()

