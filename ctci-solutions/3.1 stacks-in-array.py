# Problem: Implement 3 stacks in one array
# Solution: Create push, pop, length functions for all 3 stacks and this should solve our purpose

class stackinarr:
    def __init__(self, A=[[], [], []]):
        self.A = A 

    def push1(self, item):
        self.A[0].append(item)

    def pop1(self):
        self.A[0].pop()

    def push2(self, item):
        self.A[1].append(item)

    def pop2(self):
        self.A[1].pop()

    def push3(self, item):
        self.A[2].append(item)

    def pop3(self):
        self.A[2].pop()

    def show(self):
        return self.A

obj = stackinarr()
obj.push1("a")
obj.push1("b")
obj.push1("c")
obj.push2("b")
obj.pop1()
obj.push2("b")
obj.push2("c")
obj.push2("c")
obj.push3("p")
obj.push3("q")
obj.pop3()
obj.pop2()
obj.show()
    

