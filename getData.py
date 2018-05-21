# -*- coding: utf-8 -*-
"""
Created on Sat May 12 12:21:13 2018

@author: Jeffer
"""


# No Time To Do it Now
# Use CSV first

import urllib2



def getData(htmldir):
    # TODO : Make it configurable： like season，player_id
    url = r"http://www.stat-nba.com/query.php?page=0&QueryType=game&GameType=season&Player_id=1628&order=1&crtcol=pts&PageNum=100&Season0=2017&Season1=2018#label_show_result"
    res = urllib2.urlopen(url,timeout=300)
    html = res.read()
    res.close()
    f = open(htmldir,'w')
    f.write(html)
    return True




if __name__ == "__main__":
    if getData(r"D:\Study\PythonProject\Sk_Learn\NBA_HD\Data\1718NBA.html"):
        print "Done"