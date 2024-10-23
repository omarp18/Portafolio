import cv2
import numpy as np

class FaceRecognizer:
    def __init__(self, face_cascade_path, model_path, label_map):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + face_cascade_path)
        self.label_map = label_map
        self.confidence_threshold = 50  # Ajusta este valor según sea necesario
        
        # Verifica si el módulo cv2.face está disponible
        try:
            self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        except AttributeError:
            print("Error: El módulo cv2.face no está disponible. Asegúrate de instalar opencv-contrib-python.")
            exit()
        
        # Carga el modelo entrenado
        self.recognizer.read(model_path)

    def recognize_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            label, confidence = self.recognizer.predict(roi_gray)

            name = "Desconocido"
            if confidence < self.confidence_threshold:
                for person_name, person_label in self.label_map.items():
                    if person_label == label:
                        name = person_name
                        break

            # Dibuja el recuadro alrededor del rostro
            color = (0, 255, 0) if name != "Desconocido" else (0, 0, 255)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

            # Ajusta la posición del texto para que aparezca fuera del recuadro
            text_size = cv2.getTextSize(name, cv2.FONT_HERSHEY_SIMPLEX, 0.9, 2)[0]
            text_x = x + (w - text_size[0]) // 2
            text_y = y - 10 if y - 10 > 10 else y + h + text_size[1] + 10

            # Dibuja el texto
            cv2.putText(frame, name, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        return frame

def main():
    label_map = {'Omar': 0, 'Alanis': 1, 'Valentina': 2}
    face_recognizer = FaceRecognizer('haarcascade_frontalface_default.xml', 'trainer.yml', label_map)
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara.")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: No se pudo leer el cuadro de video.")
            break

        frame = face_recognizer.recognize_faces(frame)

        cv2.imshow("Face Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()