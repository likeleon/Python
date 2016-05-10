def spam(a, b=42):
    print(a, b)

spam(1)
spam(1, 2)

def spam(a, b=None):
    if b is None:
        b = []
    print(a, b)

spam(1)
spam(1, [2, 3, 4])

_no_value = object()
def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supllied')
    print(a, b)

spam(1)
spam(1, 2)
spam(1, None)

x = 42
def spam(a, b=x):
    print(a, b)
spam(1)
x = 23
spam(1)