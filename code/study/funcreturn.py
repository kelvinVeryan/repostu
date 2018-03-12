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
		
	
