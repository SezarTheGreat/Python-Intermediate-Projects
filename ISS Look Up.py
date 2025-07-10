import requests
from datetime import datetime
import smtplib
import time

my_latitude = 28.704060
my_longitude = 77.102493
my_email = "jyotishmanjbbarman@gmail.com"
my_pass = ""
#Information extraction for the iss and the sunrise and sunset timings
##Iss

def iss_pos_comp():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if my_latitude-5 <= iss_latitude <= my_latitude+5 and my_longitude-5 <= iss_longitude <= my_longitude+5:
        return True
##Sunrise and sunset
def is_night():
    parameters = {"lat":my_latitude,
                  "lng":my_longitude,
                  "formatted":0}

    response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if iss_pos_comp() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email,my_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject:Look UP!\n\nThe ISS is above you in the sky!"
        )
