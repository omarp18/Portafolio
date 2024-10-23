import cv2
import os

def capture_images(user_name):
    # Crear directorio para el usuario si no existe
    if not os.path.exists(f'dataset/{user_name}'):
        os.makedirs(f'dataset/{user_name}')
    
    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    sample_num = 0

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            sample_num += 1
            cv2.imwrite(f"dataset/{user_name}/{user_name}_{sample_num}.jpg", gray[y:y+h, x:x+w])
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.imshow('frame', img)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        elif sample_num >= 20:  # Capturar 20 muestras por usuario
            break

    cam.release()
    cv2.destroyAllWindows()

# Captura de imágenes para un usuario específico
capture_images('usuario3')