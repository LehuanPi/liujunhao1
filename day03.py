# sh = ["北京","上海","广东"]
# sh.append("天津")
# sh.append("重庆")
# sh.append("哈尔滨")
# sh.append("银川")
# sh.append("郑州")
# sh.append("济南")
# sh.append("太原")
# sh.append("合肥")
# sh.append("长春")
# sh.append("沈阳")
# sh.append("呼和浩特")
# sh.append("石家庄")
# sh.append("乌鲁木齐")
# sh.append("兰州")
# sh.append("西京")
# sh.append("西安")
# sh.append("长沙")
# sh.append("武汉")
# sh.append("南京")
# sh.append("成都")
# sh.append("贵阳")
# sh.append("昆明")
# sh.append("南宁")
# sh.append("拉萨")
# sh.append("杭州")
# sh.append("南昌")
# sh.append("广州")
# sh.append("福州")
# sh.append("台北")
# sh.append("海口")
# sh.append("香港")
# sh.append("澳门")
#
# sh.remove("广东")
# sh.insert(1,"广东")
#
# print(sh)

# gdp = [36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# cs = 0
# z = 0
# zh=round(sum(gdp),2)
# ws=len(gdp)
# pj=zh/ws
# print(zh,pj)

# gdp=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# a = 0
# z=0
# while a <= 7:
#     z=z+gdp[a]
#     a = a + 1
# print(round(z,2),round(z/8,2))


# a = [1,5,21,30,15,9,30,24]
# cs = 0
# z = 0
# while cs < 8:
#     if a[cs]%5 == 0:
#         z = z + a[cs]
#     cs = cs + 1
# print(z)


# List = [1,2,3,4,5,6,7,8,9]
# b=list(reversed(List))
# print(b)

cs = 0
s = 0
List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
while cs < 15:
    s = List.count(List[cs])


    cs = cs + 1
print(s)