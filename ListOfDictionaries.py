'''
Created on Feb 22, 2016

@author: AsusZen
'''

class ListOfDictionaries(object):
    list = [];
    def __init__(self):
        self

    def addHost(self, key, value):
        
        dictionary = {key: value};
        self.list.append(dictionary);
          
    def listHost(self, key):
        for item in self.list:
            value = self.getHostValue(item, key)
            if value is None:
                continue
            else: return value
            
    def getHostValue(self, item, key):
        v = item.get(key)
        return v
    
    def updateHost(self, key, value):
        
        for i in self.list:
            del i[key]; 
        
        self.addHost(key, value)
            
    def deleteHost(self, key):
        for i in self.list:
            del i[key]; 