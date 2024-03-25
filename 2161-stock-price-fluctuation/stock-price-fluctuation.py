class StockPrice:
    def __init__(self):
        self.map = {} # maps time to price
        self.latest = 0 # latest time we have seen so far
        self.max = 0
        self.maxTime = 0
        self.min = float('inf')
        self.minTime = 0

    def update(self, timestamp, price):
        self.map[timestamp] = price

        self.latest = max(self.latest, timestamp)

        if price > self.max:
            self.max = price
            self.maxTime = timestamp

        if price < self.min:
            self.min = price
            self.minTime = timestamp

    def current(self):
        return self.map[self.latest]
    
    def maximum(self):
        if self.map[self.maxTime] == self.max:
            return self.max
        
        self.max = 0
        
        for time, price in self.map.items():
            if price > self.max:
                self.max = price
                self.maxTime = time

        return self.max
    
    def minimum(self):
        if self.map[self.minTime] == self.min:
            return self.min
        
        self.min = float('inf')
        
        for time, price in self.map.items():
            if price < self.min:
                self.min = price
                self.minTime = time

        return self.min