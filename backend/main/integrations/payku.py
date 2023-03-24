from django.conf import settings
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import urllib
import urllib.request, requests
import logging
import hmac
import hashlib
from urllib.parse import quote_plus
import json

logger = logging.getLogger(__name__) 

class payku:
    apiKey = str(settings.PAYKU_PUB)
    secret_key = str(settings.PAYKU_PIV)
    URL_base = str(settings.API_URL)

    def __init__(self):
        pass

    def Pagocontarjeta(self,email,monto,orden,subject,metodopago):
        url_api = '/api/transaction'
        params = ({
                    "email": email,
                    "order": orden,
                    "subject": subject,
                    "amount": monto,
                    "payment": metodopago,
                    "urlreturn": self.URL_base + "api/main/payment_red?order=" + str(orden),
                    "urlnotify": self.URL_base + "api/main/retornopayku"
                    })
        data = ''
        pag = str(settings.PAYKU_URL) + url_api
        for key, val in params.items():
            if data =='':
                data = quote_plus(url_api, safe='') + '&' + key + '=' + quote_plus(str(val), safe='')
            else:
                data = data  + '&' + key + '=' + quote_plus(str(val))
        byteparams = bytes(data, 'utf-8')
        # Creating signature for the API
        signature = hmac.new(bytes(self.secret_key, 'utf-8'), msg=byteparams, digestmod=hashlib.sha256).hexdigest()
        # add the signuture to url
        headers = {"Authorization": "Bearer " + self.apiKey,'Content-Type': 'application/json', 'Sign': signature}
        # params['s']=str(signature)
        url = requests.post(pag, data=json.dumps(params), headers=headers)
        # Getting API response
        response = url.json()
        print(response)
        return response
