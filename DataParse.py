#-*- coding:utf-8 -*-



def ParseBySiteMap(sData):
	import re
	lLink = re.findall('<loc>(.*?)</loc>', sData)
	print "从robot.txt文件中获取的url:", lLink

class CDataParse:
	def __init__(self, sHtml):
		self.m_HtmlList = []
		self.m_PicList = []
		self.ParseHtml(sHtml)
		self.ParsePic(sHtml)
	
	def ParseHtml(self, sHtml):
		import re
		oWebRegex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
		self.m_HtmlList = oWebRegex.findall(sHtml)
	
	def ParsePic(self, sHtml):
		import re
		oWebRegex = re.compile('<img[^>]+src=["\'](.*?)["\']', re.IGNORECASE)
		self.m_PicList = oWebRegex.findall(sHtml)
	
	def GetHtmlList(self):
		return self.m_HtmlList

	def GetPicList(self):
		return self.m_PicList
