# MoonSkin
MoonSkin merupakan aplikasi yang dapat membantu kita dalam mengidentifikasi jenis penyakit pada kulit wajah dengan mengunggah gambar penyakit kulit yang kita alami. MoonSkin dapat menjadi alternatif diagnosa  penyakit kulit jenis jerawat, kudis,...... . Aplikasi ini dapat digunakan oleh semua kalangan baik anak anak ataupun orang dewasa. Aplikasi ini dapat menghitung presentase jenis penyakit melalhi gambar yang kita unggah, sehingga anda dapat menangani permasalahan kulit anda dengan tepat.
Dengan menggunakan CNN dalam mengklasifikasikan penyakit menggunakan feature data citra 

Berikut ini adalah link model yang digunakan:
https://drive.google.com/drive/folders/1V7r8inTmd_njwmX0V-A75hP-dXqsqEyG?usp=sharing

Berikut ini dataset yang digunakan:
https://drive.google.com/drive/folders/1WQvjygkXbarQ-G4xF0-U2TXAl6sXt5eT?usp=share_link

Dataset yang digunakan merupakan data gambar dari jenis penyakit diatas dengan setiap gambar memiliki jumah 76 dan total image train adalah 3
Sebelum melakukan deploy aplikasi download model yang ada kemudian masukan model ke dalam folder model

Berikut ini file Jupyter dalam pembuatan model:
https://colab.research.google.com/drive/1Qw2IWLHEu7ZfK_8ZMvyagsHEjJ0eDROd?usp=sharing

Dengan menggunakan AI project cycle membuat model klasifikasi CNN 

Deskripksi 
1. app.py berisikan flask
2. model.py digunakan untuk memanggil model dan melakukan prediksi 
3. folder model berisikan model yang telah ditraining
4. templates berisikan file html dari halaman web
5. static berisikan folder css, image, dan JavaScript
