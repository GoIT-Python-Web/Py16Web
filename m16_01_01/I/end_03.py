import requests
from typing import Any, Dict, List


# https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11
class ApiClient:
    def __init__(self, fetch: requests):
        self.fetch = fetch

    def get_json(self, url):
        response = self.fetch.get(url)
        return response.json()


class Viewer:
    def display(self, data: list[dict[str, Any]]):
        raise NotImplementedError


class CurrencyViewer(Viewer):

    def _adapter(self, data):
        result = [
            {
                f"{el.get('ccy')}": {
                    "buy": float(el.get("buy")),
                    "sale": float(el.get("sale")),
                }
            }
            for el in data
        ]
        return result

    def display(self, data: list[dict]):
        result = self._adapter(data)

        pattern = "|{:^10}|{:^10}|{:^10}|"
        print(pattern.format("currency", "sale", "buy"))
        for el in result:
            currency, *_ = el.keys()
            buy = el.get(currency).get("buy")
            sale = el.get(currency).get("sale")
            print(pattern.format(currency, sale, buy))


if __name__ == "__main__":
    client = ApiClient(requests)
    viewer = CurrencyViewer()
    data = client.get_json(
        "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11"
    )
    viewer.display(data)
