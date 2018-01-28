import csv
import sys
import os

class Player:
    def __init__(self):
        self.__Registry = dict()
    
    def setRegistry(self, registry, value):
        self.__Registry[registry] = value
    
    def getRegistry(self, registry):
        return self.__Registry[registry]
    
    def getName(self, index):
        for i in range(0,len(self.__Registry)):
        return 0
     
def readFile():

    plist = []
    firstLine = True
    Fields = Player()
        
    script_dir = os.path.dirname(__file__)
    rel_path = str(sys.argv[1])
    abs_file_path = script_dir + rel_path
    
    if (os.path.exists(abs_file_path)):
        with open(abs_file_path, newline= "") as file:
            reader = csv.reader(file, delimiter= ',', quotechar= '|')
            for row in reader:
                if(firstLine):
                    for field in row:
                        Fields.setRegistry(field,0)
                #We can read the file now
                temp = Player()
                for i in range(0, len(row)):
                    temp.setRegistry(Fields,row[i])
            return
            
    else:
        print("file not found", rel_path)
        
    return 0

 
    
def main():
    players = readFile()
    
   

main()
