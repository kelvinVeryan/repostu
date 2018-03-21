#!/usr/bin/python3
# -*- coding: utf-8 -*-
# map and reduce 
# 程序是把一个符合标准字符串转换为对应的浮点数
# map用法是第一个函数逐一运行在后面的list数据里，只有一个参数。
# reduce的用法是把第一个函数的逐一运行在后面的两个数据里，接收两个参数。均生成新的Iterator返回。
# 小数的算法。
from functools import reduce

def str2float(s):
    DIGITS = {'.':'.','0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def digit(x):
        return DIGITS[x]
    def mul(x,y):
        return x*10+y
    # posi,nega =s.split('.') #这么用更简洁
    pot=s.find('.')
    print (pot)
    positive=reduce(mul,map(digit,s[:pot]))
    negative=reduce(mul,map(digit,s[pot+1:]))/(10**len(s[pot+1:]))
    return positive+negative
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

print ('=========================================================')

# 20180313增加，求1到999内没有1的数字
# 其实本问题简单来想，三位数字，每一个在0-9之间选择除了1的9个数，9*9*9再减去一个0即可。
def haveone(s):
	for char in s:
		if char=='1':
			print(s)
			return 0
	return 1
nums=0
for num in range(1,1001):
	nums=nums+haveone(str(num))
print(nums)
