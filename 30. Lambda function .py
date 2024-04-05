def square(x):
    return x * x
print(square(5))


square = lambda x: x * x
print(square(3))

add = lambda x, y: x + y
print(add(4,42))

gen_total = lambda *args: sum(args)
print(gen_total(1,2,6,3,7))

print((lambda x,y,z: x * y + z)(3,5,6))
print((lambda *args: sum(args)/len(args))(12,14,16))