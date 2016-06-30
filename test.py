
def logger(func):
    def inner(*args, **kwargs):
        print "Arguments were %s and %s" % (args, kwargs)
        print "do other stufs"
        return func(*args, **kwargs)
    return inner

@logger
def foo(x,y):
    return x + y

print foo(5,y=1)