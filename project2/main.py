import requests 
from bs4 import BeautifulSoup
import pandas as pd 
import pyperclip

base_url = "https://fr.wikipedia.org"
page = requests.get(f"{base_url}/wiki/Gouvernement_Akhannouch")
src = page.content

soup = BeautifulSoup(src , "lxml")

tables = soup.find_all("table", {"class" : "wikitable"})


items = tables[2].tbody.find_all("tr")
data = []
count = 0
for i in  range(1, len(items)) : 
    
    minestry = items[i].find_all("td")[1].text.strip()
   
    minester = items[i].find_all("td")[3].text.strip()
    
    party = items[i].find_all("td")[4].text.strip()
    details = ""
    websites = []

    if items[i].find_all("td")[1].a is not None:

        details = base_url + items[i].find_all("td")[1].a["href"]

        page2 = requests.get(details)
        src2 = page2.content 
        soup2 = BeautifulSoup(src2,"lxml")

        infobox = soup2.find("table", {"class":"infobox"})

        if infobox is not None : 
            element = infobox.find_all("a", {"class": ["external free", "external text"]})
            if len(element)>0 : 
                for x in element: 
                    print(x)
                    if ".ma" in x["href"].strip():
                        websites.append(x["href"])
                        count+=1
     

        # print(infobox)
    else:
        print("no website")


    data.append(
        {
            "minestry" : minestry,
            "minester" : minester , 
            "party" : party, 
            "details" : details, 
            "websites" : websites
        }
    )
 
print(len(data) , " and ", count)

# print(data)

df = pd.DataFrame(data)
filename = 'project2/data.xlsx'
df.to_excel(filename, index=False)