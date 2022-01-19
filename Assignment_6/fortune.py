import requests
import datetime
from bs4 import BeautifulSoup

URL = 'http://www.erumy.com/free/todayFortuneReport.aspx'

class Fortune:

    def mingu(self, soup):
        tmpres = str(soup.select('label > ul')[0])
        todayfortune = tmpres[4:-5]
        tmpres = soup.select('div > font > label')[0]
        today = tmpres.get_text('label')
        return todayfortune

    def today_fortune(self, birth):
        url = URL + '?m=dummy&uday=' + birth + '&lunar=1'
        r = requests.get(url, auth=('user', 'pass'))
        html = r.text
        bs = BeautifulSoup(html, 'html.parser')
        return self.mingu(bs)

