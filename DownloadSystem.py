#-*- coding:utf-8 -*-

def PrintWebsiteInfo(sUrl):
	print u"当前网站robot.txt"

def PrintWebsiteFrameInfo(sUrl):
	import builtwith
	dFrameData = builtwith.parse(sUrl)
	print u"当前网站架构信息", dFrameData

def PrintWebsiteOwner(sUrl):
	import whois
	dOwnData = whois.whois(sUrl)
	print u"当前网站所有者：", dOwnData
#---------描述性信息----------------


def Download(sUrl, sUserAgent = "wswp", iNum = 2):
	import urllib2
	print "Download: ", sUrl
	dHeader = {"User-agent" : sUserAgent}
	oRequest = urllib2.Request(
			url = sUrl,
			headers = dHeader
		)
	try:
		sHtml = urllib2.urlopen(oRequest).read()
	except urllib2.URLError as e:
		print "Download error:", e.reason
		sHtml = None
		if iNum > 0:
			if hasattr(e, "code") and 500 <= e.code < 600:
				return Download(sUrl, sUserAgent, iNum - 1)
	return sHtml