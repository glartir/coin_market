import requests


class BaseRequest():
    def __init__(self):
        API_KEY = "fd4e7cd3-7e6a-4a5d-8dbc-1251ad07a38e"
        self.host="https://pro-api.coinmarketcap.com/v1/"
        self.headers = {
                        'Accepts': 'application/json',
                        'X-CMC_PRO_API_KEY': f'{API_KEY}',
                        }

    def get_endpoint(self,endpoint,params=None):
        url=self.host + endpoint

        response = requests.get(url,headers=self.headers,params=params)

        return response