names = ["Ahmet", "AYşE","oNuR", "HÜseYin"]

def upper(x):
    x = x.upper()
    return x

names2 = list(map(upper,names))
print(names2)

names3 = list(map(lambda x: x.upper(), names))
print(names3)

names4 = list(map(lambda x: x.capitalize(), names))
print(names4)