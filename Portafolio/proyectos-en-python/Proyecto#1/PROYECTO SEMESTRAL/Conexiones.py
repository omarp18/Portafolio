import psutil
from scapy.all import ARP, Ether, srp, conf

class NetworkScanner:
    def __init__(self):
        self.ipRange = self.getIpRange()
    
    def getIpRange(self):
        for iface, addrs in psutil.net_if_addrs().items():
            ipv4_addresses = [addr.address for addr in addrs if addr.family == 2]  # AF_INET (IPv4)
            if ipv4_addresses:
                # Tomar la primera dirección IPv4 encontrada
                ipAddress = ipv4_addresses[0]
                # Intentar obtener la máscara de red para esta interfaz
                netmask = next((addr.netmask for addr in addrs if addr.family == 2), None)
                if ipAddress and netmask and not ipAddress.startswith("127."):
                    # Calcular el rango de IP basado en la dirección IP y la máscara de red
                    ipParts = ipAddress.split('.')
                    netmaskParts = netmask.split('.')
                    network = ".".join(str(int(ipParts[i]) & int(netmaskParts[i])) for i in range(4))
                    ipRange = f"{network}/{sum([bin(int(x)).count('1') for x in netmaskParts])}"
                    return ipRange
        print("No se pudo determinar el rango IP de ninguna interfaz activa.")
        return None

    def scanNetwork(self):
        if not self.ipRange:
            return []
        try:
            arpRequest = ARP(pdst=self.ipRange)
            etherFrame = Ether(dst="ff:ff:ff:ff:ff:ff")
            packet = etherFrame / arpRequest
            result = srp(packet, timeout=2, verbose=False)[0]
            return result
        except Exception as e:
            print(f"Error al escanear la red: {e}")
            return []

    def listConnectedDevices(self):
        result = self.scanNetwork()
        devices = []
        for sent, received in result:
            devices.append({'ip': received.psrc, 'mac': received.hwsrc})
        return devices

    def displayDevices(self):
        devices = self.listConnectedDevices()
        if devices:
            print("Dispositivos conectados a la red:")
            for device in devices:
                print(f"IP: {device['ip']}, MAC: {device['mac']}")
        else:
            print("No se encontraron dispositivos conectados.")

# Ejemplo de uso
if __name__ == "__main__":
    scanner = NetworkScanner()
    scanner.displayDevices()
