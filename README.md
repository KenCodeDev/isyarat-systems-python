# Isyarat Systems

**Isyarat Systems** adalah sebuah program Python yang berfungsi sebagai **sistem deteksi isyarat tangan** menggunakan kamera secara real-time. Program ini mampu:

* Mendeteksi tangan dan wajah menggunakan MediaPipe.
* Mengidentifikasi bentuk jari (finger pose) untuk menentukan gestur tertentu.
* Menampilkan subtitle secara otomatis sesuai gestur yang terdeteksi.
* Mengucapkan teks subtitle menggunakan **text-to-speech (TTS)** berbasis **gTTS**.
* Memberikan tampilan visual dengan highlight, subtitle, FPS, dan nama author.
* Mengatur brightness dan contrast kamera.

Program ini cocok untuk demo interaksi berbasis gestur, edukasi, presentasi, atau proyek multimedia.

---

## ✨ Fitur Utama

* **Hand Gesture Recognition** (MediaPipe Hands)
* **Face Detection** (MediaPipe Face Detection)
* **Auto Subtitle Rendering**
* **Text-to-Speech** dengan gTTS + pygame
* **Real-time Overlay Display** (OpenCV)
* **Gesture Mapping ke Teks**
* **Auto Clean TTS Cache**
* **Support Multi-line Text Subtitle**

---

## 👤 Author

Program ini dibuat oleh:

**Kenichi Ichi**

---

## 📚 Library yang Digunakan

Program ini menggunakan beberapa library Python:

* **OpenCV (cv2)** — untuk kamera dan overlay tampilan
* **MediaPipe** — untuk deteksi tangan dan wajah
* **NumPy** — untuk operasi array
* **gTTS** — untuk text-to-speech (Google Text-to-Speech)
* **pygame** — untuk memutar file audio hasil TTS
* **threading** — agar TTS berjalan tanpa mengganggu proses kamera
* **time** — delay dan timing
* **random** — generate nama file TTS sementara
* **os** — manajemen file TTS temporary
* **colorsys** (di tobgr.py) — konversi warna HSL/HSV ke RGB/BGR

---

## 🐍 Versi Python yang Didukung

> **Wajib menggunakan Python versi 3.9 sampai 3.11**

Jika menggunakan versi **di bawah 3.9** atau **di atas 3.11**, beberapa library seperti MediaPipe atau pygame mungkin akan error atau tidak bisa diinstall.

---

## 📄 File Tambahan: tobgr.py

File ini berfungsi untuk mengonversi berbagai format warna seperti:

* RGB
* HEX
* HSL
* HSV

Menjadi format **BGR**, yang digunakan oleh OpenCV.

---

## 🔧 Cara Jalankan Program

1. Pastikan pakai **Python 3.9 - 3.11**
2. Install library yang diperlukan:

```bash
pip install opencv-python mediapipe pygame gTTS numpy
```

3. Jalankan program:

```bash
py main.py
```
atau
```bash
python main.py
```

---

## ❗ Catatan

* Program akan otomatis membuat dan menghapus file TTS sementara.
* Tekan **Q** atau **ESC** untuk keluar.
* Window "Isyarat Systems" bisa di-resize.
* Gesture mapping ada di fungsi `detect_gesture()`.

---

## ❤️ Terima kasih telah menggunakan Isyarat Systems!
