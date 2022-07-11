def read():
    num = []
    with open("./archivos/num.txt", "r", encoding="utf-8") as f:
        for line in f:
            num.append(int(line))
    print(num)

def write():
    names = ["facundo", "tati", "lauti"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for names in names:
            f.write(names)
            f.write("\n")

def run():
    write()


if __name__ == "__main__":
    run() 