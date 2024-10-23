import requests
import ipaddress

def get_geolocation_by_ip(ip_address=None):
    if ip_address is None:
        # Obtener la dirección IP de la máquina
        response = requests.get('https://api.ipify.org?format=json')
        ip_address = response.json()['ip']

    # Verificar si la IP es privada
    if ipaddress.ip_address(ip_address).is_private:
        return {'error': 'Las direcciones IP privadas no tienen geolocalización pública'}

    # Obtener la geolocalización usando la dirección IP
    api_key = '1e736c6fa5b44d4fb43b4cbb84aefbd0'  # Tu clave de API
    url = f'https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_address}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            'IP': data['ip'],
            'País': data['country_name'],
            'Región': data['state_prov'],
            'Ciudad': data['city'],
            'Latitud': data['latitude'],
            'Longitud': data['longitude']
        }
    else:
        return {'error': 'No se pudo obtener la geolocalización'}

def main_menu():
    while True:
        print("Menú de Detección de Zona Geográfica")
        print("1. Ingresar manualmente una dirección IP")
        print("2. Obtener automáticamente la dirección IP de la máquina")
        print("3. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            ip_address = input("Ingrese la dirección IP: ")
            geo_info = get_geolocation_by_ip(ip_address)
            print("Geolocalización (Ingresada manualmente):", geo_info)
        elif choice == '2':
            geo_info = get_geolocation_by_ip()
            print("Geolocalización (Automática):", geo_info)
        elif choice == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main_menu()