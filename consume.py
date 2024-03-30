import pika
from time import sleep

# RabbitMQ connection details (replace with yours)
connection_parameters = pika.ConnectionParameters(
    host='localhost',
    port=5672,
    virtual_host='/',  # Replace with your virtual host if using one
    credentials=pika.PlainCredentials('bhavith', '1234')
)

def process_message(channel, method, properties, body):
    # This function will be called when a message is received
    print(f"Received message: {body.decode()}")

    # Replace this with your actual task processing logic
    print("Performing some task based on the received message...")
    sleep(5)  # Simulate some processing time

connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

# Define the exchange and routing key (optional, adjust as needed)
exchange_name = 'my_exchange'  # Replace with the same exchange name used in the publisher
routing_key = 'TEST_ROUTING_KEY'  # Replace with the same routing key used in the publisher

# Declare a queue to receive messages (optional, adjust as needed)
queue_name = channel.queue_declare("",exclusive=True).method.queue

# Bind the queue to the exchange with the specified routing key
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

# Set up the consumer
channel.basic_consume(queue=queue_name, on_message_callback=process_message, auto_ack=True)

print("Waiting for messages...")

channel.start_consuming()
