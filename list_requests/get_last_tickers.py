from .base_request import BaseRequest
from datetime import datetime, timedelta, timezone

import json
import sys


class GetLastTickers(BaseRequest):

    def get_10_last_tickers(self):
        parameters = {
            'start': '1',
            'limit': '10',
            'sort': 'volume_24h'
        }
        endpoint = "cryptocurrency/listings/latest"

        response = self.get_endpoint(endpoint, parameters)

        return response

    def check_size(self, response):


        size_content = sys.getsizeof(
            response.content) + sys.getsizeof(dict(response.headers))

        max_size = 10 * 1024


        assert size_content < max_size, "The size of the received data exceeds 10kb"

    def check_date(self, response):
        body = json.loads(response.text)


        server_time = datetime.strptime(body['status']['timestamp'], "%Y-%m-%dT%H:%M:%S.%f%z")
        for i in range(len(body["data"])):
            last_update = datetime.strptime(body['data'][i]["last_updated"], "%Y-%m-%dT%H:%M:%S.%f%z")
            dif_days = (server_time - last_update).days

            assert dif_days == 0, "data not relevant"



    def check_time(self, response):
        assert response.status_code == 200, f"status code is NOT 200, response status = {response.status_code} "
        assert response.elapsed.total_seconds() < 0.5, f"response time exceeds 500 ms, response time = {response.elapsed.total_seconds()}"

    def first_task(self):
        response = self.get_10_last_tickers()
        self.check_time(response)
        self.check_size(response)
        self.check_date(response)




