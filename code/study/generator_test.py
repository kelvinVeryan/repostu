#!/usr/bin/python3
# -*- coding: utf-8 -*-
g = (x * x for x in range(10))
print ('g: %s ' % g)
for n in g:
	print(n)
print ('===================================')
print ('g定义的是一个generator,实际由next() 不断计算下一个值然后输出,因此只有第一遍有执行结果.')
for n in g:
	print(n)
print ('===================================')

'''
杨辉三角定义如下：

          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
实现该三角形的程序
'''

def triangles():
	l=[1]
	while 1:
		print ('preview: %s' % l)
		yield l
		print ('yield after: %s' % l)
		#这里面的l[n]和l[n+1]是已有的generator_l中的每个位置的值
		l = [1] + [ l[n] + l[n+1] for n in range(len(l)-1) ]  + [1] 
		#for tmp in l:
		#	print (tmp)
		print ('computer after: %s' % l)
	

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
