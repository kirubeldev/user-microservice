import pika
import json

RABBITMQ_URL = "amqp://guest:guest@localhost:5672/"

def get_connection():
    params = pika.URLParameters(RABBITMQ_URL)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    return connection, channel

def send_message(queue_name: str, message: dict):
    connection, channel = get_connection()
    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=json.dumps(message),
        properties=pika.BasicProperties(
            delivery_mode=2,  
        )
    )
    connection.close()
