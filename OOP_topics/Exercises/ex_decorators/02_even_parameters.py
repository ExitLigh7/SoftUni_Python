def even_parameters(function):
    def wrapper(*args):
        are_params_even_nums = True
        for arg in args:
            if isinstance(arg, int):
                if not arg % 2 == 0:
                    are_params_even_nums = False
            else:
                are_params_even_nums = False

        if not are_params_even_nums:
            return "Please use only even numbers!"

        out = function(*args)
        return out

    return wrapper


@even_parameters
def func(*args):
    return sum(args)


print(func(4, "4", 4))




