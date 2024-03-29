class Stack:

    def __init__(self):
        self.data = []

    def push(self, element) -> None:
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1] if self.data else None

    def is_empty(self):
        if not self.data:
            return True
        return False

    def __str__(self):

        return f"[{', '.join(str(x) for x in reversed(self.data))}]"

