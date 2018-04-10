 python的编码判断_unicode_gbk/gb2312_utf8（附函数）
python中， 我们平常使用最多的三种编码为 gbk/gb2312,  utf8 ,  unicode。 而python中并没有一个函数来进行 编码的判断。今天，主要对这三种编码进行讨论，并给出区分这三种编码的函数。

我们知道，

      unicode编码是1位       gbk，gb2312是2位       utf-8是3位

所以，若只有一个汉字，我们可以通过 长度来判断：

len(u'啊') == 1 #True
len(u'啊'.encode("gbk"))  == 2  #True
len(u'啊'.encdoe("utf-8")) == 3  #True
但是实际中，往往是一句话，包含好多汉字。于是，我们做如下实验：

1，u'啊'.encode("gbk")[0].decode("gbk") 将会提示错误  UnicodeDecodeError: 'gbk' codec can't decode byte 0xb0 in position 0: incomplete multibyte sequence
2，u'啊'.encode('utf8')[0].decode("utf8") 将会提示错误 UnicodeDecodeError: 'utf8' codec can't decode byte 0xe5 in position 0: unexpected end of data
3，u'啊'.encode('gbk')[0].decode('utf8')  将会提示错误 UnicodeDecodeError: 'utf8' codec can't decode byte 0xb0 in position 0: invalid start byte
4，u'啊'.encode('utf8')[0].decode('gbk')  将会提示错误 UnicodeDecodeError: 'gbk' codec can't decode byte 0xe5 in position 0: incomplete multibyte sequence
5，u'啊'.decode('utf8')       将会提示错误           UnicodeEncodeError: 'ascii' codec can't encode character u'\u554a' in position 0: ordinal not in range(128)
6，u'啊'.decode('gbk')       将会提示错误           UnicodeEncodeError: 'ascii' codec can't encode character u'\u554a' in position 0: ordinal not in range(128)
由以上可以看出，提示错误若出现 ascii，则该句编码位 ascii 无疑，从2，3可以看出 .decode("utf8")可以区分出不同的编码： unexpected end of data 表示 该句为 utf8编码， 而 invalid start byte 则表示 该句为gbk编码或者gb2312编码。

综上，可以编写如下函数来进行编码判断：（python27）
 
 
 
 
 
 
def whichEncode(text):
	text0 = text[0]
	try:
		text0.decode('utf8')
	except Exception, e:
		if "unexpected end of data" in str(e):
			return "utf8"
		elif "invalid start byte" in str(e):
			return "gbk_gb2312"
		elif "ascii" in str(e):
			return "Unicode"
	return "utf8"

print whichEncode()
