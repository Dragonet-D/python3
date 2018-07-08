import sys
x = 'runoob'
sys.stdout.write(x + '\n')
# 数字(Number)类型
a = "12"
print(int(a))
# bool float complex
# String
'''
python 中单引号和双引号使用完全相同.
字符串可以用+运算符连接在一起,用*运算符重复.
Python中字符串有两种索引方式, 从左往右以0开始,从右往左以-1开始.
Python中的字符串不能被改变.
Python没有单独的字符类型,一个字符串就是长度为1的自字符串;
'''
print("qwertyuiop"[0: 2])
word = "字符串"
str = 'Runoob'
print(str)
print(str[0: -1]) #输出第一个到倒数第二个的所有字符 Runoo
print(str[0]) # 输出字符串第一个字符
print(str[2: 5]) # 输出第三个开始到第五个字符
print(str[2:]) # 输出从第三个开始的后的所有字符
print(str * 2)
print(str + '你好')

print('----------------')
print('hello\nrunoob')
print(r'hello\nrunoob') # 在前面添加一个r,表示原始字符串,不会发生转义

a = 'a'
b = 'b'
print(a, end=' ')
print(b, end=' ')

print('============Python import mode============')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)



