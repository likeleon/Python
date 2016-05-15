import time
from functools import wraps

def timethis(func):
    '''
    실행 시간을 보고하는 데코레이터
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n:int):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1

countdown(100000)
countdown(10000000)

print(countdown.__doc__)
print(countdown.__annotations__)
countdown.__wrapped__(100000)

from inspect import signature
print(signature(countdown))