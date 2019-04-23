from random import seed
from random import randint
# seed random number generator
seed(1)

class Random:
    '''
    generate some integers
    '''
    def __init__(self, total ,low, high):
        self.total = total
        self.low = low
        self.high = high
        self.genArray = []

    def generate(self):
        self.__empty_if_full()
        for _ in range(self.total):
            value = randint(self.low, self.high)
            self.genArray.append(value)
        return self.genArray

    def __empty_if_full(self):
        if len(self.genArray) > 0:
            self.genArray = []
