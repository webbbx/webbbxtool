#coding=utf-8  
''''' 
IP反查小工具 
 
'''  
#athour by webbbx


import requests,json,urllib,sys,os  
from bs4 import BeautifulSoup  
import re
#获取页面内容  
def getPage(ip):  
    url="http://dns.aizhan.com/%s/" % (ip)
    response=urllib.urlopen(url)
    data=response.read()
    souphtml=BeautifulSoup(data)
    domainList = souphtml.find_all(text=re.compile("(\w+.\w.(?:com\.cn|cn|com|net))"))
    # print domainList
    # domainList2 = ",".join(domainList).encode('utf-8')
    for i in range(0,10):
        print domainList[i].encode('utf-8')

if __name__ == "__main__":  
#     ip='60.190.243.200'
#     outfile='F:/python1/saomiaoqi/1.html'
    ip = str(sys.argv[1])  
    print "The target IP is :%s" % ip  
    print "Starting, please wait..."  
    getPage(ip)