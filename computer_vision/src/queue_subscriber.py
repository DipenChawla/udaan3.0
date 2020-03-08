import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='cv2nlp')


def callback(ch, method, properties, body):
    '''
    import model_prediction function here
    '''
    print(json.loads(body))


if __name__ == "__main__":
    channel.basic_consume(queue='cv2nlp', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    
    channel.start_consuming()
