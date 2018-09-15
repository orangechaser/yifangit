def test1():
    names = ['bob','lisa','angel']
    for abc in names:
        print(abc)

def test2():
    sum = 0
    b = [1,2,3,4,5,6,7,8,9,10]
    for x in b:
        sum = sum + x
    print(sum)

def test3():
    sum = 0
    b = list(range(101))
    for x in b:
        sum = sum + x
    print(sum)

def test4():
    sum = 0
    n = 99
    while n > 0:
        sum = sum + n
        n = n - 2
    print(sum)

# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
# L = ['Bart', 'Lisa', 'Adam']

def test5():
    L = ['Bart', 'Lisa', 'Adam']
    for x in L:
        print("Hello",x)

# 打印出1~100

def test6():
    n = 1
    while n <= 100:
        print(n)
        n = n + 1
    print("End")

def test7():
    n = 1
    while n<= 100:
        if n > 10:
            break
        print(n)
        n = n + 1
    print("End")

# 打印1～10的偶数
def test8():
    n = -1
    while n < 10:
        n = n + 1
        if n % 2 == 1:
            continue
        print(n)

test8()