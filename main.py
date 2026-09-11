import requests

USERNAME = "sudeshjha"
TOKEN = "abcdefghijklmnopqrstuvwxyz"

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
    "id": "graph1",
    "name": "Running Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}

headers = {"X-USER-TOKEN": TOKEN}


response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
print(response.text)
