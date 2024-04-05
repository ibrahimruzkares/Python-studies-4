x = "global x"

def outer():
    x = "enclosing x"
    print(x)
    def inner():
        x = "local x"
        print(x)
    inner()

outer()
print(x)
