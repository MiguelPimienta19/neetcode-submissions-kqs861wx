class MinStack:

    def __init__(self):
        self.regularstack = []
        self.minstack = []
        

    def push(self, val: int) -> None:

        self.regularstack.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)

        

    def pop(self) -> None:
        self.regularstack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.regularstack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
