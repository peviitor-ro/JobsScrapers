import requests
import json



def update_logo(id: str, logo_url: str):
    """
    Update Logo
    """
    headers = {
        "Content-Type": "application/json"
    }
    url = "https://api.peviitor.ro/v1/logo/add/"
    data = json.dumps([{"id": id, "logo": logo_url}])

    try:
        requests.post(url, headers=headers, data=data, timeout=30)
    except requests.exceptions.RequestException:
        pass

    # return response