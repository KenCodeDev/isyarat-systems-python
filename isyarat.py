# ============================
# NOTES
# ============================
# File        : isyarat.py
# Author      : Kenichi Ichi
# Description : Sistem deteksi isyarat tangan dengan subtitle dan text-to-speech
# Python      : 3.11.9
# Libraries   : OpenCV, MediaPipe, gTTS, pygame, numpy
# 
# WAJIB MENGGUNAKAN PYTHON 3.9 - 3.11
# JIKA MENGGUNAKAN VERSI DI ATAS 3.11 DAN DIBAWAH 3.9, BISA JADI TERJADI ERROR PADA LIBRARY TERTENTU!
# ============================

import cv2
import mediapipe as mp
import numpy as np
from gtts import gTTS
import pygame
import threading
import time
import random
import os

# ============================
# CONFIGURATION
# ============================
author_name = "Kenichi Ichi"

teks1 = "Hello"
teks2 = "My name is"
teks3 = "Kenichi"
teks4 = "Ichi"
teks5 = "I am an Information Systems major\nfrom Binus University." # Note: \n itu untuk new line/baris baru
teks6 = "Nice to meet you!"
teks7 = "Love You All"

warna_subtitle = (60, 173, 3)  # FORMAT WAJIB BGR (BUKAN RGB), GUNAKAN py tobgr.py UNTUK MENGUBAH KODE WARNA RGB,HEX,HSL,HSV KALIAN KE BGR
warna_fps = (0, 255, 0)  # FORMAT WAJIB BGR (BUKAN RGB), GUNAKAN py tobgr.py UNTUK MENGUBAH KODE WARNA RGB,HEX,HSL,HSV KALIAN KE BGR
warna_author_teks = (255, 255, 0)  # FORMAT WAJIB BGR (BUKAN RGB), GUNAKAN py tobgr.py UNTUK MENGUBAH KODE WARNA RGB,HEX,HSL,HSV KALIAN KE BGR

# ============================
# INIT SUARA DULU
# ============================
TTS_DIR = "tts_temp_(auto_delete)"
os.makedirs(TTS_DIR, exist_ok=True)

pygame.mixer.init()
last_spoken = ""

def speak(text):
    global last_spoken
    if text == "" or text == last_spoken:
        return
    last_spoken = text

    def worker():
        if not pygame.mixer.get_init():
            return

        filename = os.path.join(TTS_DIR, f"tts_{random.randint(100000, 999999)}.mp3")

        try:
            tts = gTTS(text=text, lang="en")
            tts.save(filename)

            if not pygame.mixer.get_init():
                return

            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()

            while True:
                try:
                    if not pygame.mixer.get_init():
                        break
                    if not pygame.mixer.music.get_busy():
                        break
                    time.sleep(0.1)
                except pygame.error:
                    break

        finally:
            try:
                if os.path.exists(filename):
                    os.remove(filename)
            except:
                pass


    threading.Thread(target=worker, daemon=True).start()

# ============================
# MEDIAPIPE INIT
# ============================
mp_hands = mp.solutions.hands
mp_face = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
face = mp_face.FaceDetection(model_selection=0, min_detection_confidence=0.5)

# ============================
# CAMERA INIT
# ============================
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FPS, 30)


def cleanup_tts_files():
    try:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    except:
        pass

    time.sleep(0.2)

    if not os.path.exists(TTS_DIR):
        return

    for f in os.listdir(TTS_DIR):
        try:
            os.remove(os.path.join(TTS_DIR, f))
        except:
            pass

    try:
        os.rmdir(TTS_DIR)
    except:
        pass


def adjust_brightness_contrast(frame, brightness=0, contrast=0):
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow) / 255
        gamma_b = shadow
        
        frame = cv2.addWeighted(frame, alpha_b, frame, 0, gamma_b)
    
    if contrast != 0:
        f = 131 * (contrast + 127) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127 * (1 - f)
        
        frame = cv2.addWeighted(frame, alpha_c, frame, 0, gamma_c)
    
    return frame

