def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):  # 只需要判断到 sqrt(n)
        if n % i == 0:
            return False
    return True

a = int(input("输入一个数: "))
if is_prime(a):
    print(a,"是一个质数")
else:
    print(a,"不是一个质数")