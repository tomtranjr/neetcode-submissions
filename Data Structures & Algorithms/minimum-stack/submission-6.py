class MinStack:

    def __init__(self):
        self.values = []
        self.mins = []

    def push(self, val: int) -> None:
        self.values.append(val)
        val = min(val, self.mins[-1] if self.mins else val)
        self.mins.append(val)


    def pop(self) -> None:
        self.values.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        # actual soln
        return self.mins[-1]

        # ineff soln
        # res = self.values[0]
        # for element in self.values:
        #     res = min(res, element)
        # return res

        # brute soln
        # tmp = []
        # mini = self.values[-1]

        # while len(self.values):
        #     mini = min(mini, self.values[-1])
        #     tmp.append(self.values.pop())

        # while len(tmp):
        #     self.values.append(tmp.pop())

        # return mini
