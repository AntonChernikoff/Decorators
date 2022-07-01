import datetime

def file_log_decorator(file_log = 'function_errors.log'):
    def log_function(old_func):
        def new_func(*args, **kwargs):
            text = f"{datetime.datetime.now()} функция {old_func.__name__}{args}{kwargs}"
            something = old_func(*args, **kwargs)
            text = f"{text} return {something}\n"
            # print(f"{text} return {something}")
            with open(file_log, 'a', encoding='utf8') as file:
                file.write(text)
            return something
        return new_func
    return log_function

@file_log_decorator(file_log = 'func_sum.log')
def func_sum(a, b):
    return a + b

if __name__ == '__main__':
    print(func_sum(2,3))

