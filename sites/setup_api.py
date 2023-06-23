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
        self._send_clean_request()
        time.sleep(0.2)
        self._send_post_request()

    def _send_clean_request(self):
        """
        Send the clean request to the Peviitor API.
        """
        
        clean_url = 'https://api.peviitor.ro/v4/clean/'
        clean_header = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'apikey': self.api_key
        }
        requests.post(clean_url, headers=clean_header, data={'company': self.company_name})

    def _send_post_request(self):
        """
        Send the post request to update the data
        """
        post_header = {
            'Content-Type': 'application/json',
            'apikey': self.api_key
        }
        # print(json.dumps(self.data_list))
        requests.post('https://api.peviitor.ro/v4/update/', headers=post_header, data=json.dumps(self.data_list))

