import requests
API_key = "PG2UG64IUAL5X9XI"   #https://www.alphavantage.co/documentation/#daily
key = "7e76575f00ca43ff945e372f233be63c"   #"https://newsapi.org/v2/everything"
import os
from twilio.rest import Client
SID = "AC1eae4c1499721ed1fcd2e1b196a6baf8"
AUTH = "71a89242cc2eb3fcc269a673ae379320"

STOCK_NAME = "SBI"
COMPANY_NAME = "SBI"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

parameters = {

    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_key,
}

stock_data = requests.get(url=STOCK_ENDPOINT, params=parameters)
stock_data.raise_for_status()

data = stock_data.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_stock_price = data_list[0]['4. close']

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_stock_price = data_list[1]['4. close']

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
stock_diff = abs(float(day_before_yesterday_stock_price) - float(yesterday_stock_price))

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_diff = round((stock_diff/float(day_before_yesterday_stock_price)) * 100, 2)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_diff > 0:

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    parameters = {
        "apiKey": key,
        "qInTitle": COMPANY_NAME,
    }
    responce = requests.get(url=NEWS_ENDPOINT, params=parameters)
    responce.raise_for_status()
    lisi_of_articles = responce.json()['articles']

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    list_of_3_articles = lisi_of_articles[:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio.

    formatted =[f'Headline : {item["title"]}, \nBrief: {item["description"]}\n' for item in list_of_3_articles ]

    account_sid = SID
    auth_token = AUTH
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=formatted[0],
                         from_="+19893422211",
                         to='+919008811801'
                    )

    print(message.status)


#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

# SEND SMS THROUGH Twillio
