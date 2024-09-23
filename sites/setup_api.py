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
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        }

        self.access_token = requests.request("POST", "https://api.laurentiumarian.ro/get_token", headers=post_header, data=payload).json()['access']

    
    def add_jobs(self):

        post_header = {
        # 'Authorization': f'Bearer {self.access_token}',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3OTgwNDgyLCJpYXQiOjE3MjcxMTY0ODIsImp0aSI6IjBiYzZhNWZkNTI2ZjQxNjhiOTU3ZjA4YWJiMTFiMWZiIiwidXNlcl9pZCI6OX0.5x9wJuJi3hne8XbO-DayS06szwMKyICD_K3aLAoPi9w',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        }

        print(f"Data List to send: {json.dumps(self.data_list)}")
        print(f"This is the post headers: {post_header}")
        requests.request("POST", "https://api.peviitor.ro/v5/add/", headers=post_header, data=json.dumps(self.data_list))
        time.sleep(5)

