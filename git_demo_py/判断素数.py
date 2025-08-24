import sys
a=int(input("输入一个数"))
if a<=1:
    print("无法判断")
    sys.exit()
flag=False
for i in range(2,a):
    if a%i==0:
        flag=True
        break
if flag==True:
    print("不是一个质数")
else:
    print("是一个质数")
