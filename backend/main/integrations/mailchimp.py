from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
import mailchimp_transactional as MailchimpTransactional


class mailchimp:
    apiKey = str(settings.MAILCHIMP_KEY)
    server = str(settings.MAILCHIMP_SERVER)
    print(server)
    
    def __init__(self):
        pass

    def getStores(self):
        try:
            client = Client()
            client.set_config({
                "api_key": self.apiKey,
                "server": self.server
            })

            response = client.ecommerce.stores()
            return response
        except ApiClientError as error:
            print("Error: {}".format(error.text))
            return error.text
    
    def addStore(self,store_id,nombre,currency):
        try:
            client = Client()
            client.set_config({
                "api_key": self.apiKey,
                "server": self.server
            })

            response = client.ecommerce.add_store({"id": store_id, "list_id": "ecc7930a6b", "name": nombre, "currency_code":currency})
  
            return response
        except ApiClientError as error:
            print("Error: {}".format(error.text))
            return error.text
    
    def addProduct(self, store_id, payload):
        try:
            client = Client()
            client.set_config({
                "api_key": self.apiKey,
                "server": self.server
            })
            response = client.ecommerce.add_store(store_id, payload)
            return response
        except ApiClientError as error:
            print("Error: {}".format(error.text))
            return error.text

    def addCustomer(self,store_id,userid,email,name,lastname):
        try:
            client = Client()
            client.set_config({
                "api_key": self.apiKey,
                "server": self.server
            })

            response = client.ecommerce.add_store_customer(store_id, {"id": userid, "email_address": email, "opt_in_status": True,"name":name,"lastname":lastname})
            return response
        except ApiClientError as error:
            print("Error: {}".format(error.text))
            return error.text

    def addOrder(self,store_id,orderid,customerid,totalorden,productos,financial_status):
        try:
            client = Client()
            client.set_config({
                "api_key": self.apiKey,
                "server": self.server
            })
            
            response = client.ecommerce.add_store_order(store_id,{"id":str(orderid),
                                                                "customer":{"id":customerid},
                                                                "currency_code":"CLP",
                                                                "order_total":totalorden,
                                                                "lines":productos,
                                                                "financial_status":financial_status})
            
            return response
        except ApiClientError as error:
            print("Error: {}".format(error.text))
            return error.text

    def getOrder(self,store_id,order_id):
        try:
            client = Client()
            client.set_config({
                "api_key": self.apiKey,
                "server": self.server
            })
            response = client.ecommerce.get_order(store_id, order_id)
            return response
        except ApiClientError as error:
            print("Error: {}".format(error.text))
            return error.text

    def getProduct(self,store_id,product_id):
        try:
            client = Client()
            client.set_config({
                "api_key": self.apiKey,
                "server": self.server
            })
            response = client.ecommerce.get_store_product(store_id, product_id)
            return response
        except ApiClientError as error:
            print("Error: {}".format(error.text))
            return error.text

    def getAllProducts(self,store_id):
        try:
            client = Client()
            client.set_config({
                "api_key": self.apiKey,
                "server": self.server
            })
            response = client.ecommerce.get_all_store_products(store_id)
            return response
        except ApiClientError as error:
            print("Error: {}".format(error.text))
            return error.text

    def getCustomer(self,store_id,customer_id):
        try:
            client = Client()
            client.set_config({
                "api_key": self.apiKey,
                "server": self.server
            })
            response = client.ecommerce.get_store_customer(store_id, customer_id)
            return response            
        except ApiClientError as error:
            print("Error: {}".format(error.text))
            return error.text
  
    def updateOrder(self,store_id,orderid,financial_status):
        try:
            client = Client()
            client.set_config({
                "api_key": self.apiKey,
                "server": self.server
            })
            
            response = client.ecommerce.update_order(store_id,str(orderid),{"financial_status":financial_status})
            
            return response
        except ApiClientError as error:
            print("Error: {}".format(error.text))
            return error.text

    def sendSingleemail(self,  email_cliente, subject, texto):
        mailchimp = MailchimpTransactional.Client(self.apiKey)
        message = {
            "from_email": "contacto@kokorofoods.cl",
            "subject": subject,
            "text": texto,
            "to": [
            {
                "email": email_cliente,
                "type": "to"
            }
            ]
        }
        try:
            response = mailchimp.messages.send({"message":message})
            print('API called successfully: {}'.format(response))
            return response
        except ApiClientError as error:
            print('An exception occurred: {}'.format(error.text))
            return error.text