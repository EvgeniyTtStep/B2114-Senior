import time

def time_check(function):
    def time_check1(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        a = end - start
        print(f"час {a} ")
        return end - start
    return time_check1


def one():
    sum = 0
    for i in range(1, 1000000001):
        #print(i)
        sum = sum + i

decor = time_check(one)
result =decor()