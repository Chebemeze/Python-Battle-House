from datetime import datetime, timedelta
import requests

now = datetime.now()
weeks_ago = now - timedelta(days=7)
start_date = weeks_ago.strftime("%Y-%m-%d")
end_date = now.strftime("%Y-%m-%d")
url = f"https://api.open-meteo.com/v1/forecast?latitude=48.856&longitude=80.645&start_date={start_date}&end_date={end_date}&current=temperature_2m"
response = requests.get(url)
print(response.json())
# print(weeks_ago)
# print(timedelta(days=5))
# a = "eb"
