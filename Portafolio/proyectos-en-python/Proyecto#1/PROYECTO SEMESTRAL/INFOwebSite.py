# Importa los módulos necesarios
import socket
import dns.resolver

# Define la clase WebInfoRetriever
class WebInfoRetriever:
    def __init__(self, urlAddress):
        self.urlAddress = urlAddress

    def getIpV4Address(self):
        try:
            ipV4 = socket.gethostbyname(self.urlAddress)
            return ipV4
        except socket.error as e:
            return str(e)

    def getIpV6Address(self):
        try:
            ipv6_addresses = [addr for addr in socket.getaddrinfo(self.urlAddress, None, socket.AF_INET6)]
            return [addr[4][0] for addr in ipv6_addresses]
        except socket.error as e:
            return str(e)

    def getServerName(self):
        try:
            # Esto puede devolver múltiples nombres, así que se devuelve el primero encontrado
            result = dns.resolver.resolve(self.urlAddress, 'A')
            return result[0].to_text()
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN) as e:
            return str(e)

    def getServerZone(self):
        try:
            result = dns.resolver.resolve(self.urlAddress, 'NS')
            return [str(rdata) for rdata in result]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN) as e:
            return str(e)

# Ejemplo de uso
url = 'google.com'  # Aquí se pone la dirección URL que deseas consultar
web_info = WebInfoRetriever(url)

print("IPv4 Address:", web_info.getIpV4Address())
print("IPv6 Address:", web_info.getIpV6Address())
print("Server Name:", web_info.getServerName())
print("Server Zone:", web_info.getServerZone())