#import random
#num = random.randint(1,100)
#print(num)


#a = input("请输入数据：")
#print(type(a))
#a = int(a)
#print(type(a))
#print("您输入的数据为：",a)

# score = input("请输入您的分数")
# score = int(score)
# if score >= 90 and score <=100:
#     print("优秀")
# elif score >=80 and score <90:
#     print("良好")
# elif score >=70 and score <80:
#     print("一般")
# elif score >= 60 and score <70:
#     print("及格")
# elif score >=0 and score <60:
#     print("不及格")
# else:
#     print("非法输入")


# start = 1
# while True:
#     if start > 5:
#         break
#     print(start)
#     start = start + 1

# import random
# rannum = random.randint(1,100)
# while True:
#     num = input("请输入一个数字：")
#     num = int(num)
#     if num > rannum:
#         print("大了")
#     elif num < rannum:
#         print("小了")
#     else :
#         print("恭喜，猜对了！数字为：",rannum)
#         break

# 实现输入10个数字，并打印10个数的求和结果
# cishu = 0
# xianyouzhi = 0
# while cishu<=10:
#     zhi = int(input("请输入一个数字"))
#     xianyouzhi = xianyouzhi + zhi
#     cishu = cishu + 1
# print("数字总和为：",xianyouzhi)

# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
# cishu = 0
# xianyouzhi = 0
# pingjunzhi = 0
# zuidazhi = 0
# while cishu < 10:
#     zhi = int(input("请输入一个数"))
#     xianyouzhi = xianyouzhi + zhi
#     cishu = cishu + 1
#     pingjunzhi = xianyouzhi / cishu
#     if zhi > zuidazhi:
#         zuidazhi = zhi
# print("数字总和为：",xianyouzhi)
# print("数字平均数为：",pingjunzhi)
# print("数字最大值为：",zuidazhi)

# 使用random模块，如何产生50~150之间的数？
# import random
# rannum = random.randint(50,150)
# print(rannum)

# 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
# a = int(input("请输入一个数字"))
# b = int(input("请输入一个数字"))
# c = int(input("请输入一个数字"))
# if a <= 0 or b <= 0 or c <= 0:
#     print("不能形成三角形")
# elif a == b == c:
#     print("为等边三角形")
# elif a == b or b == c or c == a:
#     print("为等腰三角形")
# elif a * a + b * b == c * c or a * a + c * c == b * b or c * c + b * b == a * a:
#     print("为直角三角形")
# elif a + b > c or a + c > b or b + c > a:
#     print("为普通三角形")

# 有以下两个数，使用+，-号实现两个数的调换。
# a = 56
# b = 78
# print("a=",a + 22)
# print("b=",b - 22)

# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
# cishu = 0
# username = "root"
# password = "admin"
# while cishu < 3:
#     cishu = cishu + 1
#     yh = input("请输入用户名：")
#     mm = input("请输入密码：")
#     if yh == username and mm == password:
#         print("登录成功")
#         break
#     else:
#         if cishu == 3:
#             print("锁定")
#         else:
#             print("请重新输入")

# 编程实现下列图形的打印
# x = 0
# y = 0
# while x < 8:
#     x = x + 1
#     print(" " * (8 - x),"* " * x)

# 使用while循环实现99乘法表的打印。
# x = 1
# y = 1
# while x <= 9:
#     while y <= 9:
#         print(x,"*",y,"=",x*y)
#         y = y + 1
#     y = 1
#     x = x + 1

# 编程实现99乘法表的倒叙打印
# x = 9
# y = 9
# while x >= 1:
#     while y >= 1:
#         print(x,"*",y,"=",x*y)
#         y = y - 1
#     y = 9
#     x = x - 1

# 一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
# t = 0
# g = 0
# b = 3
# w = 2
# while True:
#     t = t+1
#     g = g + b
#     if g == 20:
#         print("最终天数为：",t)
#         break
#     g = g - w
#     print("当前高度为：",g)

# 判断下列变量命名是否合法
# while True:
#     bl = input("请输入一个变量：")
#     if

# 继续完成上午的猜数字游戏的需求功能。
# 1.	添加计数打印功能

# cs = 0
# import random
# rannum = random.randint(1,10)
# while True:
#     cs = cs + 1
#     num = input("请输入一个数字：")
#     num = int(num)
#     if num > rannum:
#         print("大了")
#     elif num < rannum:
#         print("小了")
#     else :
#         print("恭喜，猜对了！数字为：",rannum)
#         print("您用了",cs,"次")
#         break

# 2.	添加次数金币功能和锁定系统功能。

# cs = 0
# import random
# rannum = random.randint(1,10)
# while True:
#     cs = cs + 1
#     num = input("请输入一个数字：")
#     num = int(num)
#     if num > rannum:
#         print("大了")
#     elif num < rannum:
#         print("小了")
#     elif cs <= 3:
#         if num == rannnum:
#             print("恭喜获得2000金币，数字为：",rannum)
#             break
#         elif cs == 20:
#             print("尝试过多，以锁定")
#             break


# 用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
# a = 1
# b = 1
# c = 0
# while a < 20:
#     while b <= a:
#         print(a,"",b)
#         c = c + (a*b)
#         b = b + 1
#     b = 1
#     a = a + 1
# print(c)
