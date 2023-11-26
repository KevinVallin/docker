import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='MyQueue', durable=True)
message = 'Hello, message envoyé !'
channel.basic_publish(exchange='',
                      routing_key='MyQueue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2
                      ))
print(" [x] Sent %r" % message)
connection.close()
