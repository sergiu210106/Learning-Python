import datetime

def time_it(function):
    def wrapper():
        start = datetime.datetime.now()
        function()
        end = datetime.datetime.now()
        print(end - start)
    return wrapper

@time_it 
def f():
    print("letsgoo\t", end = "")
    
@time_it 
def g():
    for _ in range(100_000):
        pass
    
@time_it  
def h():
    for _ in range(100_000_000):
        pass
    
if __name__ == '__main__':
    print("time for f(): ", end = "")
    f()
    print("time for g(): ", end = "")
    g()
    print("time for h(): ", end = "")
    h()