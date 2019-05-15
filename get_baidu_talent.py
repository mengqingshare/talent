#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import urllib2
import json
import sys 
reload(sys)
sys.setdefaultencoding('utf8')

base_url = "https://talent.baidu.com/baidu/web/httpservice/getPostList?workPlace=&recruitType=2&pageSize=10&curPage="
curPage = 1
respFirstTime = urllib2.urlopen(base_url+str(curPage))
baseInfo = respFirstTime.read()
objBaseInfo = json.loads(baseInfo)
totalPage = objBaseInfo['totalPage']

print "********get baidu talent start !!!*************\n"
index = 1
while index < totalPage :
    print "get page " +str(index) + " start"

    
    respItem = urllib2.urlopen(base_url+str(index))

    dataItem = respItem.read()
    strFileName = "data/baidu/baidu_talent_" + str(index)  + "json_.txt"
    strFileNameDone = "data/baidu/baidu_talent" + ".txt"

    fileJson = open(strFileName,"w")
    fileJson.write(dataItem)
    fileJson.close()

    objItem = json.loads(dataItem)
    postList = objItem['postList']
    for post in postList :
        strLine = "new_line@" +str(post['postId'])\
                + "@" +str(post['name'])\
                + "@" +str(post['publishDate'])\
                + "@" +str(post['postType'])\
                + "@" +str(post['workPlace'])\
                + "@" +str(post['serviceCondition'])\
                + "@" +str(post['workContent']).replace("\n"," ")
        fileItem = open(strFileNameDone,"a+")
        fileItem.write(strLine+"\n")
        fileItem.close()
    index += 1
    print "get page " + str(index)+ " done"
print "********get baidu talent finished !!!*************\n"
