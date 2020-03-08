from PIL import Image
import pytesseract

class TextSeg:
    def __init__(self):
        '''
        initiate the model function
        '''
        pass
    
    def get_predictions(self):
        '''
        model.predict
        return predictions
        '''
        pass

class ApplyTess:
    def __init__(self):

        self.text_seg = TextSeg()

        final_dictionary = {}
        
        final_dictionary['invoice_no'] = None

        final_dictionary['store_address'] = None

        final_dictionary['store_name'] = None

        final_dictionary['invoice_date'] = None

    def get_tess_op(self, image_path):
        img = Image.open(image_path)
        img = img.convert('RGBA')
        text = pytesseract.image_to_string(img)
        return text
    
    def sanitize_predictions(self, model_op_dict):
        return {k:v.lower() for k,v in model_op_dict.items()}

# if __name__ == "__main__":
#     pass
