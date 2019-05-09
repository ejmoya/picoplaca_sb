def not_empty(func):
    def wrapper(arg):
        try:
            if not arg:
                raise Exception("The input can not be empty")
            res = func(arg)
            return res
        except Exception as e:
            print('Error: ' + str(e))
    return wrapper
