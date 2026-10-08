from functools import wraps
def add_extra(num):
    def decorator(func):
        @wraps(func)
        def wrapper(a,b):
            res = func(a, b) + num
            return res
        return wrapper
    return decorator
@add_extra(2)
def sum(a, b):
    """sums two numbers, a and b"""
    return a+b
print(sum(2, 3))

# wraps gotten from functools makes the metadata
# from the decorated function kept and not lost.
print(sum.__doc__)
print(sum.__name__)
