import requests
import datetime

API_KEY = "86c721dc-4e18-4306-bafb-c2c0fad14c50"  

NIST_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

def fetch_nist_vulnerabilities():
    """ Obtiene vulnerabilidades recientes desde NIST """

    start_date = (datetime.datetime.utcnow() - datetime.timedelta(days=7)).isoformat() + "Z"

    headers = {
        "X-Api-Key": API_KEY  
    }

    params = {
        "pubStartDate": start_date,
        "resultsPerPage": 2  
    }

    try:
        response = requests.get(NIST_API_URL, headers=headers, params=params)
        
        if response.status_code == 404:
            print(" Error 404: La URL de la API no es válida o el endpoint ha cambiado.")
            print(" Verifica la documentación oficial: https://nvd.nist.gov/developers/vulnerabilities")
            return []
        
        response.raise_for_status()  # Maneja otros errores HTTP
        
        data = response.json()
        return data.get("vulnerabilities", [])

    except requests.exceptions.RequestException as err:
        print(f" Error en la solicitud: {err}")
        return []

def import_nist_vulnerabilities():
    """ Importa y muestra vulnerabilidades desde NIST """

    print("🚀 Iniciando importación de vulnerabilidades desde NIST...")

    vulnerabilities = fetch_nist_vulnerabilities()

    if vulnerabilities:
        print(f" Se encontraron {len(vulnerabilities)} vulnerabilidades.")
        for vuln in vulnerabilities:
            cve_id = vuln.get("cve", {}).get("id", "N/A")
            description = vuln.get("cve", {}).get("descriptions", [{}])[0].get("value", "Sin descripción")
            print(f" {cve_id}: {description}")
    else:
        print(" No se encontraron vulnerabilidades recientes.")

    print(" Importación completada.")

if __name__ == "__main__":
    import_nist_vulnerabilities()


