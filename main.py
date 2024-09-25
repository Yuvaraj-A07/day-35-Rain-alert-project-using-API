import requests
# from twilio.rest import Client
import smtplib
import manager as mg

api_key = mg.api_key
MY_LAT = mg.MY_LAT
MY_LONG = mg.MY_LONG

my_mail = mg.my_mail
password = mg.password

# acc_id =
# acc_token =

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()
print(response.status_code)
data = response.json()
will_rain = False
# data["list"][ids]["weather"][0]["id"]
for hour_data in data["list"]:
    condition = hour_data["weather"][0]["id"]
    if condition < 700:
        will_rain = True

if will_rain:
    # client = Client(acc_id, acc_token)
    # message = client.messages.create(
    #     body="Hey its rainy today , bring up an umbrella",
    #     from_="",
    #     to=""
    # )
    # print(message.status)
    with smtplib.SMTP("smtp.gmail.com") as send_quote:
        send_quote.starttls()
        send_quote.login(user=my_mail, password=password)
        send_quote.sendmail(from_addr=my_mail,
                            to_addrs=my_mail,
                            msg=f"Subject:Rainy!!! \n\nIt's going to rain today, Bring up an Umbrella")
