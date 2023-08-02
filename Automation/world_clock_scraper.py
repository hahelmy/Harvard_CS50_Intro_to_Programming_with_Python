# This is a simple implementation of web scraping using requests and BeautifulSoup, to extract the
# current time of the 143 most popular cities in the world

import requests
from bs4 import BeautifulSoup

url = 'https://www.timeanddate.com/worldclock/'

r = requests.get(url)

soup = BeautifulSoup(r.content,'html.parser')


World_clock = []
i=0
j=1

tags = soup.find_all('td')


for tag in tags:

    city = tags[i].find('a').string
    time = tags[j]
    World_clock.append(f"{city}, {time.string}")
    i+=2
    j+=2

World_clock.sort()

for item in range(0,len(World_clock)):
    print(World_clock[item])

