import cv2
import mediapipe as mp

# Inicializando os módulos (opencv e mediapipe)
webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
identificar_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho_rosto = mp.solutions.drawing_utils

while True:
    # Ler as informações da camera
    flag_verificador, frame = webcam.read()

    if not flag_verificador:
        break

    lista_rostos = identificar_rostos.process(frame)

    if lista_rostos.detections:
        for rostos in lista_rostos.detections:
            desenho_rosto.draw_detection(frame, rostos)

    cv2.imshow("IDENTIFICANDO ROSTOS ...", frame)

    # Exit em Esc que equivale a cod 27
    if cv2.waitKey(5) == 27:
        break

webcam.release()
cv2.destroyAllWindows()
