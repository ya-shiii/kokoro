from django.conf import settings
import requests
import json

class Lioren:
    token = str(settings.LIOREN_TOKEN)

    def login(self):  
        url = "https://www.lioren.cl/api/whoami"
        headers = {
                'Content-Type': 'application/json',
                'Authorization': "Bearer "+self.token
        }
        response = requests.get(url, headers=headers)
        print(response.text)
        if response.status_code != 200:
            return False
        return response.json()

    def registrarBoleta(self,productos, receptor):  
        url = "	https://www.lioren.cl/api/boletas"
        datos = {"emisor": {"tipodoc":"39",
                            "servicio":3},
                "receptor": receptor,
                "detalles":productos,
                "exento":False
            }
        headers = {
                'Accept':'application/json',
                'Content-Type': 'application/json',
                'Authorization': "Bearer "+self.token
                }
        response = requests.post(url, headers=headers, data=json.dumps(datos))
        if response.status_code != 200:
            print(response)
            print(self.token)
            return False
        return response.json()

    def getBoleta(self, folio):
        url = "	https://www.lioren.cl/api/boletas"
        datos = {"tipodoc":"39",
                "folio":folio
            }
        headers = {
                'Accept':'application/json',
                'Content-Type': 'application/json',
                'Authorization': "Bearer "+self.token
                }
        response = requests.get(url, headers=headers, data=json.dumps(datos))
        if response.status_code != 200:
            return False
        return response.json()
    

