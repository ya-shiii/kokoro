from django.conf import settings
import requests
import json
from datetime import datetime

class Omnisend:

    token = str(settings.OMNISEND_TOKEN)
    headers = {
            'content-type': "application/json",
            'X-API-KEY': token
            }
    def Contact(self, email, first_name, last_name):
        url = 'https://api.omnisend.com/v3/contacts'
        param = 'email=' + email
        enParam = param.encode()
        response = requests.get(url, headers=self.headers, params=enParam)
        print(response)
        data = response.json()
        if len(data['contacts']) == 0:
            date = datetime.now()
            payload = {
                "createdAt": date.isoformat()+'Z',
                'firstName': first_name,
                'lastName': last_name,
                'country': 'Chile',
                'countryCode': 'CL',
                "identifiers": [
                            {
                            "type": "email",
                            "id": email,
                            "channels": {
                                "email": {
                                "status": "subscribed",
                                "statusDate": date.isoformat()+'Z'
                                }
                            }
                            }
                        ],
            }
            response = requests.post(url, headers=self.headers, data=json.dumps(payload))
            data = response.json()
            print(data)
            return data['contactID']
        return data['contacts'][0]['contactID']

    def AddOrder(self, products, contactID, ordernumber, subtotal, total, discount, tax, shipping, paymentStatus):
        url = 'https://api.omnisend.com/v3/orders'
        date = datetime.now()
        payload = {
                    "orderID": str(ordernumber),
                    "orderNumber": ordernumber,
                    "contactID": str(contactID),
                    "currency": "CLP",
                    "subTotalSum": int(subtotal)*100,
                    "orderSum": int(total)*100,
                    "discountSum": int(discount)*100,
                    "taxSum": int(tax)*100,
                    "shippingSum": int(shipping)*100,
                    "createdAt": date.isoformat()+'Z',
                    "paymentMethod": "Credit card",
                    "paymentStatus": paymentStatus,
                    "products": products
                }
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        data = response.json()
        print(data)
        return data['orderID']
    
    def getProduct(self, productID):
        url = 'https://api.omnisend.com/v3/products/' + productID
        response = requests.get(url, headers=self.headers)
        data = response.json()
        return data


    def FullfilmentOrder(self, orderID, CarrierName, CarrierURL, Tracking):
        url = 'https://api.omnisend.com/v3/orders/' + str(orderID)
        payload = {
            'fulfillmentStatus': 'fulfilled',
            'trackingCode': Tracking,
            'courierUrl': CarrierURL,
            'courierTitle': CarrierName

        }
        response = requests.patch(url, headers=self.headers, data=json.dumps(payload))
        data = response.json()
        return data

    def CustomeEvent(self, eventID, name, systemname, email, fields):
        url = 'https://api.omnisend.com/v3/events/' + str(eventID)
        payload = {
                    "name": name,
                    "systemName": systemname,
                    "email": email,
                    "fields": fields
                    }
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        data = response
        return data