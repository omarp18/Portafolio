import scapy.all as scapy
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class NetworkAnalyzer:
    def __init__(self, emailRecipient):
        self.trafficCapture = TrafficCapture()
        self.patternDetector = PatternDetector()
        self.reportGenerator = ReportGenerator()
        self.emailSender = EmailSender(emailRecipient)

    def startAnalysis(self):
        capturedPackets = self.trafficCapture.captureTraffic()
        suspiciousPatterns = self.patternDetector.detectPatterns(capturedPackets)
        report = self.reportGenerator.generateReport(suspiciousPatterns)
        self.emailSender.sendEmail(report)

class TrafficCapture:
    def captureTraffic(self):
        print("Capturando tráfico de red...")
        # Captura 100 paquetes como ejemplo; ajusta según tus necesidades
        packets = scapy.sniff(count=100)  
        return packets

class PatternDetector:
    def detectPatterns(self, packets):
        print("Detectando patrones sospechosos...")
        # Lógica para detectar patrones sospechosos en los paquetes capturados
        suspiciousPatterns = []
        for packet in packets:
            if packet.haslayer(scapy.TCP) and packet[scapy.TCP].flags == 'S':
                suspiciousPatterns.append(f"SYN packet detected from {packet[scapy.IP].src}")
        return suspiciousPatterns

class ReportGenerator:
    def generateReport(self, suspiciousPatterns):
        print("Generando informe...")
        if not suspiciousPatterns:
            return "No se detectaron patrones sospechosos."
        report = "Informe de análisis de tráfico:\n"
        for pattern in suspiciousPatterns:
            report += f"{pattern}\n"
        return report

class EmailSender:
    def __init__(self, recipientEmail):
        self.recipientEmail = recipientEmail

    def sendEmail(self, report):
        print(f"Enviando informe a {self.recipientEmail}...")
        senderEmail = "polancoomar18@gmail.com"
        password = "afcf meam mhru uoed"  # Utiliza una contraseña de aplicación si usas Gmail

        msg = MIMEMultipart()
        msg['From'] = senderEmail
        msg['To'] = self.recipientEmail
        msg['Subject'] = "Informe de Análisis de Tráfico de Red"
        
        msg.attach(MIMEText(report, 'plain'))
        
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(senderEmail, password)
            text = msg.as_string()
            server.sendmail(senderEmail, self.recipientEmail, text)
            server.quit()
            print("Informe enviado exitosamente.")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")

# Ejemplo de uso:
emailRecipient = "valeisaor@gmail.com"
networkAnalyzer = NetworkAnalyzer(emailRecipient)
networkAnalyzer.startAnalysis()
