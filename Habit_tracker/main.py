import requests
import datetime as dt
pixels_endpoint = "https://pixe.la/v1/users"
token_key = "iqei7ce331wqcsKsxhcauhuwnansiuhwe"
username = "akash82176945"


user_params = {
    "token": token_key,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    }

# responce = requests.post(url=pixels_endpoint, json=user_params)
# print(responce.text)

Post_endpoint = f"{pixels_endpoint}/{username}/graphs"

post_params = {
    "id": "graph1",
    "name": "Cycling graph",
    "unit": "km",
    "type": "float",
    "color": "sora",
}

header = {
    "X-USER-TOKEN": token_key,
}

# responce = requests.post(url=Post_endpoint, json=post_params, headers=header)
# print(responce.text)

pixel_post_endpoint = f'https://pixe.la/v1/users/{username}/graphs/{post_params["id"]}'

today = dt.datetime.today()
# date = today.day
# month = today.month
# year = today.year
#
formatted_date = today.strftime("%Y%m%d")                # f"{year}{month}{date}"
print(formatted_date)

post_parms = {
    "date": formatted_date,
    "quantity": input("How many kilometers you cycled today? : "),
}


post = requests.post(url=pixel_post_endpoint, headers=header, json=post_parms)
print(post.text)
