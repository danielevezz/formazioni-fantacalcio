from bs4 import BeautifulSoup as bs
import requests
import re
import csv
from Player import Player

class Parser:
    html = None
    url = "https://www.fantagazzetta.com/probabili-formazioni-serie-a"
    filenameTeam = ""
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

    def __init__(self, filenameTeam):
        page = requests.get(self.url, headers={"User-Agent": "Requests"})
        self.html = bs(page.content, "html.parser")
        self.soup = str(self.html)
        self.filenameTeam = filenameTeam
        print(f"Request: {page.status_code}")

    
    def parse(self):
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
        with open(self.filenameTeam, "r") as file:
            team = csv.reader(file, delimiter=",")

            giornata = re.search(r"SERIE A - [0-9]+. giornata", self.soup)
            print(f"{giornata.group()}\n")

            # Print the matches
            print("Le partite sono:")
            for link in self.html.find_all("a"):
                href = link.get("href")

                matches = re.findall(r'[a-z]+-[a-z]+', href)
                for match in matches:
                    if match is not None:
                        tmp = match.split("-")
                        home = tmp[0].capitalize()
                        away = tmp[1].capitalize()
                        if home == "Spal":
                            home = home.upper()
                        if away == "Spal":
                            away = away.upper()
                        if home[:3] in complete and away[:3] in complete:
                            print(f"{home} - {away}")

            print("")
            # Search the player percentages
            players = []

            for player in team:
                if team is None:
                    continue
                nome = player[1].strip().replace(" ", "-")
                squadra = complete[player[2]].strip()
                posizione = player[0]
                costo = player[3]
                p = Player(nome, squadra, posizione, costo)

                for link in self.html.find_all("a"):
                    href = link.get("href")

                    if f"{squadra}/{nome}" in href:
                        sibling = link.parent.nextSibling
                        panchina = False
                        if sibling is None:
                            sibling = link.parent.previousSibling
                            panchina = True

                        sibling = str(sibling)

                        perc = re.search(r'[0-9]+%', sibling).group()[:-1]

                        nome = nome.replace("-", " ").capitalize()

                        if panchina:
                            print(f"{nome} è in panchina con indice di subentro: {perc}%")
                        else:
                            print(f"{nome}: {perc}%")
                            p.isPlaying = True

                        p.percentage = int(perc)

                if f"{nome.capitalize()}: " in self.soup:
                    print(f"{nome} non è disponibile")
                
                players.append(p)
            return players
