import requests
from bs4 import BeautifulSoup
import csv 
import pandas as pd 

date = input("enter a date in this format MM/DD/YYYY : ")
page = requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}")

def main(page) : 
    print("started scraping")
    soup  = BeautifulSoup(page.content, "lxml")
    # print(soup)
    championships = soup.find_all("div", {"class": "matchesList"})

    def get_title(championship) : 
        title = championship.find("div", {"class" : "title"}).h2.text.strip()
        print(title)

    def get_game_details(championship) :
        title = championship.find("div", {"class" : "title"}).h2.text.strip()
        game_details = []
        games = championship.find("div", {"class" : "ul"})
        for game in games.find_all("div",{"class": "allData"}) :
            week = game.find("div", {"class" : "date"}).text.strip()
          
            status = game.find("div", {"class" : "matchStatus"}).span.text.strip()
            teamA = game.find("div", {"class" :"teamA"}).p.text.strip()
            teamB = game.find("div", {"class" :"teamB"}).p.text.strip()

            score = "-".join([element.text.strip() for element in game.find_all("span", {"class": "score"})])
            time = game.find("span", {"class": "time"}).text.strip()

            game_details.append(
                {
                  "date" : date , "championship" : title ,  "week" :  week, "status" : status ,"teamA" : teamA, "teamB" : teamB , "score" : score , "time"  : time 
                }
            )
       
        print(game_details)
        return game_details
    
 

    all_games = []
    for elem in championships : 
        get_title(elem)
        all_games += get_game_details(elem)

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(all_games)

    filename = 'project1/matches.xlsx'

    df.to_excel(filename, index=False)


        

main(page)