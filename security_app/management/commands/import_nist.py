import requests
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Importa vulnerabilidades desde la API de NIST"

    def handle(self, *args, **kwargs):
        self.stdout.write("🚀 Starting NIST vulnerability import...")

        # 🔹 API Key de NIST (Reemplázala con la tuya)
        API_KEY = "86c721dc-4e18-4306-bafb-c2c0fad14c50"

        # 🔹 URL de la API de NIST
        url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

        # 🔹 Parámetros de la consulta
        params = {
            "pubStartDate": "2025-03-20T23:49:27.000Z",
            "resultsPerPage": 5  
        }

        # 🔹 Encabezados con el API Key
        headers = {
            "X-Api-Key": API_KEY
        }

        try:
            # 🔹 Realizar la solicitud a la API
            response = requests.get(url, headers=headers, params=params)

            # 🔹 Verificar si la solicitud fue exitosa
            if response.status_code == 200:
                data = response.json()
                self.stdout.write("✅ Datos importados correctamente:")
                self.stdout.write(str(data))  # Muestra los datos recibidos en la consola
            else:
                self.stdout.write(f"❌ Error {response.status_code}: {response.text}")

        except requests.exceptions.RequestException as e:
            self.stdout.write(f"❌ Error al conectar con la API: {e}")

        self.stdout.write("✅ NIST vulnerability import completed.")
