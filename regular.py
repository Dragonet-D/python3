'''
    正则表达式是一个特殊的字符序列,它能帮助你方便检查一个字符串是否模式匹配.
    Python自1.5版本起增加了re模块,他提供Perl风格正则表达式模式.
    re模块使Python语言拥有全部的正则表达式模式.
'''
import re

print(re.match('www', 'www.runoob.com').span()) # 在起始位置匹配
print(re.match('com', 'www.runoob.com')) # 不在起始位置匹配

line = 'Cats are smarter than dogs'

matchObj = re.match(r'(.*) are (.*?) .*',line, re.M|re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")

phone = "2004-959-559"
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)

def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

pattern = re.compile(r'\d+')
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result1)

it = re.finditer(r'\d+', '12a32bc43jf3')
for match in it:
    print(match.group())

re.split('\W+', 'runoob, runoob, runoob.')



















