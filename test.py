'''
print(100 + 200 + 300)
print(1,2,3,4)
print('100+200', 100+200)
name = input('请输入你的名字')
print('您好,', name)
print('1024 * 768 = ', 1024 * 768)
if name == '罗丹':
	print('是我老婆')
else:
	print('不是我老婆')
'''
#字符串
#print(r'''a\n
#	b
#c''')
#print(r'abc\n\\\t')
'''
#布尔值
print(True, False, True and True, True and False, True or False, not True) 

#变量
a = 'ABC'
b = a
a = 'XYZ'
print(a, b)
#编码  内存unicode 磁盘bytes encode() decode() len()
x = b'ABC'
print(ord('A'), ord('中'), chr(66), chr(25991), '\u4e2d\u6587', x, 'ABC'.encode('ascii'), b'ABC'.decode('utf-8'), len('ABC'))
'''
#格式化  %s 字符串 %d整数 %f浮点数 %x十六进制整数  %%表示%
print('Hello, %s' % 'world', '%2d-%02d' % (3,1), '%.2f' % 3.1415926, 'growth rate %d %%' % 7)
print('Hello, {0}, 成绩提升了{1:.1f}%'.format('小明', 17.125))
s1, s2 = 71, 85
r = (s2 - s1) / s1
print('小明提升的百分点是%.1f%%' % r)






















