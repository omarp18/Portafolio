import socket
import yagmail

class PortScanner:
    def __init__(self, target_ip):
        self.target_ip = target_ip

    def scan_ports(self, start_port, end_port):
        open_ports = []
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((self.target_ip, port))
                if result == 0:
                    open_ports.append(port)
        return open_ports

    def scan_single_port(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((self.target_ip, port))
            return result == 0

class ReportGenerator:
    def __init__(self, open_ports):
        self.open_ports = open_ports

    def generate_report(self):
        report_lines = ["Ports Scan Report", "==================="]
        if self.open_ports:
            report_lines.append("Open Ports:")
            for port in self.open_ports:
                report_lines.append(f"Port {port}")
        else:
            report_lines.append("No open ports found.")
        return "\n".join(report_lines)

class EmailSender:
    def __init__(self, username, password, from_email, to_email):
        self.username = username
        self.password = password
        self.from_email = from_email
        self.to_email = to_email

    def send_email(self, subject, body):
        yag = yagmail.SMTP(self.username, self.password)
        try:
            yag.send(to=self.to_email, subject=subject, contents=body)
            print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")

def get_local_ip():
    # Obtener la IP local de la computadora
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Conectar a un servidor externo para obtener la IP local
        s.connect(("8.8.8.8", 80))  # Google DNS
        local_ip = s.getsockname()[0]
    except Exception as e:
        print(f"Error obtaining local IP: {e}")
        local_ip = None
    finally:
        s.close()
    return local_ip

def main():
    target_ip = get_local_ip()  # Obtener la IP local
    if not target_ip:
        print("Could not determine local IP address. Exiting.")
        return

    start_port = 20
    end_port = 1024

    # Crear un escáner de puertos
    scanner = PortScanner(target_ip)
    open_ports = scanner.scan_ports(start_port, end_port)

    # Generar el informe
    report_generator = ReportGenerator(open_ports)
    report = report_generator.generate_report()

    # Enviar el informe por correo electrónico
    username = "polancoomar18@gmail.com"  # Reemplaza con tu correo electrónico
    password = "afcf meam mhru uoed"  # Reemplaza con tu contraseña
    from_email = "polancoomar18@gmail.com"  # Reemplaza con tu correo electrónico
    to_email = "valeisaor@gmail.com"  # Reemplaza con el correo electrónico del destinatario

    email_sender = EmailSender(username, password, from_email, to_email)
    email_sender.send_email("Port Scan Report", report)

if __name__ == "__main__":
    main()