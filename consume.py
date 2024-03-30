import pika
import config

# RabbitMQ connection details (replace with yours)
connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    virtual_host="/",  # Replace with your virtual host if using one
    credentials=pika.PlainCredentials("bhavith", "1234"),
)


# Callback fucntion
def process_message(channel, method, properties, body):
    # This function will be called when a message is received
    print(f"Received message: {body.decode()}")


connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()


# Declare a queue to receive messages (optional, adjust as needed)
channel.queue_declare(config.MESSAGE_QUEUE_NAME, durable=True)

# Bind the queue to the exchange with the specified routing key
# channel.queue_bind(exchange=config.MESSAGE_EXCHANGE_NAME, queue=queue_name, routing_key=routing_key)

# Set up the consumer
channel.basic_consume(
    queue=config.MESSAGE_QUEUE_NAME, on_message_callback=process_message, auto_ack=True
)

print("Waiting for messages...")

channel.start_consuming()
