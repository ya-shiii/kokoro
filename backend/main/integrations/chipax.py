from django.conf import settings
import requests
import json

class Chipax:
    app_id = str(settings.CHIPAX_ID)
    secret_key = str(settings.CHIPAX_KEY)
    
    def login(self):  
        url = "https://api.chipax.com/login"
        payload = {'app_id': self.app_id,
                   'secret_key': self.secret_key}
        headers = {
                'Content-Type': 'application/json'
        }
        response = requests.post(url, json= payload, headers=headers)
        result = response.json()
        return result['token']


    def facturas(self, token):
        url = 'https://api.chipax.com/dtes'
        headers = {
                  'Authorization': 'JWT ' + token
                  }
        response = requests.get(url, headers=headers)
        result = response.json()
        return result
    
    def clientes(self, token, rut):
        url = 'https://api.chipax.com/clientes/' + rut
        headers = {
                  'Authorization': 'JWT ' + token
                  }
        response = requests.get(url, headers=headers)
        result = response.json()
        return result


    def productos(self, token):
        url = 'https://api.chipax.com/productos'
        headers = {
                  'Authorization': 'JWT ' + token
                  }
        response = requests.get(url, headers=headers)
        result = response.json()
        return result


    def createNotasVenta(self, token, payload):
        url = 'https://api.chipax.com/notas-venta'
        headers = {
                  'Content-Type': 'application/json',
                  'Authorization': 'JWT ' + token
                  }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        return response.json()
    
    def crearCliente(self, token, payload):
        url = 'https://api.chipax.com/clientes'
        headers = {
                  'Authorization': 'JWT ' + token
                  }
        response = requests.post(url, headers=headers, data=payload)
        return response.json()