import pika

# RabbitMQ connection details (replace with yours)
connection_parameters = pika.ConnectionParameters(
    host='localhost',
    port=5672,
    virtual_host='/',  # Replace with your virtual host if using one
    credentials=pika.PlainCredentials('bhavith', '1234')
)

# Connect to RabbitMQ
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

# Define the exchange and routing key (optional, adjust as needed)
exchange_name = 'my_exchange'  # Replace with your desired exchange name
routing_key = 'TEST_ROUTING_KEY'  # Replace with the message you want to listen for

# Message to publish
message = "This is the message to trigger the task!"

# Publish the message
channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message.encode())

print(f"Message published to exchange '{exchange_name}' with routing key '{routing_key}'")

connection.close()
