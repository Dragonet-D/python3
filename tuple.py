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
print(tuple1[0])
print(tuple1[2:5])
