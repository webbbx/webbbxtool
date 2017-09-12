#coding=utf-8  
''''' 
IP反查小工具 
 
'''  
#author by webbbx


import requests,json,urllib,sys,os  
from bs4 import BeautifulSoup  
import re
#获取页面内容  
def get_Domain(ip):  
    url="http://dns.aizhan.com/%s/" % (ip)
    try:
        response=urllib.urlopen(url)
        data=response.read()
        souphtml=BeautifulSoup(data)
        # domainList = souphtml.find_all(text=re.compile("(\w+.\w.(?:com\.cn|cn|com|net))"))
        domainList = souphtml.find_all(text=re.compile("^((?!http).)*com|.cn|.net|.org|.gov|.edu|.wang"))
        # print domainList
        domainList_Make = domainList[:-1]
    except Exception,e:
        print e
        print "%s can not be reversed" % ip

    # domainList2 = ",".join(domainList).encode('utf-8')
    try:
        for i in domainList_Make:    
            print i.encode('utf-8')
    except Exception,e:
        print "%s can not be reversed" % ip
        

if __name__ == "__main__":  
    # ip='162.159.209.34'
    ip = str(sys.argv[1])  
    print "The target IP is :%s" % ip  
    print "Starting, please wait..."  
    get_Domain(ip)
