from django.conf import settings
import requests
import json

class tradegecko:
    key = str(settings.TRADEGECKO_KEY)

    def variant(self, variant_id):
        url = 'https://api.tradegecko.com/variants'
        payload = {'ids': variant_id}
        headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + self.key
        }
        response = requests.get(url, headers=headers, params=payload)
        result = response.json()
        return result['variants']

    def product(self, brand):
        url = 'https://api.tradegecko.com/products'
        payload = {'status': 'active', 'brand': brand}
        headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + self.key
        }
        response = requests.get(url, headers=headers, params=payload)
        result = response.json()
        return result['products']

    def updateVariantQuantity(self,id,quantity):
        url = 'https://api.tradegecko.com/variants/'+str(id)
        payload = {'variant':{'committed_stock': str(quantity)}}
        headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + self.key
        }
        response = requests.put(url, headers=headers, params=payload)
        result = response.json()
        return result

    def getProduct(self, id):
        url = 'https://api.tradegecko.com/products/'+str(id)
        headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + self.key
        }
        response = requests.get(url, headers=headers)
        result = response.json()
        print(result)
        return result

    def getAllProduct(self, page):
        url = 'https://api.tradegecko.com/variants?page=' + str(page)
        headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + self.key
        }
        response = requests.get(url, headers=headers)
        result = response.json()
        return result

    def getVariant(self,id):
        url = 'https://api.tradegecko.com/variants/'+str(id)
        headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + self.key
        }
        response = requests.get(url, headers=headers)
        result = response.json()
        print(result)
        return result   
    
    def getOrder(self,id):
        url = 'https://api.tradegecko.com/orders/'+str(id)
        headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + self.key
        }
        response = requests.get(url, headers=headers)
        result = response.json()
        return result

    def getOrderAll(self, page):
        url = 'https://api.tradegecko.com/orders/?page='+ str(page)
        headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + self.key
        }
        response = requests.get(url, headers=headers)
        result = response.json()
        return result
        
    def getOrderLineItem(self,id):
        url = 'https://api.tradegecko.com/order_line_items/'+str(id)
        headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + self.key
        }
        response = requests.get(url, headers=headers)
        result = response.json()
        print(result)
        return result

    def getAddress(self,id):
        url = 'https://api.tradegecko.com/addresses?ids[]='+str(id)
        headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + self.key
        }
        response = requests.get(url, headers=headers)
        result = response.json()
        return result
    
    def getCustomerbyEmail(self,email):
        url = 'https://api.tradegecko.com/companies?email='+str(email)
        headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + self.key
        }
        response = requests.get(url, headers=headers)
        result = response.json()
        print(result)
        return result

    def getContact(self, ids):
        url = 'https://api.tradegecko.com/contacts?ids[]='+str(ids)
        headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + self.key
        }
        response = requests.get(url, headers=headers)
        result = response.json()
        print(result)
        return result

    def getCustomer(self,company_id):
        url = 'https://api.tradegecko.com/companies?ids[]='+str(company_id)
        headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + self.key
        }
        response = requests.get(url, headers=headers)
        result = response.json()
        print(result)
        return result

    def createOrder(self,id_company,fecha,address_billing,address_shipment,status,products):
        url = 'https://api.tradegecko.com/orders'
        payload = {"order":{"company_id":id_company,
                            "issued_at":fecha,
                            "tax_treatment": "inclusive",
                            "status": status,
                            "billing_address_id":address_billing,
                            "shipping_address_id":address_shipment,
                            "order_line_items":products
                            }
                  }
        print('payload  -------- ')
        print(payload)
        headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + self.key
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        result = response.json()
        print(result)
        return result

    def createCompany(self,nombre, company_type, email, mobile):
        url = 'https://api.tradegecko.com/companies'
        payload = {"company":{"name":nombre,"company_type":"consumer","email":email, "mobile": mobile}}
        headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + self.key
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        result = response.json()
        print(result)
        return result
    
    def createAddress(self,nombre, company_id, calle, city, country, phone, comuna, number):
        url = 'https://api.tradegecko.com/addresses'
        payload = {"address":{"company_id":company_id,
                                "label":nombre,
                                "address1":calle,
                                "city":city,
                                "phone_number": phone,
                                "address2": number,
                                "suburb": comuna,
                                "country": country}}
        headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + self.key
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        result = response.json()
        print(result)
        return result


    def getInvoice(self,invoice_id):
        url = 'https://api.tradegecko.com/invoices?ids[]='+str(invoice_id)
        headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + self.key
        }
        response = requests.get(url, headers=headers)
        result = response.json()
        return result
