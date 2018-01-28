#!/bin/env python3
import csv

class Player:
    def __init__(self):
        self.__Registry = dict()
    
    def setRegistry(self, registry, value):
        self.__Registry[registry] = value
    
    def getRegistry(self, registry):
        return self.__Registry[registry]
        
        
def readFile():
    with open("csv/Hackathon dataset.csv", newline= "\n") as file:
        reader = csv.reader(file, delimiter= ',', quotechar= '|')
        for row in reader:
            print(row)
            return
        
    return 0

 
    
def main():
    footballPlayers = readFile
   

main()
