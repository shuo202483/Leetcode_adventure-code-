class MyQueue:
    def __init__(self):
        self.in_stack, self.out_stack = [], []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def _move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        self._move()
        return self.out_stack.pop()          # 记得 return！

    def peek(self) -> int:
        self._move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not (self.in_stack or self.out_stack)


ops   = ["MyQueue","push","pop","empty"]
args  = [[],[1],[],[]]

obj   = None
res   = []
for op, arg in zip(ops, args):
    if op == "MyQueue":
        obj = MyQueue()
        res.append(None)          # 构造函数的返回值总是 null
    else:
        out = getattr(obj, op)(*arg)
        res.append(out)
print(res)