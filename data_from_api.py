"""
Poniższy kod pochodzi ze strony https://open-meteo.com/en/docs#daily=rain_sum.
Aby zadziałał wymagane zainstalowanie bibliotek:

pip install openmeteo-requests
pip install requests-cache retry-requests numpy pandas

Wszystkie wymagane biblioteki zapisane w pliku requirements.txt

Kod dostosowany do zadania w celu wyryfikacji wyników.
"""

import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
from constants import LATITUDE, LONGITUDE

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://historical-forecast-api.open-meteo.com/v1/forecast"
params = {
	"latitude": LATITUDE,
	"longitude": LONGITUDE,
	"start_date": "2024-10-01",
	"end_date": "2024-10-30",
	"daily": "rain_sum"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process daily data. The order of variables needs to be the same as requested.
daily = response.Daily()
daily_rain_sum = daily.Variables(0).ValuesAsNumpy()

daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left"
)}
daily_data["rain_sum"] = daily_rain_sum

daily_dataframe = pd.DataFrame(data = daily_data)
print(daily_dataframe)