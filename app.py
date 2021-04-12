from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from PIL import Image
from pix2tex import get_prediction

app = Flask(__name__)
cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def root():
  return "App is up!"


@app.route("/predict/latex", methods=['POST'])
@cross_origin()
def predict_latex():
    file = request.files['file']
    img = Image.open(file.stream)
    return jsonify({"prediction": get_prediction(img)})


app.run(host='0.0.0.0', port=8080, debug=True)
