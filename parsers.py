from bs4 import BeautifulSoup
import requests


class WeatherComParser:
    def get_local_weather(self):
        page = requests.get("https://weather.com/redir?page=today&id=autodetect&locale=")

        soup = BeautifulSoup(page.content, "html.parser")

        temp = soup.find('div', 'today_nowcard-temp').contents[0].text
        feels = soup.find('span', 'deg-feels').text
        description = soup.find('div', 'today_nowcard-phrase').contents[0]

        return {
            'temp': temp,
            'description': description,
            'feels': feels,
        }


class AirMattersParser:
    def get_warsaw_aqi(self):
        # TODO: Make it accept location!
        page = requests.get("https://air-quality.com/place/poland/warsaw/65d8cd8b?lang=en&standard=aqi_us")
        soup = BeautifulSoup(page.content, "html.parser")

        aqi = soup.find('div', 'indexValue').text

        return {
            'aqi': aqi
        }


#w = WeatherComParser()
#print(w.get_local_weather())

#a = AirMattersParser()
#print(a.get_warsaw_aqi())
