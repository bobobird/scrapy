#-*- coding:utf-8 -*-

import os
import ValueConstant

def CheckFileAndGetPath(sFileName):
	sDir = ValueConstant.ValueData["Dir"]
	if not os.path.exists(sDir):
		os.makedirs(sDir)
	sPath = os.path.join(sDir, sFileName)
	return sPath.replace("\\", "/")

def ReadFile(sFileName):
	sPath = CheckFileAndGetPath(sFileName)
	if not os.path.isfile(sPath):
		print u"文件不存在", sPath
		return None
	oFile = None
	try:
		oFile = open(sPath, "rb")
		sFile = oFile.read()
	except Exception as e:
		print u"读取失败"
		raise
	finally:
		if oFile:
			oFile.close()
	return sFile

def WriteFile(sFileName, sFileContent):
	sPath = CheckFileAndGetPath(sFileName)
	oFile = None
	try:
		oFile = open(sPath, "wb")
		oFile.write(sFileContent)
	except Exception as e:
		print u"写入失败"
		raise
	finally:
		if oFile:
			oFile.close()
	return True

def WriteImg(sFileName, sFileContent):
	sPath = CheckFileAndGetPath(sFileName)
	oFile = None
	try:
		oFile = open(sPath, "wb")
		oFile.write(sFileContent.content)
	except Exception as e:
		print u"写入失败"
		raise
	finally:
		if oFile:
			oFile.close()
	return True