cv2.namedWindow("Isyarat Systems", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Isyarat Systems", 1280, 720)

# ============================
# SUBTITLE
# ============================
subtitle = ""
alpha = 0

# ============================
# FINGER COUNTER
# ============================
def count_fingers(hand):
    tips = [4, 8, 12, 16, 20]
    f = []
    
    if hand.landmark[tips[0]].x < hand.landmark[tips[0] - 1].x:
        f.append(1)
    else:
        f.append(0)
    
    for i in range(1, 5):
        if hand.landmark[tips[i]].y < hand.landmark[tips[i] - 2].y:
            f.append(1)
        else:
            f.append(0)
    
    return f

# ============================
# GESTURE DETECTION
# ============================
def detect_gesture(f, handLM):
    if f == [1, 1, 0, 0, 0]:
        thumb_tip = handLM.landmark[4]
        index_tip = handLM.landmark[8]
        
        if index_tip.y < thumb_tip.y and abs(index_tip.x - thumb_tip.x) < 0.1:
            return teks7
    
    if f == [1, 1, 1, 1, 1]: return teks1
    if f == [0, 1, 0, 0, 0]: return teks2
    if f == [0, 1, 1, 0, 0]: return teks3
    if f == [0, 1, 1, 1, 0]: return teks4
    if f == [0, 0, 0, 0, 0]: return teks5
    if f == [1, 1, 0, 0, 1]: return teks6
    
    return ""

# ============================
# MULTI-LINE TEXT DISPLAY
# ============================
def put_multi_line_text(frame, text, x, y, font_scale, color, thickness):
    lines = text.split('\n')
    y_offset = y
    
    for line in lines:
        cv2.putText(frame, line, (x, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness, cv2.LINE_AA)
        y_offset += int(40 * font_scale)

# ============================
# MAIN LOOP
# ============================
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    frame = cv2.flip(frame, 1)
    frame = adjust_brightness_contrast(frame, brightness=20, contrast=10)
    h, w, _ = frame.shape
    
    face_res = face.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if face_res.detections:
        for det in face_res.detections:
            box = det.location_data.relative_bounding_box
            x, y = int(box.xmin * w), int(box.ymin * h)
            bw, bh = int(box.width * w), int(box.height * h)
            cv2.rectangle(frame, (x, y), (x + bw, y + bh), (0, 255, 255), 2)
    
    gesture_text = ""
    hand_res = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    if hand_res.multi_hand_landmarks:
        for handLM in hand_res.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLM, mp_hands.HAND_CONNECTIONS)
            f = count_fingers(handLM)
            gesture_text = detect_gesture(f, handLM)
    
    if gesture_text != "":
        subtitle = gesture_text
        alpha = 255
        speak(subtitle)
    
    if alpha > 0:
        overlay = frame.copy()
        put_multi_line_text(overlay, subtitle, 50, h - 100, 1.6, warna_subtitle, 3)
        frame = cv2.addWeighted(overlay, alpha / 255, frame, 1 - alpha / 255, 0)
        alpha -= 4
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, warna_fps, 2)
    
    cv2.putText(frame, "Kenichi Ichi", 
                (10, h - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, warna_author_teks, 1, cv2.LINE_AA)
    
    cv2.imshow("Isyarat Systems", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        cleanup_tts_files()
        break
    elif key == ord('+'):
        frame = adjust_brightness_contrast(frame, brightness=30, contrast=0)
    elif key == ord('-'):
        frame = adjust_brightness_contrast(frame, brightness=-30, contrast=0)

    if cv2.getWindowProperty("Isyarat Systems", cv2.WND_PROP_VISIBLE) < 1:
        cleanup_tts_files()
        break

cap.release()
cv2.destroyAllWindows()
