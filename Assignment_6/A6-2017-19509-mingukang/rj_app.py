from crawler import Crawler
from events import Events
from mood_detect import Mood
from article import Article
from fortune import Fortune

crawler = Crawler()
address = "관악구"

# 데이터 수집
weather_data = crawler.weather_fetch()

#print(weather_data)
#print(fine_dust_data)

# 날씨 이벤트 처리
weather_events = Events(weather_data, Events.WEATHER)
weather_events.process_events()

# Mood decision
mood = Mood()
template = mood.decision(weather_events.temp)
#print(template)

# fortune check
fortune = Fortune()
var = input("Please enter your birth [Ex)19990929] : ")
fortuneString = fortune.today_fortune(var)

# 기사 생성
article = Article(template, address, weather_events, fortuneString)
print(article.generate())
