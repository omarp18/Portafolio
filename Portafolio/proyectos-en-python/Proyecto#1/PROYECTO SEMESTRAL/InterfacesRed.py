import os
import netifaces

class NetworkInterfaceLister:
    def __init__(self):
        self.interfaces = self._get_interfaces()

    def _get_interfaces(self):
        return netifaces.interfaces()

    def _get_interface_status(self):
        # Obtener la salida de ifconfig
        ifconfig_output = os.popen('ifconfig').read()
        interface_status = {}
        current_interface = None

        for line in ifconfig_output.split('\n'):
            if line and not line.startswith('\t'):
                current_interface = line.split(':')[0]
                interface_status[current_interface] = 'inactive'
            if 'status: active' in line:
                interface_status[current_interface] = 'active'
        
        return interface_status

    def list_interfaces(self):
        interface_status = self._get_interface_status()
        print("Interfaces de red disponibles:")
        for iface in self.interfaces:
            status = interface_status.get(iface, 'inactive')
            print(f"- {iface} ({status})")

# Uso de la clase
lister = NetworkInterfaceLister()
lister.list_interfaces()