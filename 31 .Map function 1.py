products = [["Shoe",150], ["Pants",120], ["Shirt",100], ["Coat",200]]

def discount(x):
    product , price = x[0], x[1]
    price = price * 0.9
    return [product, price]

result = list(map(discount, products))
print(result)
