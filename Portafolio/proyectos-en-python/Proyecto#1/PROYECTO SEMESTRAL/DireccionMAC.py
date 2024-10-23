import netifaces

class MacAddressRetriever:
    def __init__(self, interface='en0'):
        self.interface = interface
        self.mac_address = self._get_mac_address()

    def _get_mac_address(self):
        try:
            mac_address = netifaces.ifaddresses(self.interface)[netifaces.AF_LINK][0]['addr']
            return mac_address
        except KeyError:
            return 'No se pudo obtener la dirección MAC'

    def display_mac_address(self):
        print(f"La dirección MAC de esta máquina es: {self.mac_address}")

# Uso de la clase
retriever = MacAddressRetriever()
retriever.display_mac_address()