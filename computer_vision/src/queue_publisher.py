import pika
import json

class PikaChu:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='cv2nlp')

    
    def publish_to_queue(self, message):
        self.channel.basic_publish(exchange='', routing_key='cv2nlp', body=json.dumps(message))

    def __del__(self):
        self.channel.close()

        self.connection.close()
