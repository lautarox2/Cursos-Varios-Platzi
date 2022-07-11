from datetime import datetime

def exe_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron" + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@exe_time
def random_func():
    for _ in range(1,1000000):
        pass

def suma(a: int, b: int) -> int:
    return a + b


suma(5, 5)
#random_func()


