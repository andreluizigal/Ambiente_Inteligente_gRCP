import pika

from time import sleep

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = 'luminosity'
message = '25' #teste

while True:
    try:
        channel.basic_publish(
            exchange='topic_logs', routing_key=routing_key, body=message)
        print(" [x] Sent %r:%r" % (routing_key, message))
        sleep(5)
    
    except: connection.close()
