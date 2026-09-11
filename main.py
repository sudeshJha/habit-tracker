import requests
from datetime import datetime

USERNAME = "sudeshjha"
TOKEN = "abcdefghijklmnopqrstuvwxyz"
GRAPH_ID = "graph1"
HEADERS = {"X-USER-TOKEN": TOKEN}


# ------------------------------- CREATE A USER
PIXELA_USER_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=PIXELA_USER_ENDPOINT, json=user_params)

# ------------------------------- CREATE A GRAPH
GRAPH_ENDPOINT = f"{PIXELA_USER_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": {GRAPH_ID},
    "name": "Running Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=HEADERS)

# ------------------------------- CREATE A PIXEL
PIXEL_CREATION_ENDPOINT = f"{PIXELA_USER_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime(year=2026, month=9, day=9)
pixel_data = {"date": today.strftime("%Y%m%d"), "quantity": "20"}

# response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_data, headers=HEADERS)


# ------------------------------- EDIT A PIXEL
edit_date = datetime(year=2026, month=9, day=9).strftime("%Y%m%d")
new_pixel_data = {"quantity": "40"}
PIXEL_UPDATE_ENDPOINT = f"{PIXEL_CREATION_ENDPOINT}/{edit_date}"

response = requests.put(url=PIXEL_UPDATE_ENDPOINT, json=new_pixel_data, headers=HEADERS)
print(response.text)
