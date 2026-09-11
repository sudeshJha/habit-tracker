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
