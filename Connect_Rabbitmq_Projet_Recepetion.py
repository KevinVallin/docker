import pika

def call_back(ch, method, properties, body):
    print(" [x] Received %r" % body)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='MyQueue', durable=True)
channel.basic_consume(queue='MyQueue', on_message_callback= call_back, auto_ack=True)
print(' [*] En attente de votre message. Faite controle+C pour manger tes grands morts')
channel.start_consuming()