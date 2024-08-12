def multiply(multiplier):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            multiplied_result = result * multiplier
            return multiplied_result
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
