"""
0716. Max Stack
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
"""
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x,x))
        else:
            mx = self.stack[-1][1]
            self.stack.append((x, max(x,mx)))

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()[0]
        return None
    
    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return None

    def peekMax(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return None        

    def popMax(self) -> int:
        top = self.stack.pop()
        temp = []
        while top[0] != top[1]:
            temp.append(top[0])
            top = self.stack.pop()
        for elem in temp[::-1]:
            self.push(elem)
        return top[0]


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

