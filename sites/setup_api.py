import os
import requests
import json
import time


# Inspired from the Andrei Cojocaru update_peviitor_api Decorator
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
        self.api_key = os.environ.get('API_KEY')

    def __call__(self):
        """
        Perform the data update process.
        """
        self.get_token()
        time.sleep(0.2)
        self.add_jobs()
    
    def get_token(self):

        payload = json.dumps({
        "email": "irimusrares7@gmail.com"
        })
        
        post_header = {
        'Content-Type': 'application/json'
        }

        self.access_token = requests.request("POST", "https://api.laurentiumarian.ro/get_token", headers=post_header, data=payload).json()['access']

    
    def add_jobs(self):

        post_header = {
        'Authorization': f'Bearer {self.access_token}',
        'Content-Type': 'application/json'
        }

        requests.request("POST", "https://api.laurentiumarian.ro/jobs/add/", headers=post_header, data=json.dumps(self.data_list))
        
        # don't delete this lines if you want to see the graph on scraper's page
        file = self.company_name.lower() + '.py'
        data = {'data': len(self.data_list)}
        dataset_url = f'https://dev.laurentiumarian.ro/dataset/JobsScrapers/{file}/'
        requests.post(dataset_url, json=data)
        ########################################################
    

