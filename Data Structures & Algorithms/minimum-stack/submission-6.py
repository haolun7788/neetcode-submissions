class MinStack:
    
    def __init__(self):
        self.lis = []
        self.minsofar = []

    def push(self, val: int) -> None:
        self.lis.append(val)
        if not self.minsofar or val < self.minsofar[-1]:
            self.minsofar.append(val)
        else:
            self.minsofar.append(self.minsofar[-1])

    def pop(self) -> None:
        self.lis.pop()
        self.minsofar.pop()

    def top(self) -> int:
        return self.lis[-1]

    def getMin(self) -> int:
        return self.minsofar[-1]

