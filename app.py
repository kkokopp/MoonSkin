# import sklearn
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from model import load, prediksi
from PIL import Image
import cv2
import tensorflow as tf
# from model import load, prediksi
UPLOAD_FOLDER = os.path.join('static', 'images')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# load model dan scaler
load()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

@app.route('/diagnosa', methods=["GET", "POST"])
def diagnosa():
    # menangkap data yang diinput user melalui form
    if request.method == "POST":
        foto = request.files['image_kulit']
        img_filename = secure_filename('prediksi.jpeg')
        foto.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))
        path = 'static/images/prediksi.jpeg'
        data = tf.keras.utils.load_img(path, target_size=(224, 224))
        prediction_result, cofidence, pengertian = prediksi(data)
        return render_template('diagnosa1.html', hasil_prediksi=prediction_result, nilai_kecocokan=cofidence, pengertian=pengertian)
    
    return render_template('diagnosa1.html')

    # melakukan prediksi menggunakan model yang telah dibuat

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)