from flask import Flask, request, jsonify, render_template
from PIL import Image, ImageOps
import numpy as np
import base64
import re
from io import BytesIO
from tensorflow.keras.models import load_model
import traceback

app = Flask(__name__)
model = load_model("model.h5")

CLASSES = ['sun', 'hand', 'face', 'flower']

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fuzzy")
def fuzzy():
    return render_template("fuzzy.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json['image']
        match = re.search(r'base64,(.*)', data)
        if not match:
            return jsonify({'prediction': 'Invalid image format'})

        img_str = match.group(1)
        image_bytes = base64.b64decode(img_str)
        original = Image.open(BytesIO(image_bytes)).convert('L')
        img = ImageOps.invert(original)
        img = ImageOps.autocontrast(img)
        img = img.resize((28, 28), Image.Resampling.LANCZOS)

        img_array = np.array(img)/255.0
        img_array = img_array.reshape(1,28,28,1)

        pred = model.predict(img_array)[0]

        # Convert sigmoid outputs to percentages
        fuzzy_values = {CLASSES[i]: float(pred[i]*100) for i in range(len(CLASSES))}
        predicted_class = CLASSES[np.argmax(pred)]

        return jsonify({'prediction': predicted_class, 'fuzzy': fuzzy_values})

    except Exception as e:
        traceback.print_exc()
        return jsonify({'prediction': 'Error occurred'})

if __name__ == "__main__":
    app.run(debug=True)