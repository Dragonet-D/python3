# 循环语句有 for 和 while

n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print('1 到 %d 之和为: %d' % (n, sum))

var = 1
while var == 1:
    num = int(input('输入一个数字 :'))
    print('输入的数字是:', num)

print('Good bye!')

# while else 语句

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print(count, '大于5')

# for 语句
languages = ['C', 'C++', 'Perl', 'Python']
for x in languages:
    print(x)

sites = ['Baidu', 'Google', 'Taobao']
for site in sites:
    if site == 'Runoob':
        print('菜鸟教程!')
        break
    print(site)
else:
    print('没有循环数据!')
print('完成循环!')

# range()函数
'''
    如果你需要遍历数字序列,可以使用内置range()函数
'''
for i in range(5, 9):
    print(i) # 5 6 7 8

'''
    也可以使rang以指定数字开始并指定不用的增量(甚至可以是负数, 有时这也叫做'步长')
'''
for i in range(0, 10, 3):
    print(i)

























