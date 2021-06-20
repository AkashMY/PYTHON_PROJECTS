import requests

GENDER = "Male"
WEIGHT_KG = 76
HEIGHT_CM = 177
AGE = 25

Application_ID = "26681ed2"

Application_Keys = "574106bbf69315c12875ef110eb7fb2a"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercise you did?")

headers = {
    "x-app-id": Application_ID,
    "x-app-key": Application_Keys,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)


# Authorization: Basic QWthc2hNWTpBazk5MDA=

sheet_post_url = "https://api.sheety.co/AkashMY/WorkoutTracking/workouts"

requests.post(url=sheet_post_url,)
