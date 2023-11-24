import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='MyQueue', durable=True)
message = 'Hello, Roux de merde qui fait pas son taf a lheure'
channel.basic_publish(exchange='',
                      routing_key='MyQueue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2
                      ))
print(" [x] Sent %r" % message)
connection.close()