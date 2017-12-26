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
'''
print('Hello, %s' % 'world', '%2d-%02d' % (3,1), '%.2f' % 3.1415926, 'growth rate %d %%' % 7)
print('Hello, {0}, 成绩提升了{1:.1f}%'.format('小明', 17.125))
s1, s2 = 71, 85
r = (s2 - s1) / s1
print('小明提升的百分点是%.1f%%' % r)
'''
#列表 len函数 append函数 insert函数 pop方法 赋值
'''
list = ['a', 'b', 'c']
list.append('d')
list.insert(1, 1)
list.pop()
list.pop(1)
list[-1] = 'd'
print(list, len(list), list[-1])
'''
#元组  初始化后不能修改
'''
classMates = ('e', 'f', 'g')
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0], L[1][1], L[2][2])
'''
#条件判断 if else elif
'''
age = 18
if age > 10:
	print('你的年龄是：', age, '岁');
height = 1.75
weight = 80.5
bmi = 80.5 / (1.75 * 1.75)
bmiText = ''
if bmi < 18.5:
	bmiText = '过轻'
elif bmi >= 18.5 and bmi < 25:
	bmiText = '正常'
elif bmi >= 25 and bmi < 28:
	bmiText = '过重'
elif bmi >= 28 and bmi < 32:
	bmiText = '肥胖'
else:
	bmiText = '严重肥胖'
print(bmiText)
'''
#循环 for in循环 range函数 list函数 while循环 break continue
'''
names = [0, 1, 2]
for name in names:
	print(name)
print(range(10), list(range(10)))
L1 = ['Bart', 'Lisa', 'Adam']
for l1 in L1:
	print('Hello, ' + l1)
	'''
#字典 dict  in c操作符 get方法 pop方法 
#set结构 add方法 remove方法
'''
d = { 'a': 95, 'b': 90, 'c': 85 }
d['d'] = 70
print(d['a'], d, 'b' in d, d.get('e', 0), d.pop('a'), d)
s = set([1,1,2,2,3,4])
s.add(5)
tt = { (1, 2): 2 }
print(s, s.remove(1), tt)
'''
#函数 def关键字
print(abs(-1))
n1 = 255
n2 = 1000
print(hex(n1), hex(n2))
def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type for abs(): \'str\'')
	if x < 0:
		x = -x
	return x
print(my_abs(0), my_abs(10), my_abs(-10), my_abs('a'))
def noop():
	pass
	







