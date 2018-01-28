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
        
    def getRegistryViaIndex(self, index):
        count = 0
        for i in self.__Registry:
            if(count == index):
                return self.getRegistry(i)
            count += 1
        return 0
def readFile():

    plist = []
    firstLine = True
        
    script_dir = os.path.dirname(__file__)
    rel_path = str(sys.argv[1])
    abs_file_path = script_dir + rel_path
    
    if (os.path.exists(abs_file_path)):
        with open(abs_file_path, newline= "") as file:
            reader = csv.reader(file, delimiter= ',', quotechar= '|')
            for row in reader:
                if(firstLine):
                    Fields = row;
                    firstLine = False
                #We can read the file now
                temp = Player()
                for i in range(0, len(row)):
                    temp.setRegistry(Fields[i],row[i])
                plist.append(temp)
            
    else:
        print("file not found", rel_path)
        
    return plist

 
    
def main():
    players = readFile()
    print(players[2].getRegistryViaIndex(1))
    
   

main()
