import sys

class BuySellStock:
    def __init__(self, array):
        self.result = 0
        if len(array) < 2 or array == None:
            return -1
        self.array = array
        self.run()

    def run(self):
        current_buy = self.array[0]
        global_sell = self.array[1]
        global_profit = global_sell - current_buy
        current_profit = -sys.maxsize - 1

        for i in range(1, len(self.array)):
            current_profit = self.array[i] - current_buy

            if current_profit > global_profit:
                global_profit = current_profit
                global_sell = self.array[i]

            if current_buy > self.array[i]:
                current_buy = self.array[i]

        self.result = global_sell - global_profit, global_sell

    def display(self):
        return "Buy Price : " + str(self.result[0]) + " Sell Price: " + str(self.result[1])



array = [ 1, 2, 3, 4, 3, 2, 1, 2, 5 ]
result = BuySellStock(array)
print(result.display())