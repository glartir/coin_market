from .base_request import BaseRequest
from datetime import datetime, timedelta, timezone
import threading
import json
import sys
import time
import pytest


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

        #бросаем исключение на 10*1024
        assert size_content < 10240, "The size of the received data exceeds 10kb"

    def check_date(self, response):
        body = json.loads(response.text)


        server_time = datetime.strptime(body['status']['timestamp'], "%Y-%m-%dT%H:%M:%S.%f%z")
        for i in range(len(body["data"])):
            last_update = datetime.strptime(body['data'][i]["last_updated"], "%Y-%m-%dT%H:%M:%S.%f%z")
            dif_days = (server_time - last_update).days

            assert dif_days == 0, "Data not relevant"



    def check_time(self, response):
        print(response.elapsed.total_seconds())
        assert response.status_code == 200, f"Status code is NOT 200, response status = {response.status_code} "
        assert response.elapsed.total_seconds() < 0.5, f"Response time exceeds 500 ms, response time = {response.elapsed.total_seconds()}"

    def first_task(self):
        response = self.get_10_last_tickers()
        self.check_time(response)
        self.check_size(response)
        self.check_date(response)

    def get_multuply_request(self,barrier,i,responses):

        barrier.wait()                              # Накапливаем все запросы чтоб их запустить  в один момент
        if responses["time_start"]==0:              # Первый вошедший поток запустит таймер
            responses["time_start"]=time.time()

        responses[i] = self.get_10_last_tickers()


        # self.check_time(responses[i])
        # self.check_size(responses[i])
        # self.check_date(responses[i])








    def multistart(self,number):
        barrier = threading.Barrier(number,timeout=10)
        running_threads=[]
        responses = {"time_start" : 0, "time_finish" : 0}
        for i in range (number):
            thread=threading.Thread(target=self.get_multuply_request,args=(barrier,i,responses,))

            thread.start()
            running_threads.append(thread)
        #time.sleep(10)
        for r in running_threads:
            r.join()
        responses["time_finish"]=time.time()


        for i in range(number):
            self.check_time(responses[i])
            self.check_size(responses[i])
            self.check_date(responses[i])
        total_time= responses["time_finish"]-responses["time_start"]
        rps=number/total_time
        assert  rps>5 , "The number of response per second is less than 5 "
        print(f"total time = {total_time}")



# a=GetLastTickers()
# a.multistart()
#a.first_task()