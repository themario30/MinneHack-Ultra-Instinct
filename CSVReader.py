#!/bin/env python3
import csv
import os

class Player:
    def __init__(self):
        self.__Registry = dict()
    
    def setRegistry(self, registry, value):
        self.__Registry[registry] = value
    
    def getRegistry(self, registry):
        return self.__Registry[registry]
        
        
def readFile():
    script_dir = os.path.dirname(__file__)
    rel_path = "csv\Hackathon dataset.csv"
    abs_file_path = os.path.join(script_dir, rel_path)
    
    with open(abs_file_path, newline= "") as file:
        reader = csv.reader(file, delimiter= ',', quotechar= '|')
        for row in reader:
            print(row)
            return
        
    return 0

 
    
def main():
    footballPlayers = readFile
   

main()
