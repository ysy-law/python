import math
from collections import Iterable
# 数据类型
# 整数、浮点、字符串、布尔值、空值（None）
# 变量、常量
# ord函数 获取字符的整数表示
print(ord('A'))
# chr函数 编码转换成对应的字符
print(chr(65))
# 如果知道字符的整数编码，还可以用十六进制这么写str
print('\u4e2d\u6587')
# bytes类型的数据用带b前缀的单引号或双引号表示
print(b'ABC')
# encode函数 字符串转换成指定的bytes
print('ABC'.encode('ascii'), '中文'.encode('utf-8'))
# decode函数 字节转换成字符串 传入errors='ignore'忽略错误的字节
print(b'ABC'.decode('utf-8'), b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
# len函数 字符数 如果换成bytes，len()函数就计算字节数
print(len('中文'), len('中文'.encode('utf-8')))
# 字符串格式化  占位符 %d 整数  %f 浮点数 %s 字符串 %x 十六进制 
# 有几个%?占位符，后面就跟几个变量或者值，顺序要对应好
# 用%%来表示一个%
# format函数格式化
print('hi, %s, you have $%d.' % ('罗丹', 1), '%3d-%03d' % (3, 1), '%.2f' % 3.141592654, 'growth rate: %d %%' % 4)
print('Hello, {0}, 成绩提升了 {1: .1f}%'.format('小明', 17.125))
# 练习 
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位
s1, s2 = 72, 85
r = (s2 - s1) / s1 * 100
print('小明提升的百分点是%.1f%%' % r)
# 列表list
# len函数 获取list元素的个数
lists = [1,2,3]
print(len(lists))
# append函数 往list中追加元素到末尾
lists.append(4)
print(lists)
# insert函数 插入到指定位置
lists.insert(1, 5)
print(lists)
# pop函数 删除list末尾的元素 删除指定位置的元素，用pop(i)方法，其中i是索引位置：
lists.pop()
lists.pop(1) 
print(lists)
# 元组tuple tuple一旦初始化就不能修改
tuples = (4,5,6)
print(tuples)
# 条件判断
# if语句  elif else
# 练习 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
height = 1.75
weight = 80.5
bmi = weight / (height * height)
result = ''
if bmi < 18.5:
	result = '过轻'
elif bmi >= 18.5 and bmi < 25:
	result = '正常'
elif bmi >= 25 and bmi < 28:
	result = '过重'
elif bmi >= 28 and bmi < 32:
	result = '肥胖'
else:
	result = '严重肥胖'
print('小明的BMI指数为%.2f，属于%s' % (bmi, result))
# 循环
# for ... in 循环 依次把list或tuple中的每个元素迭代出来
for l in lists:
	print(l)
# range函数 生成一个整数序列
print(list(range(5)))
# while循环
num = 0
n = 99
while n > 0:
	n -= 2
	num += n
print(num)
# break 提前退出循环
# conti 跳过当前的这次循环，直接开始下一次循环
# 字典dict
dicts = {
	'a': 0,
	'b': 1,
	'c': 2
}
# in关键字 判断key是否存在
print('a' in dicts, 'd' in dicts)
# get方法 如果key不存在，可以返回None，或者自己指定的value
print(dicts.get('a'), dicts.get('d', '不存在此键'))
# set数据结构 也是一组key的集合，但不存储value key不能重复
sets = set([1,2,3])
print(sets)
# add方法 添加元素到set中，可以重复添加，但不会有效果
sets.add(4)
sets.add(4)
print(sets)
# remove方法 删除元素
sets.remove(4)
print(sets)
# 函数 def关键字定义 
# 定义函数时，需要确定函数名和参数个数；
# 如果有必要，可以先对参数的数据类型做检查；
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple。
# 数据类型转换函数 int方法、float方法、str方法、bool方法
# 练习 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
n1 = 255
n2 = 1000
print(str(hex(255)), str(hex(1000)))
# 练习 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0的两个解。
def quadratic(a, b, c):
	x1 = None
	x2 = None
	t = b * b - 4 * a * c
	if a == 0:
		return - c / b
	elif t >= 0:
		x1 = (-b + math.sqrt(t)) / (2 * a)
		x2 = (-b - math.sqrt(t)) / (2 * a)
		return x1, x2
	else:
		return '无解'
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
# 函数参数
# 位置参数
def power1(x, n):
	s = 1
	while n > 0:
		s = s * x
		n = n - 1
	return s
print(power1(5, 3))
# 默认参数
def power2(x, n = 2):
	s = 1
	while n > 0:
		s = s * x
		n = n - 1
	return s
print(power2(5), power2(2, 6))
# 可变参数
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum += n * n
	return sum
num = [2,3]
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
print(calc(1,2,3), *num)
# 关键字参数
def person(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)
person('liuqi', 25)
person('liuqi', 25, city = 'BeiJing')
# 命名关键字参数
def person2(name, age, *, city, job):
	print(name, age, city, job)
person2('liuqi', 25, city = 'Beijing', job = 'web engineer')
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 练习 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(x, y = 1, *z):
	s = x * y
	for i in z:
		s = s * i
	return s
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
# 切片
# 练习 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
	if not s:
		return ''
	start = 0
	end = -1
	l = len(s)
	while s[start] == ' ':
		start += 1
		if(start == l):
			return ''
	while (s[end] == ' '):
		end -= 1
	return s[start : end + l + 1]
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
# 迭代
dt = { 'a': 1, 'b': 2, 'c': 3 }
# 迭代key
for k in dt:
	print(k)
# 迭代value
for v in dt.values():
	print(v)
# 迭代key、value
for k, v in dt.items():
	print(k, v)
# 判断可迭代对象的方法 collections模块的Iterable类型判断
print(isinstance('abc', Iterable), isinstance([], Iterable), isinstance(123, Iterable))
# enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate([7,8,9]):
	print(i, value)
# 练习 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
	if not L:
		return (None, None)
	min = max = L[0]
	for i, value in enumerate(L):
		if value < min:
			min = value
		if value > max:
			max = value
	return (min, max)
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
# 列表生成式
print([x * x for x in list(range(1, 11))])
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
# 高阶函数 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式






























