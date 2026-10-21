# 任务 B：购物清单总价计算（2026-10-17）
#
# 要求：
# 1. 写一个商品列表，每件商品包含：名称、单价（元）、数量
# 2. 写一个函数，算出单件商品的小计（单价 × 数量）
# 3. 用 for 循环打印每件商品的小计，并算出总价
# 4. 自定一条规则（比如单件小计超过 100 元算“贵”），用 if 标出符合规则的商品
#
# 运行方式：在 VS Code 终端里输入  python shopping_total.py

name="苹果"
price=5
count=3
print(name,price,count)
subtotal=price*count
print("小计",subtotal)
