import pickle
import tensorflow as tf
from keras.preprocessing import image
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np
import cv2 
    
global model

image_size = 200 

class_dict = {1:{'nama':'herpes','defi':'Herpes merupakan kelompok virus yang dapat menyebabkan infeksi. Infeksi virus ini umumnya di tandai dengan kulit kering, luka terbuka yang berair dan luka lepuh. Herpes Simplex Virus (HSV) dan Varicella- Zoster virus (VZ) adalah dua jenis virus penyakit herpes yang umum menyerang manusia. Herpes Simplex, yaitu penyakit yang disebabkan oleh infeksi virus herpes simplex tipe 1 dan 2 sedangkan Herpes Zoster, penyakit yang disebabkan oleh infeksi virus varicella-zoster atau virus yang berjenis sama dengan penyebab cacar air'},
              2:{'nama':'jerawat', 'defi':'Jerawat adalah gangguan pada kulit. Kondisi ini berhubungan dengan produksi minyak (sebum) yang terjadi secara berlebihan. Minyak berlebih bisa menyumbat pori-pori kulit. Pada setiap pori-pori kulit, terdapat folikel yang terdiri dari kelenjar minyak dan rambut. Jerawat terjadi ketika folikel rambut atau tempat tumbuhnya rambut tersumbat oleh minyak dan sel kulit mati.'},
              0:{'nama':'flek hitam', 'defi':'Flek hitam adalah masalah kulit yang ditandai dengan munculnya bintik hitam pada wajah, lengan, bahu dan bagian tubuh lainnya. Flek hitam sendiri merupakan kumpulan pigmen alami, atau melanin, yang berisi melanosome. Masalah kulit ini paling sering disebabkan oleh paparan sinar matahari atau sinar ultraviolet. Kondisi kulit tertentu atau efek samping dari obat juga bisa memicu timbulnya flek hitam.'},
              3:{'nama':'kutil', 'defi':'Kutil adalah benjolan kecil, berdaging pada kulit atau selaput lendir yang disebabkan oleh virus papiloma manusia.Kutil disebabkan oleh berbagai strain virus papiloma manusia. Strain yang berbeda dapat menyebabkan kutil di berbagai bagian tubuh. Kutil dapat menyebar dari satu bagian tubuh ke bagian lain, atau antarmanusia melalui kontak dengan kutil.'},
              4:{'nama':'tahi lalat', 'defi':'Tahi lalat adalah bintik kecil berwarna cokelat, agak kehiataman, dan terletak di atas permukaan kulit. Tahi lali muncul akibat pengelompokan sel-sel melanosit, sel penghasil zat warna kulit. Selain berwarna cokelat atau agak gelap, warna tahi lalat juga ada yang sama persis dengan warna kulit. Bentuknya ada yang bulat, oval, menonjol, atau datar. Tekstur permukaan tahi lalat juga bervariasi, ada yang halus atau kasar, bahkan beberapa di antaranya ada yang ditumbuhi bulu.'}}

def load():
    global model
    model = tf.keras.models.load_model('model/model_2.h5')
    # path = 'static/images/prediksi.jpeg'
    # data_foto = tf.keras.utils.load_img(path, target_size=(200, 200))


def prediksi(data):
    x = tf.keras.utils.img_to_array(data)
    x = np.expand_dims(x, axis=0)
    prediksi = model.predict(x)
    nilai_kecocokan = round(100 * (np.max(prediksi[0])), 2)
    # nilai_kecocokan = prediksi
    # nilai_kecocokan = np.argmax(prediksi)
    prediksi = np.argmax(prediksi)
    hasil_prediksi = class_dict[prediksi]['nama']
    pengertian = class_dict[prediksi]['defi']
    return hasil_prediksi, nilai_kecocokan, pengertian

