from flask import Flask, request, jsonify, render_template
import json
import datetime
from PIL import Image
from main import ApiMain
from io import BytesIO
from flask_cors import CORS, cross_origin

app = Flask(__name__)


CORS(app)

@app.route("/get_stuff", methods=["POST"])
def get_images():
    try:
        print(request.get())
        json_dict = request.args
        image_base64 = json_dict['image_array']
        file_name = str(datetime.datetime.now())

        im1 = Image.open(BytesIO(base64.b64decode(array_received)))
        im1 = im1.save(file_name)
        with open(file_name, "wb") as fh:
            fh.write(img_data.decode(image_base64))
#        ApiMain().start_process(file_name)

        return jsonify({'status':1})
    except Exception as e:
        print(e)
        return jsonify({'status':0})

if __name__ =="__main__":
    app.run(host="0.0.0.0", port=8086,threaded=True)
