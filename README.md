# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus. Nah, sebagai calon data scientist masa depan Anda diminta untuk membantu Jaya Jaya Institut dalam menyelesaikan permasalahannya. Mereka telah menyediakan dataset yang dapat Anda unduh melalui tautan berikut: students' performance. Selain itu, mereka juga meminta Anda untuk membuatkan dashboard agar mereka mudah dalam memahami data dan memonitor performa siswa.

### Permasalahan Bisnis

1. Tingginya tingkat dropout mahasiswa
2. Kesulitan mengidentifikasi mahasiswa yang berisiko dropout
3. Kurangnya metode dalam memonitoring performa mahasiswa

### Cakupan Proyek

1. Pengolahan dan analisis data mahasiswa
2. Exploratory data analysis
3. Pembuatan model machine learning
4. Pembuatan dashboard analisis
5. Pembuatan prototype prediksi dropout

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup environment:

```
Python 3.12.12
Library: pandas, numpy, scikit-learn, matplotlib, seaborn, streamlit
Visualisasi: Tableau Public
Model: Random Forest Classifier
```
Ikuti langkah-langkah dibawah untuk mempersiapkan environment proyek ini:
1. Membuat virtual environment dengan menjalankan perintah berikut di terminal
```
python -m venv venv
```

2. Mengaktifkan virtual environment dengan menjalankan perintah berikut

Windows
```
venv\Scripts\activate
```
macOS / Linux
```
source venv/bin/activate
```

3. Menginstall dependensi dengan menjalankan perintah berikut
```
pip install -r requirements.txt
```

4. Menjalankan notebook melalui perintah berikut
```
jupyter notebook notebook.ipynb
```

### Cara Menjalankan Sistem Machine Leaning

1. Pastikan semua dependensi sudah terinstall
2. Menjalankan aplikasi streamlit dengan perintah berikut
```
streamlit run app.py
```
3. Setelah perintah dijalankan, aplikasi akan otomatis terbuka di browser
4. Masukkan beberapa informasi mahasiswa seperti Age at Enrollment, Admission Grade, Curricular Units 1st Semester Approved, dan Curricular Units 2nd Semester Approved
5. Klik tombol Predict untuk melihat hasil prediksi

## Business Dashboard

Link Dashboard: https://public.tableau.com/views/StudentDropoutAnalysisDashboard_17738282207190/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

Chart yang dibuat:
1. KPI Total Students -> Menunjukkan jumlah total mahasiswa
2. KPI Total Dropout -> Menunjukkan jumlah mahasiswa yang mengalami dropout
3. KPI Dropout Rate -> Menunjukkan persentase mahasiswa yang mengalami dropout dibandingkan dengan total mahasiswa
4. KPI Graduate Rate -> Menunjukkan persentase mahasiswa yang berhasil menyelesaikan studi
5. Student Status Distribution -> Menunjukkan distribusi jumlah mahasiswa berdasarkan status akademik
6. Dropout by Gender -> Menunjukkan perbandingan distribusi status mahasiswa berdasarkan gender
7. Age at Enrollment vs Status -> Menunjukkan rata-rata usia mahasiswa saat pertama masuk kuliah berdasarkan status mahasiswa
8. Academic Performance vs Status -> Menunjukkan perbandingan performa akademik mahasiswa berdasarkan status mahasiswa

## Conclusion

Proyek ini bertujuan untuk menganalisis fenomena dropout mahasiswa di Jaya Jaya Institut serta mengidentifikasi faktor-faktor yang berkaitan dengan status akademik mahasiswa. Berdasarkan hasil analisis data, diketahui bahwa dari total 4.424 mahasiswa, sekitar 32,12% mengalami dropout, sementara sekitar 49,93% berhasil lulus dan sisanya masih berstatus enrolled. Angka tersebut menunjukkan bahwa dropout merupakan permasalahan yang cukup signifikan bagi institusi karena hampir sepertiga mahasiswa tidak menyelesaikan pendidikannya.

Hasil analisis visualisasi menunjukkan beberapa pola yang berkaitan dengan status mahasiswa. Distribusi status mahasiswa menunjukkan bahwa jumlah mahasiswa yang lulus lebih tinggi dibandingkan yang dropout, namun jumlah dropout masih tergolong besar. Analisis berdasarkan gender menunjukkan bahwa dropout terjadi pada kedua kelompok gender dengan pola yang relatif serupa. Selain itu, rata-rata usia saat pertama kali masuk kuliah pada mahasiswa yang dropout cenderung lebih tinggi dibandingkan mahasiswa yang berhasil lulus.

Dari sisi performa akademik, mahasiswa yang berhasil lulus memiliki rata-rata jumlah mata kuliah yang lulus pada semester pertama dan kedua lebih tinggi dibandingkan mahasiswa yang dropout. Sebaliknya, mahasiswa yang mengalami dropout menunjukkan performa akademik yang lebih rendah pada tahap awal perkuliahan. Hal ini menunjukkan bahwa performa akademik pada semester awal memiliki hubungan yang cukup kuat dengan keberhasilan mahasiswa dalam menyelesaikan studinya.

### Rekomendasi Action Items (Optional)

1. Meningkatkan pemantauan performa akademik mahasiswa
Institusi dapat melakukan pemantauan performa akademik mahasiswa secara lebih intensif, terutama pada semester satu dan semester dua perkuliahan.

2. Memberikan pendampingan akademik untuk mahasiswa yang berisiko dropout
Mahasiswa yang diprediksi memiliki risiko tinggi untuk droput dapat diberikan program pendampingan khusus, seperti mentoring oleh dosen pembimbing akademik ataupun konseling akademik.

3. Mengembangkan sistem deteksi risiko dropout
Institusi dapat mengetahui lebih awal mahasiswa yang berisiko dropout melalui model machine learning yang telah dibuat.

4. Meningkatkan program dukungan bagi mahasiswa pada semester awal
Institusi dapat memberikan atau membuat program dukungan tambahan untuk meningkatkan keberhasilan studi mahasiswa.
