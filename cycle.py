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
    print(i) # 0 3 6 9

for i in range(-10, -100, -30):
    print(i) # -10 -40 -70

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

print(list(range(5))) # [0, 1, 2, 3, 4]

# break和continue语句及循环中的else字句
'''
    break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
'''
for letter in 'Runoob':
    if letter == 'b':
        break
    print(letter)

var1 = 10
while var1 > 0:
    print(var1)
    var1 = var1 - 1
    if var1 == 5:
        break

print('Good bye!')

'''
    continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环
'''

for letter in 'Runoob':
    if letter == 'o':
        continue
    print(letter)

var2 = 10
while var2 > 0:
    var2 -= 1
    if var2 == 5:
        continue
    print(var2)

print('Good bye')

'''
    循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,但循环被break终止时不执行
'''

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, '是质数')

# pass 语句
'''
    Python pass是空语句，是为了保持程序结构的完整性。
    pass 不做任何事情，一般用做占位语句
'''
while True:
    pass
    break

sequence = [12, 34, 34, 23, 123, 3123]
for i, j in enumerate(sequence):
    print(i, j)

n = 0
summ = 0
for n in range(0, 101): # n 范围0-100
    summ += n
print(summ)

i = 1
while i <= 9:
    j = 1
    while j <= i:
        mut = j*i
        print('%d * %d = %%d'%(j,i,mut), end=' ')
        j += 1
    print('')
    i+=1



