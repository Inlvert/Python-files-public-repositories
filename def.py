def add(x, y):
    return X + y
def bar(x):
    add(x, "1", "2")
add.__code__ = bar.__code__
add(42)
