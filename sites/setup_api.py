import os
import requests
import json
import time


class UpdatePeviitorAPI:
    """
    Class for updating data on pe viitor API
    """

    def __init__(self, company_name, data_list):
        """
        Initialize the UpdatePeviitorAPI instance.
        """
        self.company_name = company_name
        self.data_list = data_list
        self.email = os.environ.get('API_KEY')

    def __call__(self):
        """
        Perform the data update process.
        """
        self.get_token()
        time.sleep(0.2)
        self.add_jobs()
    
    def get_token(self):

        payload = json.dumps({
        "email": self.email
        })
        
        post_header = {
        'Content-Type': 'application/json'
        }

        self.access_token = requests.request("POST", "https://api.peviitor.ro/v5/get_token/", headers=post_header, data=payload).json()['access']

    
    def add_jobs(self):

        post_header = {
        'Authorization': f'Bearer {self.access_token}',
        'Content-Type': 'application/json'
        }

        requests.request("POST", "https://api.peviitor.ro/v5/add/", headers=post_header, data=json.dumps(self.data_list))

