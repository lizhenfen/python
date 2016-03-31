In [154]: strs.decode('unicode_escape')
Out[154]: u'\u5546\u5bb6\u53d1\u5355\u7c7b\u578b\u672a\u7ed1\u5b9a'

In [155]: print strs.decode('unicode_escape')
商家发单类型未绑定

In [156]: str =strs.decode('unicode_escape')

In [157]: str
Out[157]: u'\u5546\u5bb6\u53d1\u5355\u7c7b\u578b\u672a\u7ed1\u5b9a'

In [158]: str.encode('utf8')
Out[158]: '\xe5\x95\x86\xe5\xae\xb6\xe5\x8f\x91\xe5\x8d\x95\xe7\xb1\xbb\xe5\x9e\x8b\xe6\x9c\xaa\xe7\xbb\x91\xe5\xae\x9a'

In [159]: print str.encode('utf8')
商家发单类型未绑定
