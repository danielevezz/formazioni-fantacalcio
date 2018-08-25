from bs4 import BeautifulSoup as bs
import requests
import re
import csv

url = "https://www.fantagazzetta.com/probabili-formazioni-serie-a"

page = requests.get(url, headers={"User-Agent": "Requests"}).content
soup = bs(page, "html.parser")

complete = {
    "Ata": "Atalanta",
    "Bol": "Bologna",
    "Cag": "Cagliari",
    "Chi": "Chievo",
    "Emp": "Empoli",
    "Fio": "Fiorentina",
    "Fro": "Frosinone",
    "Gen": "Genoa",
    "Int": "Inter",
    "Juv": "Juventus",
    "Laz": "Lazio",
    "Mil": "Milan",
    "Nap": "Napoli",
    "Par": "Parma",
    "Rom": "Roma",
    "Sam": "Sampdoria",
    "Sas": "Sassuolo",
    "SPA": "SPAL",
    "Tor": "Torino",
    "Udi": "Udinese",
}
with open("team.csv", "r") as file:
    team = csv.reader(file, delimiter=",")

    for player in team:
        nome = player[0].strip().replace(" ","-")
        squadra = complete[player[1]].strip()

        for link in soup.find_all("a"):
            href = link.get("href")

            if f"{squadra}/{nome}" in href:
                sibling = link.parent.nextSibling
                panchina = False
                if sibling is None:
                    sibling = link.parent.previousSibling
                    panchina = True
            
                
                sibling = str(sibling)

                perc = re.search(r'[0-9]+%',sibling).group()

                nome = nome.replace("-"," ").capitalize()

                if panchina:
                    print(f"{nome} è in panchina con indice di subentro: {perc}")
                else:
                    print(f"{nome}: {perc}")


