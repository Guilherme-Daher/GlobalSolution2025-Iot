import cv2
import mediapipe as mp
import time
import datetime
import threading
from playsound import playsound
import tkinter as tk

# Inicialização do MediaPipe
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5)

# Função para tocar o alarme em thread separada
def play_alarm():
    playsound('alarm.wav')

# Função para simular o acendimento de luz (janela branca)
def turn_on_light():
    window = tk.Tk()
    window.title("ALERTA DE MOVIMENTO")
    window.configure(bg='white')
    window.geometry("300x200")
    label = tk.Label(window, text="MOVIMENTO DETECTADO!", bg='white', fg='red', font=("Arial", 10, "bold"))
    label.pack(pady=50)
    window.after(3000, window.destroy)  # Luz "acende" por 3 segundos
    window.mainloop()

# Função para logar mensagem com data/hora
def log_detection():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[ALERTA] Movimento detectado em: {now}")

# Inicialização da câmera
cap = cv2.VideoCapture(0)

print(">>> Sistema de segurança iniciado. Aguarde... <<<")

# Controle para evitar múltiplos disparos simultâneos
motion_detected = False
last_detection_time = 0
cooldown = 5  # segundos entre detecções

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Conversão para RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Processamento com MediaPipe
    results = pose.process(rgb_frame)

    # Simulação de ambiente escuro (reduz brilho)
    dark_frame = cv2.convertScaleAbs(frame, alpha=0.3, beta=0)

    # Detecção de presença humana
    if results.pose_landmarks:
        current_time = time.time()
        if not motion_detected or (current_time - last_detection_time) > cooldown:
            motion_detected = True
            last_detection_time = current_time

            # Loga a detecção
            log_detection()

            # Alarme sonoro
            threading.Thread(target=play_alarm).start()

            # Simula acender luz
            threading.Thread(target=turn_on_light).start()

    else:
        motion_detected = False

    # Mostra o vídeo com efeito escuro
    cv2.imshow('Sistema de Segurança - Monitoramento', dark_frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        print(">>> Sistema de segurança finalizado. <<<")
        break

cap.release()
cv2.destroyAllWindows()

