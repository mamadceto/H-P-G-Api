from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
import time
import random
import uuid
from concurrent.futures import ThreadPoolExecutor

app = FastAPI()

def get_app_data():
    return {
        "train": ["82647f43-3f87-402d-88dd-09a90025313f", "c4480ac7-e178-4973-8061-9ed5b2e17954"],
        "chain": ["d1690a07-3780-4068-810f-9b5bbf2931b2", "b4170868-cef0-424f-8eb9-be0622e8e8e3"],
        "bike":  ["d28721be-fd2d-4b45-869e-9f253b554e50", "43e35910-c168-4634-ad4f-52fd764a843f"],
        "clone": ["74ee0b5b-775e-4bee-974f-63e7f4d5bacb", "fe693b26-b342-4159-8808-15e3ff7f8767"]
    }

def get_headers(token=None):
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,fa;q=0.8",
        "content-type": "application/json",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site"
    }
    if token:
        headers["authorization"] = f"Bearer {token}"
    return headers

def login_client(app_token):
    url = "https://api.gamepromo.io/promo/login-client"
    data = {
        "appToken": app_token,
        "clientId": f"{time.time()*1000000}-{random.randint(7080730066215695760, 9080730066215695760)}",
        "clientOrigin": "deviceid"
    }
    while True:
        try:
            response = requests.post(url, headers=get_headers(), json=data)
            response_data = response.json()
            if 'error_code' in response_data and response_data.get('error_code') == 'TooManyIpRequest':
                time.sleep(60 * random.uniform(1, 1.5))
            elif 'clientToken' in response_data:
                return response_data.get('clientToken')
        except Exception as e:
            time.sleep(5)

def register_event(client_token, promp_id):
    url = "https://api.gamepromo.io/promo/register-event"
    headers = get_headers(client_token)
    while True:
        data = {
            "promoId": promp_id,
            "eventId": str(uuid.uuid4()),
            "eventOrigin": "undefined"
        }
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.json().get('hasCode', '') == True:
                break
            time.sleep(random.randint(20, 25))
        except Exception as e:
            time.sleep(5)

def create_code(client_token, promp_id):
    url = 'https://api.gamepromo.io/promo/create-code'
    data = {"promoId": promp_id}
    while True:
        try:
            response = requests.post(url, headers=get_headers(client_token), json=data)
            promo_code = response.json().get('promoCode', '')
            if promo_code:
                return promo_code
            time.sleep(5)
        except Exception as e:
            time.sleep(5)

def execute_promo(category):
    app_data = get_app_data()
    if category not in app_data:
        return []

    app_token, promp_id = app_data[category]

    client_token = login_client(app_token)
    time.sleep(random.randint(20, 25))

    register_event(client_token, promp_id)
    code = create_code(client_token, promp_id)
    return code

@app.get('/generate')
async def generate_all_codes():
    num_codes_per_category = 4
    categories = get_app_data().keys()
    result = {"Creator": "@mmdceto"}

    with ThreadPoolExecutor(max_workers=16) as executor:
        futures = {category: [executor.submit(execute_promo, category) for _ in range(num_codes_per_category)] for category in categories}

    for category, future_list in futures.items():
        result[category] = [future.result() for future in future_list]

    return JSONResponse(content=result)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
