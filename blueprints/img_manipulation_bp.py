import json
from flask import Blueprint, request, jsonify, abort, Response
from core import Model
from core import image
import time
import os
import sys

img_manipulation_bp = Blueprint('img_manipulation', __name__)

model = Model('assets/exported-model')

@img_manipulation_bp.route("/tf-process-image", methods=["POST"])
def processImage():
    content = request.json
    response = {}
    b64image = content['image']['base64']
    if b64image == '' or b64image is None:
        response['error'] = "Image cannot be empty"
        return jsonify(response)
    start_time = time.time()
    b64image = b64image.replace('+', '-')
    b64image = b64image.replace('/', '_')
    try:
        predictedvalue = model.predict(b64image)
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        response['error'] = "Failed to process"
        return jsonify(response)
    response['imageOutput'] = image.asciiToB64(predictedvalue)
    response['elapsedTime'] = time.time() - start_time
    return jsonify(response)

