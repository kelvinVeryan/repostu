#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 如果函数的结果是返回一个函数，那返回函数里不要引用任何循环变量，或者后续会发生变化的变量，会造成前面的返回函数执行结果与变量变化后一样。
def count():
	fs=[]
	for i in range(1,4):
		print ('i: %d' % i )
		def f():
			return i*i
		
		fs.append(f)
		print ('fs : %s' % str(fs) )
	return fs

#print (count()[0]())
#print (count()[1]())
#print (count()[2]())
f1,f2,f3=count()
#print f1()
#f2()
#f2()
print (f1)
print (f1())
print (f2)
print (f2())
print (f3)
print (f3())

print ('======================================================')

def count1():
	fs=[]
	def f():
		return i*i
	for i in range(1,4):
		print ('i: %d' % i )
		fs.append(f)
	return fs
f1,f2,f3=count1()
print (count1())
print (f1)
print (f1())
print (f2)
print (f2())
print (f3)
print (f3())

print ('======================================================')
# 解决上面问题的方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
# 就是fs.append(f(i))和fs.append(f)的区别
def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1,f2,f3=count2()
print (f1)
print (f1())
print (f2)
print (f2())
print (f3)
print (f3())

print ('======================================================')
# 利用闭包返回一个计数器函数，每次调用它返回递增整数： nonlocal 把i声明成了非局部变量 
def createCounter():
    i=0
    def counter():
        nonlocal i
        i+=1
        return i
    return counter
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
