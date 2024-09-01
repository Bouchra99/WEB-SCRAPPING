# import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

movieName = input("Enter the movie name : ").strip()


imdb = f"https://www.imdb.com/title/tt0137523/?ref_={ '%'.join(movieName.split()) }"
rotenTomato = f"https://www.rottentomatoes.com/m/{ '_'.join(movieName.split())}"
s = HTMLSession()

def get_soup(url) :

    page = s.get(url)
    print(page.status_code)
    src = page.text
    soup = BeautifulSoup(src, "html.parser")

    return soup

imdbSoup = get_soup(imdb)
rotenTomatoSoup = get_soup(rotenTomato)
# print(soup)
imdbScore = imdbSoup.find("div",{"class" : "sc-eb51e184-0 ghvwpw"}).find("span", {"class": "sc-eb51e184-1 ljxVSS"}).text.strip()

criticsScore = rotenTomatoSoup.find("rt-button", {"slot" : "criticsScore"}).find('rt-text').text.strip()
popcornMeter =  rotenTomatoSoup.find("rt-button", {"slot" : "audienceScore"}).find('rt-text').text.strip()


print(imdbScore)
print(criticsScore)
print(popcornMeter)
