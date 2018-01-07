# python 数据类型
# Number       (数字)
# String       (字符串)
# List         (列表)
# Tuple        (元组)
# Sets         (集合)
# Dictionary   (字典)

# Number类型
# int     整数
# float   浮点数
# bool    布尔
# complex 复数
a, b, c, d = 1, 2.0, True, 4 + 3j

# type() isinstance()用法、区别
'''
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
'''
print(type(a), type(b), type(c), type(d))
print(isinstance(a, int), isinstance(b, float), isinstance(c, bool), isinstance(d, complex))
print(int)

# String类型
'''
Python中的字符串用单引号(')或双引号(")括起来，同时使用反斜杠(\)转义特殊字符。
字符串的截取的语法格式如下：
变量[头下标:尾下标]
索引值以 0 为开始值，-1 为从末尾的开始位置。

加号 (+) 是字符串的连接符， 星号 (*) 表示复制当前字符串，紧跟的数字为复制的次数。
'''
str = 'liuqi'
print(str[0:-1])
print(str + 'luodan')
print(str * 2)

'''

函数	       描述
int(x [,base]) 将x转换为一个整数
float(x)       将x转换到一个浮点数
complex(real [,imag]) 创建一个复数
str(x)         将对象 x 转换为字符串
repr(x)        将对象 x 转换为表达式字符串
eval(str)      用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)       将序列 s 转换为一个元组
list(s)        将序列 s 转换为一个列表
set(s)         转换为可变集合
dict(d)        创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s)   转换为不可变集合
chr(x)         将一个整数转换为一个字符
ord(x)         将一个字符转换为它的整数值
hex(x)         将一个整数转换为一个十六进制字符串
oct(x)         将一个整数转换为一个八进制字符串
'''



















