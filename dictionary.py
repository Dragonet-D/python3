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
# dictProperty = {['Name']: 'Runoob', 'Age': 7} # 用列表会报错
# print(dictProperty)

# 字典内置函数和方法
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
len(dict) # 长度 即键的总数
str(dict) # 输出字典, 也可以打印字符串表示
type(dict) # 返回输入的变量类型, 如果变量是字典就返回字典类型

dict.clear()
dict.copy()

dictFromkeys = {'name': 'xiaoming', 'age':18}
dictfromkeys = dictFromkeys.fromkeys('name', 10)
# 创建一个新字典, 以序列seq中元素做字典的键, val为字典所有键对应的初始值
# {'n': 10, 'a': 10, 'm': 10, 'e': 10}
print(dictfromkeys)

dictGet = dictFromkeys.get('name', None)
print(dictGet)
print("name" in dict)
print(dictFromkeys.items()) # dict_items([('name', 'xiaoming'), ('age', 18)])
print(dictFromkeys.keys()) # dict_keys(['name', 'age'])

# 	radiansdict.update(dict2)

dict1 = {'name': 'xiaoming'}
dict2 = {'age': 123}
dict1.update(dict2) # 合并dict2到dict1
print(dict1)

dict1.setdefault('sex', 'male')
print(dict1)

print(list(dict1.values())) # ['xiaoming', 123, 'male']

site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj = site.pop('name')
print(pop_obj) # 菜鸟教程
print(site) # {'alexa': 10000, 'url': 'www.runoob.com'}

site.popitem() # 随机返回并删除字典中的一对键和值