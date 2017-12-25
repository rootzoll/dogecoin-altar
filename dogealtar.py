#!/usr/bin/env python
import urllib2, urllib
import time
import sys

##########################################
# DOGE ALTAR Control Script
##########################################
# my first python in a very loooong time
# feel free to improve :D
##########################################

# init balance
balance = 0.0

##################
# BURNING DOGE
##################

def processBurnedDoge( burnAmount ):
   # TODO --> switch GIO Pin on / sleep / off and play holy sound with speech of wisdom   
   print "TODO: switch on burn fire and make sound for " + str(tipToTheDOGE) + "DOGE"
   return


##################
# MAIN LOOP
##################

while True:
    try:
        print "Get fresh balance of burn address ..."
        data = urllib.urlopen('https://dogechain.info/chain/Dogecoin/q/addressbalance/DDogepartyxxxxxxxxxxxxxxxxxxw1dfzr')
        print 
        freshBanalceStr = data.read()
        freshBalance = float(freshBanalceStr)
        if freshBalance>balance:
            tipToTheDOGE = freshBalance - balance
            balance = freshBalance
            print "SUCH BURN - MUCH WOW: " + str(tipToTheDOGE)
            processBurnedDoge( tipToTheDOGE )
        time.sleep(20)
    except:
        e = sys.exc_info()[0]
        print "SUCH ERROR: %s" % e
        # TODO play error sound 
        print "take a nap doge altar - your drunk (30 secs)"
        time.sleep(60)
        pass