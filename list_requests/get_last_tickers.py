from list_requests.base_request import BaseRequest

import json

class GetLastTickers(BaseRequest):

    def get_10_last_tickers(self):
        parameters = {
            'start': '1',
            'limit': '10',
            'sort': 'volume_24h'
        }
        endpoint = "cryptocurrency/listings/latest"

        response = self.get_endpoint(endpoint, parameters)
        assert response.status_code==200 , f"status code is NOT 200, response status = {response.status_code} "
        assert response.elapsed.total_seconds() < 0.5 , f"response time exceeds 500 ms, response time = {response.elapsed.total_seconds()}"
        return response


    def get_data(self):
        response = self.get_10_last_tickers()

        body = json.loads(response.text)
        headers=response.headers.items()


        print(len(response.content))  # размер body


        print(response.elapsed.total_seconds())#время ответа
        print(headers)
        print(body)






a = GetLastTickers()
a.get_data()