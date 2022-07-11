

def mk_div(n):
    def div(x):
        assert type(x) == int, "Solo se pueden poner números"
        return x / n
    return div

def run():
    division3 = mk_div(3)
    division5 = mk_div(5)
    division10 = mk_div(10)
    print(division10(50))

if __name__ == "__main__":
    run()
