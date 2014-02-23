# Author: Schaden Philipp
#
# Description:
# class that updates the repo.csv with use of the libmng class

import requests
from libmng import Libmng


class updater():

    def __init__(self):
        self.localmng = Libmng('local')
        
    
    # getmaster downloads the online csv temporary
    def getmaster(self,url):
#        self.req = requests.get(url) for testing local repos are used
        self.mastermng = Libmng('master')
        print self.mastermng
        
    # getdiff looks for missing entries in the local csv
    def getdiff(self):
        for local in self.localmng.getall(0):
            for master in self.mastermng.getall(0):
                if local == master:
                    print 'ja'
                    #break
                else:
                    print 'nein',local,master
                    self.localmng.addlib(master[0],master[1],'added through update')
                    #break
            
        
    # updatelocal adds missing entries from the online csv to 
    # the local csv
    def updatelocal(self):
        pass
    
    
        
    



