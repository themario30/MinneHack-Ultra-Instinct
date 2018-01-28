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
        
        
def readFile():
    script_dir = os.path.dirname(__file__)
    rel_path = "/" + str(sys.argv[1])
    abs_file_path = script_dir + rel_path
    
    if (os.path.exists(abs_file_path)):
        with open(abs_file_path, newline= "") as file:
            reader = csv.reader(file, delimiter= ',', quotechar= '|')
            for row in reader:
                #We can read the file now
                if(row != None):
                    print(row[0])
            
    else:
        print("file not found", rel_path)
        
    return 0

 
    
def main():
    readFile()
   

main()
