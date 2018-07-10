'''
    元组与列表类似,不同之处在于元组不能修改.
'''
tup1 = ('Google', 'Runoob', 1997, 2000)
print(type(tup1))

# 创建空元组

tup2 = ()
print(type(tup2))

tup3 = (50,)
tup4 = (50)
print(type(tup3))
print(type(tup4))

# 访问元组
tuple1 = (123, 222, '123123', 'google')
tuple2 = (1,)
print(tuple1[0])
print(tuple1[2:5])

# 修改元组
print(tuple1 + tuple2)

# 元组运算符
tupleForCalc = ('Google')
tupleForCalc2 = ('Google')
len(tupleForCalc)
tupleForCalc3 = tupleForCalc + tupleForCalc2
print(tupleForCalc3 * 4)
isTrue = 3 in (1, 2, 3) # 元素是否存在 True
for x in tuple1:  # 迭代
    print(x)

# 元组索引, 截取

L = ('Google', 'Taobao', 'Runoob')
print(L[2])
print(L[-2])
print(L[1:])

# 元组内置函数

len(tupleForCalc)
max(tupleForCalc)
min(tupleForCalc)
tuple([1, 2, 3]) # 把列表转换为元组




















