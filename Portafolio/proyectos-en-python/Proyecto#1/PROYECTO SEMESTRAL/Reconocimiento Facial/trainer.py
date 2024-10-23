import cv2
import numpy as np
import os

def load_images_and_labels(directory):
    labels = []
    images = []
    label_map = {}
    current_label = 0

    if not os.path.exists(directory):
        print(f"Error: El directorio {directory} no existe.")
        return images, labels, label_map

    for foldername in os.listdir(directory):
        folder_path = os.path.join(directory, foldername)
        if os.path.isdir(folder_path):
            if foldername not in label_map:
                label_map[foldername] = current_label
                current_label += 1
            
            for filename in os.listdir(folder_path):
                if filename.endswith(".jpg") or filename.endswith(".png"):
                    image_path = os.path.join(folder_path, filename)
                    if not os.path.isfile(image_path):
                        print(f"Error: El archivo {image_path} no existe.")
                        continue

                    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                    if image is None:
                        print(f"Error: No se pudo leer la imagen {image_path}.")
                        continue

                    image = preprocess_image(image)

                    labels.append(label_map[foldername])
                    images.append(image)

    print(f"Label map: {label_map}")
    print(f"Number of images: {len(images)}")
    print(f"Labels: {labels}")

    return images, np.array(labels), label_map

def preprocess_image(image):
    image = cv2.resize(image, (200, 200))  # Tamaño razonable
    image = cv2.equalizeHist(image)
    return image

def main():
    try:
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        print("cv2.face está disponible.")
    except AttributeError:
        print("Error: El módulo cv2.face no está disponible. Asegúrate de instalar opencv-contrib-python.")
        return

    # Ruta completa al directorio de imágenes
    desktop_path = os.path.expanduser("~/Desktop")
    images_directory = os.path.join(desktop_path, "dataset")  # Cambiado a "dataset"

    images, labels, label_map = load_images_and_labels(images_directory)
    if not len(images):  # Comprobar si la lista de imágenes está vacía
        print("No se pudieron cargar imágenes. Asegúrate de que el directorio contiene imágenes válidas.")
        return

    try:
        recognizer.train(images, labels)
        recognizer.save('trainer.yml')  # Guarda el modelo entrenado
        print("Modelo entrenado y guardado como 'trainer.yml'.")
    except Exception as e:
        print(f"Error al entrenar el modelo: {e}")

if __name__ == "__main__":
    main()