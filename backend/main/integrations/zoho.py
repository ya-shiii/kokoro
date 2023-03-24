from os import access
from django.conf import settings
import requests
from main.models import zoho
import json

class zohoc: 
    zoho_info = zoho.objects.all().latest('id')
    org = '774498621'
    client_id = str(settings.CLIENDID)
    clint_access = str(settings.CLIENTSECRET)

    def __init__(self):
        url = 'https://inventory.zoho.com/api/v1/organizations?organization_id='+ self.org
        headers = {
        'Authorization': 'Zoho-oauthtoken ' + self.zoho_info.access_token,
        'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers)
        result = response.json()
        if result['code'] > 1:
            url = 'https://accounts.zoho.com/oauth/v2/token?'
            # headers = {
            #     'Authorization': 'Zoho-oauthtoken ' + self.zoho_info.access_token
            #     }
            print(self.client_id, self.clint_access)
            param = {'refresh_token': self.zoho_info.refresh_token,
                     'client_id' : str(self.client_id),
                     'client_secret': self.clint_access,
                     'grant_type': 'refresh_token'
                     }
            response = requests.post(url, headers=headers, params=param)
            print(response.url)
            print(response.text)
            data = response.json()
            print('refresh code response')
            print(data)
            if data['access_token']:
                token = zoho(access_token=data['access_token'], refresh_token=self.zoho_info.refresh_token)
                token.save()
                self.zoho_info = zoho.objects.all().latest('id')

    def createContact(self, payload_contact):
        url = 'https://inventory.zoho.com/api/v1/contacts?organization_id=' + self.org
        headers = {
                    'Authorization': 'Zoho-oauthtoken ' + self.zoho_info.access_token,
                    'Content-Type': 'application/json'
                    }
        payload = payload_contact
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        result = response.json()
        return result

    def createProduct(self, payload_product):
        url = 'https://inventory.zoho.com/api/v1/items?organization_id=' + self.org
        headers = {
                    'Authorization': 'Zoho-oauthtoken ' + self.zoho_info.access_token,
                    'Content-Type': 'application/json'
                    }
        payload = payload_product
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        result = response.json()
        return result

    def createOrder(self, payload_order):
        url = 'https://inventory.zoho.com/api/v1/salesorders?organization_id=' + self.org
        headers = {
                    'Authorization': 'Zoho-oauthtoken ' + self.zoho_info.access_token,
                    'Content-Type': 'application/json'
                    }
        payload = payload_order
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        result = response.json()
        return result

    def getAllProduct(self):
        url = 'https://inventory.zoho.com/api/v1/items?organization_id=' + self.org
        headers = {
                    'Authorization': 'Zoho-oauthtoken ' + self.zoho_info.access_token,
                    'Content-Type': 'application/json'
                    }
        response = requests.get(url, headers=headers)
        result = response.json()
        return result
    
    def get_Product(self, item_id):
        url = 'https://inventory.zoho.com/api/v1/items/' + item_id + '?organization_id=' + self.org
        headers = {
                    'Authorization': 'Zoho-oauthtoken ' + self.zoho_info.access_token,
                    'Content-Type': 'application/json'
                    }
        response = requests.get(url, headers=headers)
        result = response.json()
        return result

    def getContactByName(self, name):
        url = 'https://inventory.zoho.com/api/v1/contacts?contact_name=' + str(name) +  '&organization_id=' + self.org
        headers = {
                    'Authorization': 'Zoho-oauthtoken ' + self.zoho_info.access_token,
                    'Content-Type': 'application/json'
                    }
        response = requests.get(url, headers=headers)
        result = response.json()
        return result

    def confirmOrder(self, id):
        url = 'https://inventory.zoho.com/api/v1/salesorders/' + id + '/status/confirmed?organization_id=' + self.org
        headers = {
                    'Authorization': 'Zoho-oauthtoken ' + self.zoho_info.access_token,
                    'Content-Type': 'application/json'
                    }
        response = requests.post(url, headers=headers)
        result = response.json()
        return result


    def createInvoice(self, payload_invoice):
        url = 'https://inventory.zoho.com/api/v1/invoices?organization_id=' + self.org
        headers = {
                    'Authorization': 'Zoho-oauthtoken ' + self.zoho_info.access_token,
                    'Content-Type': 'application/json'
                    }
        payload = payload_invoice
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        result = response.json()
        return result

    def confirmInvoice(self, id):
        url = 'https://inventory.zoho.com/api/v1/invoices/' + id + '/status/sent?organization_id=' + self.org
        headers = {
                    'Authorization': 'Zoho-oauthtoken ' + self.zoho_info.access_token,
                    'Content-Type': 'application/json'
                    }
        response = requests.post(url, headers=headers)
        result = response.json()
        return result
    
    def createPayment(self, payload_payment):
        url = 'https://inventory.zoho.com/api/v1/customerpayments?organization_id=' + self.org
        headers = {
                    'Authorization': 'Zoho-oauthtoken ' + self.zoho_info.access_token,
                    'Content-Type': 'application/json'
                    }
        payload = payload_payment
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        result = response.json()
        return result

    def createPackage(self, payload_package, salesorder_id):
        url = 'https://inventory.zoho.com/api/v1/packages?organization_id=' + self.org
        headers = {
                    'Authorization': 'Zoho-oauthtoken ' + self.zoho_info.access_token,
                    'Content-Type': 'application/json'
                    }
        payload = payload_package
        param = {
                 'salesorder_id': int(salesorder_id)
                }
        response = requests.post(url, headers=headers, data=json.dumps(payload), params=param)
        result = response.json()
        return result
    
    def createShipment(self, payload_shipment, package_id, salesorder_id):
        url = 'https://inventory.zoho.com/api/v1/shipmentorders?organization_id=' + self.org
        headers = {
                    'Authorization': 'Zoho-oauthtoken ' + self.zoho_info.access_token,
                    'Content-Type': 'application/json'
                    }
        payload = payload_shipment
        param = {'package_ids': int(package_id),
                 'salesorder_id': int(salesorder_id)
                }
        response = requests.post(url, headers=headers, data=json.dumps(payload), params=param)
        result = response.json()
        return result

    def updateContact(self, payload_contact, contact_id):
        url = 'https://inventory.zoho.com/api/v1/contacts/' + contact_id +'?organization_id=' + self.org
        headers = {
                    'Authorization': 'Zoho-oauthtoken ' + self.zoho_info.access_token,
                    'Content-Type': 'application/json'
                    }
        payload = payload_contact
        response = requests.put(url, headers=headers, data=json.dumps(payload))
        result = response.json()
        return result