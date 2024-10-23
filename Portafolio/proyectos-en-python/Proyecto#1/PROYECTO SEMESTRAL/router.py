import requests

# Información del router
ROUTER_IP = '192.168.0.1'
LOGIN_URL = f'http://{ROUTER_IP}/login'
WIFI_CONFIG_URL = f'http://{ROUTER_IP}/apply_settings'

# Credenciales de inicio de sesión
USERNAME = 'admin'
PASSWORD = 'admin'

# Iniciar sesión en el router
session = requests.Session()
login_data = {
    'username': USERNAME,
    'password': PASSWORD
}

response = session.post(LOGIN_URL, data=login_data)
response.raise_for_status()

# Verificar si el inicio de sesión fue exitoso
if 'login successful' not in response.text:
    print('Inicio de sesión fallido')
    exit()

# Datos de configuración Wi-Fi
wifi_config_data = {
    'ssid': 'MiRedWiFi',
    'password': '12345678',
    'security': 'WPA2'
}

# Enviar configuración Wi-Fi
response = session.post(WIFI_CONFIG_URL, data=wifi_config_data)
response.raise_for_status()

print('Configuración Wi-Fi aplicada correctamente')