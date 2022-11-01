# Get data from people.xlsx file using Sheety API.

import requests


class DataFile:
    SHEETY_ENDPOINT = "https://api.sheety.co/ddfb0aadc6f7778438ec04f264db5801/peoples/one"

    def __init__(self):
        self.data = {}

    def get_data(self):
        res = requests.get(url=self.SHEETY_ENDPOINT)
        data_json = res.json()
        self.data = data_json["one"]
        return self.data  # returns dictionary with first name, last name, email, interest
