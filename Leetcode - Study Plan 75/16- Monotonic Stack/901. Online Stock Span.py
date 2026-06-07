# 901. Online Stock Span

class StockSpanner:

    def __init__(self):
        self.stack = []     # [(price, count), ...]

    def next(self, price: int) -> int:
        count = 1
        while self.stack and self.stack[-1][0] <= price:
            count += self.stack.pop()[1]
        self.stack.append((price, count))

        return count


inputs = [
    ([[], [100], [80], [60], [70], [60], [75], [85]], [None, 1, 1, 1, 2, 1, 4, 6])
]
for inp, resul in inputs:
    s = StockSpanner()
    my_result = []
    for price in inp:
        if not price:
            count = None
        else:
            count = s.next(price[0])
        my_result.append(count)
    print(my_result, my_result == resul)
