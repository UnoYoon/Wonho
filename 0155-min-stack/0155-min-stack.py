class Node:
    def __init__(self, val, minVal):
        self.val = val
        self.minVal = minVal

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minVal = self.getMin()
        if val < minVal:
            self.stack.append(Node(val, val))
        else:
            self.stack.append(Node(val, minVal))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return float("inf") # 이러한 문구는 문제에 없는데 코테 볼 때 물어보기
        return self.stack[-1].minVal


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()