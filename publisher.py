import pika
import config

# RabbitMQ connection details (replace with yours)
connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    virtual_host="/",  # Replace with your virtual host if using one
    credentials=pika.PlainCredentials(
        "bhavith", "1234"
    ),  # This is Optional/ use this only if there is credentials
)

# Connect to RabbitMQ
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

# Creating a Queue
channel.queue_declare(queue=config.MESSAGE_QUEUE_NAME, durable=True)

# Message to publish
message = "Hello Test Queue 111!"

# Publish the message
channel.basic_publish(
    exchange=config.MESSAGE_EXCHANGE_NAME,
    routing_key=config.MESSAGE_QUEUE_NAME,
    body=message,
    properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent), #Optional Persist data
)

print(
    f"Message published to exchange '{config.MESSAGE_EXCHANGE_NAME}' with routing key '{config.MESSAGE_QUEUE_NAME}'"
)

connection.close()
