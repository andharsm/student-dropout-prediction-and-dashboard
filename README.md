# **Prototype Prediksi & Dashboard Student Dropout Analysis**

![andharsm-dashboard](https://github.com/user-attachments/assets/88aa203f-146b-4a0c-bccf-469e60474087)


## **Business Understanding**

Dalam era digital dan globalisasi yang semakin berkembang, institusi pendidikan baik itu sekolah, universitas, lembaga kursus, hingga platform e-learning (ecourse) memiliki peran yang sangat penting dalam membentuk masa depan individu dan masyarakat. Semua jenis institusi ini menghadapi tantangan serupa dalam hal mempertahankan partisipasi dan kesuksesan peserta didiknya. Tingkat dropout yang tinggi merupakan salah satu masalah utama yang dapat menghambat misi institusi pendidikan tersebut.

Dropout adalah kondisi di mana peserta didik berhenti atau tidak menyelesaikan program pendidikan yang mereka ikuti. Ini dapat terjadi di berbagai tingkat pendidikan, mulai dari sekolah dasar hingga pendidikan tinggi, serta di berbagai jenis program pelatihan dan kursus. Fenomena ini dapat disebabkan oleh berbagai faktor seperti kesulitan akademik, masalah keuangan, kurangnya dukungan sosial, dan motivasi yang rendah.

Dampak dari tingkat dropout yang tinggi tidak hanya dirasakan oleh individu peserta didik, tetapi juga oleh institusi pendidikan itu sendiri. Bagi peserta didik, dropout dapat berarti hilangnya kesempatan untuk meraih pendidikan yang lebih baik dan peningkatan kualitas hidup. Bagi institusi pendidikan, tingkat dropout yang tinggi dapat mempengaruhi reputasi, pendanaan, dan kemampuan untuk menarik peserta didik baru. Oleh karena itu, sangat penting bagi setiap institusi pendidikan untuk memahami dan mengatasi masalah dropout ini.

Dengan mengembangkan sistem prediksi dan dashboard analisis dropout, institusi pendidikan dapat lebih proaktif dalam mengidentifikasi peserta didik yang berisiko tinggi dan mengambil langkah-langkah preventif yang tepat. Sistem ini bertujuan untuk membantu institusi dalam memahami faktor-faktor yang mempengaruhi dropout dan menyediakan data yang diperlukan untuk membuat keputusan yang informasional.

### Permasalahan Bisnis
* Bagaimana cara mengidentifikasi peserta didik yang berisiko tinggi untuk dropout dengan menggunakan data akademik dan non-akademik?
* Faktor-faktor apa saja yang paling mempengaruhi risiko dropout?
* Bagaimana membangun model prediksi yang akurat untuk mengidentifikasi peserta didik yang berisiko tinggi dropout?
* Metode atau algoritma apa yang paling efektif untuk digunakan dalam prediksi dropout?
* Apa saja langkah-langkah yang bisa diambil oleh institusi pendidikan untuk mencegah peserta didik berisiko tinggi dari dropout?

### Cakupan Proyek

* Analisis dan prediksi student dropout
* Pengembangan model machine learning untuk memprediksi attrition
* Identifikasi fitur importance
* Evaluasi dan pemilihan model terbaik
* Pembuata prototype prediksi
* Persiapan data untuk pembuatan dashboard
* Analisa Dashboard

### Sumber Data
Dataset yang digunakan adalah data student perfomance yang disediakan oleh Dicoding pada learning path Data Science kelas [Belajar Penerapan Data Science](https://www.dicoding.com/academies/590-belajar-penerapan-data-science).

### Setup Environment
a. Pastikan Python sudah terinstal di komputer Anda (disarankan Python 3.7+).
b. Buat virtual environment (opsional tapi direkomendasikan):
```
python -m venv myenv
source myenv/bin/activate  # Untuk Unix atau MacOS
myenv\Scripts\activate  # Untuk Windows
```
c. Instalasi requirements:
```
pip install -r requirements.txt
```

## **Business Dashboard**

Dashboard dibuat pada platform Looker Studio, dan dapat diakses pada [Dashboard Student Performance](https://lookerstudio.google.com/reporting/adec2a01-5c2b-4820-95b9-485581df7942)

### Pengaruh Beasiswa:
* Seluruh data: Dropout rate 39.15%
* Dengan beasiswa: Dropout rate 13.83%
* Tanpa beasiswa: Dropout rate 48.37%
* Kesimpulan: Beasiswa secara signifikan mengurangi tingkat dropout.

### Program Studi:
* Nursing konsisten memiliki tingkat dropout tertinggi di semua skenario.
* Social Service memiliki tingkat dropout rendah, terutama untuk penerima beasiswa.

### Usia:
* Mahasiswa yang lebih muda (18-20 tahun) cenderung memiliki tingkat dropout lebih tinggi.

### Nilai Kualifikasi vs Nilai Admisi:
* Ada korelasi positif antara nilai kualifikasi sebelumnya dan nilai admisi.
* Mahasiswa dropout cenderung memiliki nilai yang lebih rendah.

### Pembayaran:
* Mayoritas mahasiswa (baik lulusan maupun dropout) telah melakukan pembayaran.

### Nilai Kurikuler:
* Beberapa program studi menunjukkan penurunan nilai di semester kedua.

## **Menjalankan Sistem Machine Learning**

### Mengakses sistem via online
Prototype sistem machine learning student dropout prediction dapat diakses di: [student dropout prediction](https://student-dropout-prediction-and-dashboard.streamlit.app)

### Menjalankan di lokal
a. Pastikan Python sudah terinstal di komputer Anda (disarankan Python 3.7+).
b. Buat virtual environment (opsional tapi direkomendasikan):
```
python -m venv myenv
source myenv/bin/activate  # Untuk Unix atau MacOS
myenv\Scripts\activate  # Untuk Windows
```
c. Instalasi requirements:
```
pip install -r requirements.txt
```
d. Jalankan prototype prediksi
```
streamlit run dashboard/app.py
```

## **Conclusion**

* Beasiswa secara signifikan mengurangi tingkat dropout, menunjukkan bahwa dukungan finansial berperan penting dalam mempertahankan mahasiswa.
* Terdapat variasi tingkat dropout antar program studi, dengan beberapa program studi memerlukan perhatian khusus untuk mengurangi tingkat dropout.
* Usia muda merupakan faktor risiko dropout yang perlu diperhatikan, mungkin memerlukan intervensi tambahan untuk mendukung mahasiswa dalam kelompok usia ini.
* Nilai akademik yang lebih rendah sebelum dan saat masuk ke institusi dapat menjadi indikator awal risiko dropout.
* Penurunan nilai di semester kedua dapat menjadi indikator awal potensi dropout, sehingga diperlukan perhatian khusus untuk membantu mahasiswa yang mengalami penurunan performa akademik.

## **Rekomendasi Action Items**

### Peningkatan Program Beasiswa:
* Memperluas program beasiswa untuk mengurangi tingkat dropout secara keseluruhan.
* Fokus pada program studi dengan tingkat dropout tinggi, seperti Nursing.

### Program Mentoring Khusus:
* Implementasikan program mentoring untuk mahasiswa tahun pertama, terutama yang berusia 18-20 tahun.

### Evaluasi dan Penguatan Kurikulum:
* Analisis penyebab penurunan nilai di semester kedua untuk beberapa program studi.
* Tinjau dan sesuaikan kurikulum untuk memastikan transisi yang lebih baik antar semester.

### Peningkatan Proses Seleksi:
* Evaluasi ulang kriteria admisi, terutama untuk program studi dengan tingkat dropout tinggi.
* Pertimbangkan untuk memberikan bobot lebih pada nilai kualifikasi sebelumnya dalam proses seleksi.
