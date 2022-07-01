
def df_dec(dx = 5):
    def func_dec(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs) * dx
            return res
        return wrapper
    return func_dec

@df_dec(dx = 5)
def func(x):
    return x**2

print(func(5))
