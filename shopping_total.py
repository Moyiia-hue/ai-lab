# 任务 B：购物清单总价计算（2026-10-17）
#
# 要求：
# 1. 写一个商品列表，每件商品包含：名称、单价（元）、数量
# 2. 写一个函数，算出单件商品的小计（单价 × 数量）
# 3. 用 for 循环打印每件商品的小计，并算出总价
# 4. 自定一条规则（比如单件小计超过 100 元算“贵”），用 if 标出符合规则的商品
#
# 运行方式：在 VS Code 终端里输入  python shopping_total.py

item=[["apple",2,56],["banana",3,45],["pine",5,20]]
def xiaoji(a,b):
    return a*b
total=0
for i in item:
    result=xiaoji(i[1],i[2])
    print(i[0],result)
    if result>100:
        print("贵")
    else:
        print("便宜")
    total=total+result
print("总价",total)

