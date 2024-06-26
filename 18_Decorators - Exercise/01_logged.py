def logged(function):

    def wrapper(*args, **kwargs):
        return f"you called {function.__name__}{args}\n" \
               f"it returned {function(*args, **kwargs)}"

    return wrapper



@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))