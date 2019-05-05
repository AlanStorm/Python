# 权重
goods = [{"name": "good1", "price": 200, "sales": 100, "stars": 5, "comments": 400},
         {"name": "good2", "price": 300, "sales": 120, "stars": 4, "comments": 500},
         {"name": "good3", "price": 500, "sales": 3000, "stars": 2, "comments": 199},
         {"name": "good4", "price": 1288, "sales": 8, "stars": 5, "comments": 398},
         {"name": "good5", "price": 899, "sales": 99, "stars": 5, "comments": 2000}]


# 权重
# 价格占的权重是40%，销量占的权重是17%，评级占的权重是13%，评论占的权重是30%
# sorted() 进行排序
def my_sorted(arg):
    price = arg['price']
    sales = arg['sales']
    star = arg['stars']
    comment = arg['comments']
    data = price * 0.4 + sales * 0.17 + star * 0.13 + comment * 0.3
    return data


print(sorted(goods, key=my_sorted))

r = sorted(goods, key=lambda x: x['price'] * 0.4 + x['sales'] * 0.17 + x['stars'] * 0.13 + x['comments'] * 0.3,
           reverse=True)
print(r)
