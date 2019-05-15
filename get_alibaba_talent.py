#!/usr/bin/python
# -*- coding: UTF-8 -*- 
# 引入一些包
import urllib2 
import json
import sys 

# 设置编码
reload(sys)
sys.setdefaultencoding('utf8')

# 基础信息，为了获取总页数
base_url = "https://job.alibaba.com/zhaopin/socialPositionList/doList.json?pageIndex="
curPage = 1
# 读取数据
respFirstTime = urllib2.urlopen(base_url+str(curPage))
baseInfo = respFirstTime.read()
# 把 json 变成可以处理的数据
objBaseInfo = json.loads(baseInfo)
# 总页数
totalPage = objBaseInfo['returnValue']['totalPage']

# 正式开始
print "********get alibaba talent start !!!*************\n"
# 循环标记，页数
index = 1
# 循环，到最大页数为止
while index < totalPage :
    print "get page " +str(index) + " start"

    # 请求每一页的数据
    respItem = urllib2.urlopen(base_url+str(index))
    dataItem = respItem.read()

    # 数据存储文件 每一页的 json 数据
    strFileName = "data/alibaba/alibaba_talent_" + str(index)  + "json_.txt"
    # 最后的汇总数据
    strFileNameDone = "data/alibaba/alibaba_talent" + ".txt"

    # 文件操作，打开文件
    fileJson = open(strFileName,"w")
    # 写数据
    fileJson.write(dataItem)
    # 关闭文件
    fileJson.close()

    # 读取json
    objItem = json.loads(dataItem)
    # 获取真正的职位数据
    postList = objItem['returnValue']['datas']

    # 每一个职位变成一行数据，字段按照接口取
    for post in postList :
        # newline 是每一行的开头 ，字段用 @ 分开
        strLine = "new_line@" +str(post['id'])\
                + "@" +str(post['name'])\
                + "@" +str(post['departmentName'])\
                + "@" +str(post['workLocation'])\
                + "@" +str(post['workExperience'])\
                + "@" +str(post['firstCategory'])\
                + "@" +str(post['secondCategory'])\
                + "@" +str(post['description'])\
                + "@" +str(post['requirement'])

        # 文件操作，打开文件
        fileItem = open(strFileNameDone,"a+")
        # 写入数据
        fileItem.write(strLine+"\n")
        # 关闭文件
        fileItem.close()

    # 页数加1
    index += 1
    
    print "get page " + str(index)+ " done"

print "********get alibaba talent finished !!!*************\n"
