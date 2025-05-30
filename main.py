from fastapi import FastAPI, Request
import requests
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# CORS ayarı (Django'dan fetch yapabilmek için)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

   # weather_translation = {
    #    "parçalı az bulutlu": "Partly Cloudy",
     #   "sağanak": "Shower Rain",
      #  "açık": "Clear",
       # "az bulutlu": "Few Clouds",
        #"kapalı": "Overcast",
    #    "sis": "Fog",
     #   "hafif yağmur": "Light Rain",
      #  "yoğun yağmur": "Heavy Rain",
       # "kar": "Snow",
       # "gök gürültülü sağanak yağış": "Thunderstorm"
        # gerektiği kadar ekleyebilirsin
  #  }

API_KEY = "1031abb06011708df56975abf0b04e6f"

@app.get("/weather")
def get_weather(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=en"
    response = requests.get(url)
    data = response.json()

   # description = data["weather"][0]["description"]
   # translated = weather_translation.get(description.lower(), description)
   # data["weather"][0]["description"] = translated

    return JSONResponse(content=data)