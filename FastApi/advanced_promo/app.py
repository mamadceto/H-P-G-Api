from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
import requests
import time
import random
import uuid
from concurrent.futures import ThreadPoolExecutor
from fastapi.responses import JSONResponse

app = FastAPI()

MAX_CODES = 20

def get_app_data():
    return {
        "train": ["82647f43-3f87-402d-88dd-09a90025313f", "c4480ac7-e178-4973-8061-9ed5b2e17954"],
        "chain": ["d1690a07-3780-4068-810f-9b5bbf2931b2", "b4170868-cef0-424f-8eb9-be0622e8e8e3"],
        "bike": ["d28721be-fd2d-4b45-869e-9f253b554e50", "43e35910-c168-4634-ad4f-52fd764a843f"],
        "clone": ["74ee0b5b-775e-4bee-974f-63e7f4d5bacb", "fe693b26-b342-4159-8808-15e3ff7f8767"]
    }

def get_headers(token: Optional[str] = None):
    headers = {
        "accept": "*/*",
        "content-type": "application/json"
    }
    if token:
        headers["authorization"] = f"Bearer {token}"
    return headers

def login_client(app_token: str):
    url = "https://api.gamepromo.io/promo/login-client"
    data = {
        "appToken": app_token,
        "clientId": f"{uuid.uuid4()}-{int(time.time() * 1000)}",
        "clientOrigin": "deviceid"
    }
    while True:
        try:
            response = requests.post(url, headers=get_headers(), json=data)
            response_data = response.json()
            if response_data.get('error_code') == 'TooManyIpRequest':
                time.sleep(60 * random.uniform(1, 1.5))
            elif 'clientToken' in response_data:
                return response_data['clientToken']
        except requests.RequestException:
            time.sleep(5)

def register_event(client_token: str, promo_id: str):
    url = "https://api.gamepromo.io/promo/register-event"
    headers = get_headers(client_token)
    data = {
        "promoId": promo_id,
        "eventId": str(uuid.uuid4()),
        "eventOrigin": "undefined"
    }
    while True:
        try:
            response = requests.post(url, headers=headers, json=data)
            response_data = response.json()
            if response_data.get('hasCode', False):
                break
            time.sleep(random.randint(20, 25))
        except requests.RequestException:
            time.sleep(5)

def create_code(client_token: str, promo_id: str):
    url = "https://api.gamepromo.io/promo/create-code"
    headers = get_headers(client_token)
    data = {"promoId": promo_id}
    while True:
        try:
            response = requests.post(url, headers=headers, json=data)
            response_data = response.json()
            promo_code = response_data.get('promoCode')
            if promo_code:
                return promo_code
            time.sleep(5)
        except requests.RequestException:
            time.sleep(5)

def execute_promo(category: str):
    app_data = get_app_data()
    if category not in app_data:
        return []

    app_token, promo_id = app_data[category]

    client_token = login_client(app_token)
    time.sleep(random.randint(20, 25))

    register_event(client_token, promo_id)
    return create_code(client_token, promo_id)

class GenerateResponse(BaseModel):
    codes: dict
    Creator: str

@app.get("/generate", response_model=GenerateResponse)
async def generate_codes(
    category: Optional[str] = Query(None),
    num: int = Query(4, le=MAX_CODES)
):
    if num > MAX_CODES:
        raise HTTPException(status_code=400, detail=f"The maximum number of key creations is {MAX_CODES}")

    app_data = get_app_data()

    if not category or (category not in app_data and category != "all"):
        raise HTTPException(status_code=400, detail="The structure of the provided API is incorrect.")

    result = {}
    categories = [category] if category != "all" else app_data.keys()

    with ThreadPoolExecutor(max_workers=len(categories) * num) as executor:
        futures = {}
        for cat in categories:
            futures[cat] = [executor.submit(execute_promo, cat) for _ in range(num)]

        for cat in futures:
            result[cat] = [future.result() for future in futures[cat]]

    response = {
        "Creator": "@mmdceto",
        "codes": result
    }
    return JSONResponse(content=response)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5000)
