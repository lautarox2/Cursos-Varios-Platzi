import time

class FiboIter():

    def __init__(self, max_num: int):
        self.max_num = max_num

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter ==1:
            self.counter +=1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            if self.aux >= self.max_num:
                raise StopIteration
            self.n1, self.n2 = self.n2, self.aux
            self.counter +=1
            return self.aux


if __name__ == "__main__":
    fibonacci = FiboIter(150)
    for element in fibonacci:
        print(element)
        time.sleep(0.5)