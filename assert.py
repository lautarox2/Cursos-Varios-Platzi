from multiprocessing.sharedctypes import Value


def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input("ingresa un número: ")
    assert num.isnumeric() and int(num) > 0, "Debe ser postivo"
    print(divisors(num))
    print("Terminó el programa")

if __name__ == "__main__":
    run()