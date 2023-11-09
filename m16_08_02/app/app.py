import json
from datetime import datetime

import pika

from models import Task

credentials = pika.PlainCredentials("pglbwiuh", "*****")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="sparrow-01.rmq.cloudamqp.com",
        port=5672,
        credentials=credentials,
        virtual_host="pglbwiuh",
    )
)
channel = connection.channel()

exchange = "Web16 Service"
queue_name = "web_16_campaign"

channel.exchange_declare(exchange=exchange, exchange_type="direct")
channel.queue_declare(queue=queue_name, durable=True)
channel.queue_bind(exchange=exchange, queue=queue_name)


def create_tasks(nums: int):
    for i in range(nums):
        task = Task(consumer="Noname").save()

        channel.basic_publish(
            exchange=exchange,
            routing_key=queue_name,
            body=str(task.id).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )

    connection.close()


if __name__ == "__main__":
    create_tasks(1000)
