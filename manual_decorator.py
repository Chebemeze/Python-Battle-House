def add_extra(num):
    def decorator(func):
        def wrapper(a,b):
            res = func(a, b) + num
            return res
        return wrapper
    return decorator

def sum(a, b):
    return a+b
a = add_extra(2)
b = a(sum)
print(b(2, 3))