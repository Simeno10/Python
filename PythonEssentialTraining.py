# Python code​​​​​​‌‌​​​‌‌​​‌​​​​‌​​‌‌​‌​​‌​ below
class NonIntArgumentException(Exception):
    pass

def handleNonIntArguments(func):
    def wrapper(*args):
        try:
            for i in args:
                if(type(i) is not int):
                    raise NonIntArgumentException("NonIntArgumentException")
            return func(*args)
        except TypeError:
            print('There was a type error!')
    return wrapper
