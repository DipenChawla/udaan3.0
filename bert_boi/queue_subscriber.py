import pika
import json
import os
from bert import Ner


from extract_address import extract_store_address

from extract_store import extract_store_name

from extract_invoice import extract_invoice 

from extract_date import DateParser
username= os.getenv('RBMQ_USR')
password = os.getenv('RBMQ_PASS')

model = Ner('out_base/')
credentials = pika.PlainCredentials(username, password)

connection = pika.BlockingConnection(pika.ConnectionParameters('3.91.55.83',5672,'/', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='cv2nlp')


def callback(ch, method, properties, body):
    '''
    import model_prediction function herei
    '''
    resp_json = json.loads(body))

    extract_invoice(resp_json['invoice_no'])
    extract_store_address(resp_json['store_address'])
    extract_store_name(resp_json['store_name'])
    DateParser().get_custom_date(resp_json['invoice_date'])

if __name__ == "__main__":
    channel.basic_consume(queue='cv2nlp', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel.start_consuming()                             
