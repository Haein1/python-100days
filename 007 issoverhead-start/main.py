import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 00000 # Your latitude
MY_LONG = 00000  # Your longitude

def IsISSCloseToMe():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def if_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "Asia/Taipei"
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    print(sunrise)
    print(sunset)
    time_now = datetime.now().hour
    time_now_hour = 19
    if time_now >= sunset or time_now <= sunrise:
        return True
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if IsISSCloseToMe() and if_night():
        # print(0)
        my_email = "@gmail.com"
        my_password = ""
        # connection = smtplib.SMTP("smtp.gmail.com", 587)
        # print(IsISSCloseToMe())
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="@qq.com",
            msg="Subject:Attention!\n\nHi!\nISS is over your head.\nTake a look!\nBest,\nY"
        )
        connection.close()



