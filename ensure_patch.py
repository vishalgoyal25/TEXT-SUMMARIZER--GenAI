import inspect
from functools import wraps

def ensure_annotations(func):
    sig = inspect.signature(func)

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()

        for name, value in bound.arguments.items():
            expected_type = func.__annotations__.get(name)
            if expected_type and not isinstance(value, expected_type):
                raise TypeError(f"Argument '{name}' must be {expected_type}, got {type(value)}")

        result = func(*args, **kwargs)

        expected_return_type = func.__annotations__.get('return')
        if expected_return_type and not isinstance(result, expected_return_type):
            raise TypeError(f"Return value must be {expected_return_type}, got {type(result)}")

        return result

    return wrapper
