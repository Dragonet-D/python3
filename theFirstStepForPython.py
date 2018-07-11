# end 关键字
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b

# sep 参数使用
aa,bb,cc = 10, 20, 30
print(aa, bb, cc, sep='$')

def fab(n):
    if n<1:
        return
    if n==1 or n==2:
        return 1
    else:
        return fab(n-1)+fab(n-2)

print(fab(10))