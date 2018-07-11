# 集合(set)是一个无序不重复元素的序列
'''
    可以使用大括号{}或者set()函数创建集合,注意:创建一个空集合必须用set()而不是{},因为{}是用来创建一个空字典.
'''
parameter = {'1', '2'}
parameter2 = set('123')
print(parameter, parameter2)

basket = {'apple', 'orange', 'pear', 'banana'}
isHave = 'apple' in basket
print(isHave)

a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b) # 集合a中包含元素而b中不包含的元素
print(a|b) # 并集
print(a & b) # 交集
print(a ^ b) # 不同时包含于a和b的元素

aaa = {x for x in "aaaaaasdasdasdweqw" if x not in 'abc'}
print(aaa)