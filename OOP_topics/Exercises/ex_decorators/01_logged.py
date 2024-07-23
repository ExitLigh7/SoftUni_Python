def logged(func):
    def wrapper(*args, **kwargs):
        # Get the function name
        func_name = func.__name__

        # Log the function call details
        args_list = ", ".join(map(str, args))
        kwargs_list = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [args_list, kwargs_list]))

        output = f"you called {func_name}({all_args})\n"

        # Call the actual function
        result = func(*args, **kwargs)

        # Log the result
        output += f"it returned {result}"
        return output

    return wrapper


@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))