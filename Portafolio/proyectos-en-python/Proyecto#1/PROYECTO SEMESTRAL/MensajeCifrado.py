import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from cryptography.fernet import Fernet

# Configuración del correo electrónico
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = 'polancoomar18@gmail.com'
smtp_password = 'afcf meam mhru uoed'

# Direcciones de correo
sender_email = 'polancoomar18@gmail.com'
receiver_email = 'valeisaor@gmail.com'

# Generar clave de cifrado
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Texto a enviar
plain_text = "Este es el mensaje que sera cifrado y enviado."
encrypted_text = cipher_suite.encrypt(plain_text.encode())

# Función para enviar correo
def send_email(subject, body, to_email):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
            print(f"Correo enviado a {to_email}")
    except Exception as e:
        print(f"Error al enviar correo: {e}")

# Enviar correo con texto cifrado
send_email(
    subject="Texto Cifrado",
    body=f"El texto cifrado es: {encrypted_text.decode()}",
    to_email=receiver_email
)

# Enviar correo con texto plano y clave
send_email(
    subject="Texto Plano y Clave",
    body=f"El texto plano es: {plain_text}\nLa clave para descifrar es: {key.decode()}",
    to_email=receiver_email
)