# Python 条件语句是通过一条或多条语句执行的结果来决定的代码块
a = 10
if a > 10:
    print(True)
elif a < 1:
    print(a)
else:
    print('others')

age = int(input("请输入你家狗狗的年龄"))
print('')
if age<0:
    print('are you kidding me ?')
elif age == 1:
    print('相当于14岁的人')
elif age == 2:
    print('相当于22岁的人')
elif age > 2:
    human = 22 + (age - 2) * 5
    print('对应人类的年龄:', human)

number = 7
guess = -1
print('猜字谜游戏')
while guess != number:
    guess = int(input('请输入数字:'))
    if guess == number:
        print('恭喜, 你猜对了')
    elif guess < number:
        print('你猜小了...')
    elif guess > number:
        print('你猜大了')

# if 嵌套
num = int(input("输入一个数字"))
if num % 2 == 0:
    if num % 3 == 0:
        print('你输入的数字可以整除2 和 3')
    else:
        print('你输入的数字可以整除2, 但是不可以整除3')
else:
    if num % 3 == 0:
        print('你输入的数字可以整除3, 但不能整除2')
    else:
        print('你输入的数字不能整除2 和 3')

import random
x = random.choice(range(100))
y = random.choice(range(200))
if x > y:
    print(x)
elif x == y:
    print(x + y)
else:
    print(y)
















