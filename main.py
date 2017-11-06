#-*- coding:utf-8 -*-
#scrapy for http://www.qiushibaike.com
from sys import argv
import os
import ValueConstant
import DownloadSystem
from DataParse import CDataParse


class CMain:
	def __init__(self):
		pass


if __name__ == "__main__":
	import ValueConstant
	import FileSystem
	print u"传入参数", argv
	sUrl = ValueConstant.ValueData["Urls"]

	#---------------网站信息展示-----------
	DownloadSystem.PrintWebsiteInfo(sUrl)
	#DownloadSystem.PrintWebsiteFrameInfo(sUrl)
	#DownloadSystem.PrintWebsiteOwner(sUrl)
	#--------------------------------------
	
	#由于网站设置了拦截设置，需要加header否则会报错BadStatusLine
	sHtml = DownloadSystem.Download(sUrl)
	#print u"下载内容：", sHtml 
	oDataParse = CDataParse(sHtml)
	FileSystem.WriteFile("test.html", sHtml)
	print u"看看分析出来的链接：", oDataParse.GetHtmlList()
	print u"看看分析出来图片的链接：", oDataParse.GetPicList()

	index = 1
	for sTmpUrl in oDataParse.GetPicList():
		if sTmpUrl.endswith(".jpg"):
			sPic = DownloadSystem.Download(sUrl + sTmpUrl)
			FileSystem.WriteFile(str(index) + "test.jpg", sPic)
			index = index + 1
	os.system("pause")
else:
	print u"当前文件不是主要文件", __name__
