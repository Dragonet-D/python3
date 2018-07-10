# 字典是另一种可变容器模型,且可存储任意类型对象.
d = {'key1': 1, 'key2': 'hello'}
d2 = {123: 123, 'abc': 124}

# 访问字典里面的值 如果访问字典没有的值就会报错
print(d['key1'])

# 修改字典
dictChange = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dictChange['Name'] = 123
print(dictChange)

# 删除字典元素
dictDel = {'Name': 'Runoob', 'Age': 7}
dictDel.clear() # 清空字典
del dictDel # 删除字典

# 字典的特性
'''
    键是不可变,所以可以用数字, 字符串或元组充当,用列表就不行
'''
dictProperty = {['Name']: 'Runoob', 'Age': 7} # 用列表会报错
print(dictProperty)

# 字典内置函数和方法
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
len(dict) # 长度 即键的总数
str(dict) # 输出字典, 也可以打印字符串表示
type(dict) # 返回输入的变量类型, 如果变量是字典就返回字典类型

dict.clear()
dict.copy()
dict.fromkeys() #
