import random
from parsers import WeatherComParser, AirMattersParser

try:
    # Works on Pythonista on iOS, might want to adapt to other TTS engine
    import speech
    can_speak = True
except:
    can_speak = False


name = "Marcin"

greetings = ["Cześć", "Witaj", "Dzień dobry"]
suggestion_beginnings = ['Przyda Ci się', 'Rzeczy potrzebne dziś to']
rainy_words = ['deszcze', 'opady', 'burze']

w = WeatherComParser()
weather = w.get_local_weather()

a = AirMattersParser()
# Looking for open api to get local results, for now hardcoded
air = a.get_warsaw_aqi()

suggested_items = []

if int(air['aqi']) > 100:
    suggested_items.append('maska')

if int(weather['feels'].replace('°', '')) < 18:
    suggested_items.append('kurtka')

if int(weather['feels'].replace('°', '')) < 10:
    suggested_items.append('czapka')

if any(word in weather['description'] for word in rainy_words):
    suggested_items.append('parasol')

if len(suggested_items) > 0:
    suggestion = "{} {} i {}.".format(random.choice(suggestion_beginnings), ", ".join(suggested_items[:-1]), suggested_items[-1])
else:
    suggestion = ""

announcement = "{greeting} {name}, na dworze jest {temp}, {description}, odczuwalna temperatura to {feels}, wskaźnik jakości powietrza A.Q.I. wynosi {aqi}, {suggestion}"\
    .format(greeting=random.choice(greetings),
                   name=name,
                   temp=weather['temp'],
                   description=weather['description'],
                   feels=weather['feels'],
                   aqi=air['aqi'],
                   suggestion=suggestion)


if can_speak:
    speech.say(announcement, "pl_PL")
else:
    print(announcement)




