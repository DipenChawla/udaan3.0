from get_model_op import TextSeg, ApplyTess
from queue_publisher import PikaChu
import os


class ApiMain:

    def __init__(self):
        self.tess_obj = ApplyTess()

    def start_process(self,image_path):
        req = {}

        tess_out = self.tess_obj.get_tess_op(image_path)
        req['invoice_no'] = tess_out
        req['store_address'] = tess_out
        req['store_name'] = tess_out
        req['invoice_date'] = tess_out
        req['image_name'] = image_path
        print(PikaChu().publish_to_queue(req))

