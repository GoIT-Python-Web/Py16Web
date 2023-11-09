import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

message = b'Hello World!!'
channel.basic_publish(exchange='', routing_key='hello', body=message)

print(f" [x] Sent '{message}'")
connection.close()
