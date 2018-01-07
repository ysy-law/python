'''
面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。
而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。
'''

'''
和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
'''
class Student(object):
	def __init__(self, name, score):
		self.__name = name   # 私有变量
		self.score = score
	def printScore(self):
		print('%s:%s' % (self.__name, self.score))
	def getName(self):
		return self.__name
bart = Student('Bart', 59)
lisa = Student('lisa', 87)
bart.printScore()
lisa.printScore()
'''
和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
'''
'''
在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private）
'''
bart.age = 22
print(bart.getName(), bart._Student__name)

'''
需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
'''

# 练习 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Students(object):
	def __init__(self, name, gender):
		self.name = name
		self.__gender = gender
	def get_gender(self):
		return self.__gender
	def set_gender(self, gender):
		if gender == 'male' or gender == 'female':
			self.__gender = gender
		else:
			print('请输入male或female字符串')
barts = Students('Bart', 'male')
if barts.get_gender() != 'male':
    print('测试失败!')
else:
    barts.set_gender('female')
    if barts.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')		

# 继承和多态

class Animal():
	def run(self):
		print('animal is running')
class Dog(Animal):
	def run(self):
		print('dog is running')
class Cat(Animal):
	def run(self):
		print('cat is running')
dog = Dog()
cat = Cat()
print(dog.run(), cat.run())



















