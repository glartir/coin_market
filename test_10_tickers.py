import pytest

from .list_requests.get_last_tickers import GetLastTickers


def test_10_tickers_first_task():

    last_10_tickers=GetLastTickers()
    last_10_tickers.first_task()

def test_10_tickers_first_task2():

    last_10_tickers=GetLastTickers()
    last_10_tickers.first_task()
