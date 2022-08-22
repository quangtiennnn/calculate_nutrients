import requests
import datetime as dt
# import json
import os
APP_ID = "35154950"
API_KEY = "d88f5e88bc8c22542352c4cb36cfdcc3"

nutrients_endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"

headers = {
    "Content-Type": 'application/json',
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id" : "0",
}

parameters = {
    "query":"noodle and rice",
    # "timezone": "US/Eastern"
}

response = requests.post(nutrients_endpoint, json=parameters, headers=headers)
data = response.json()

USER_NAME = "b9656573b2bab5d97fed2ce9c016d3c9"
PROJECT_NAME= "myWorkout"
SHEET_NAME = "eating"
API_URL = f"https://api.sheety.co/{USER_NAME}/{PROJECT_NAME}/{SHEET_NAME}"
# https://api.sheety.co/b9656573b2bab5d97fed2ce9c016d3c9/myWorkout/eating
current = dt.datetime.now()
current_day = current.strftime("%d/%m/%Y")
current_time = current.strftime("%H:%M:%S")
USER_NAME = "quangtiennnn"
PASSWORD = 'QUANGTIENVANHUNGNGUOIBAN'
auth = (
    # os.environ["USERNAME"],
    USER_NAME,PASSWORD
    # os.environ["PASSWORD"],
)
dict_push = {}
for i in range(len(data['foods'])):
    sheet_input = {
        SHEET_NAME: {
            'date': current_day,
            'time': current_time,
            'food': data['foods'][i]['food_name'].title(),
            'quantity': data['foods'][i]['serving_qty'],
            'calories':data['foods'][i]['nf_calories'],
        }
    }
    sheet_response = requests.post(url=API_URL, json=sheet_input,auth = auth)
    print(sheet_response)