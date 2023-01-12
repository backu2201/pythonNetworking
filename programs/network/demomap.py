def add(num):
    return num+5
price=[10,20,15,13,45,16,33]
new_price=[]
for p in price:
    new_price.append(add(p))
print(new_price)