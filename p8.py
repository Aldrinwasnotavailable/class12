#Wap to implement push,pop and peek

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Adds an item to the top of the stack."""
        self.items.append(item)
        print(f"Pushed: {item}. Stack: {self.items}")

    def pop(self):
        """Removes and returns the item from the top of the stack."""
        if self.is_empty():
            print("Error: Stack is empty. Cannot pop.")
            return None
        popped_item = self.items.pop()
        print(f"Popped: {popped_item}. Stack: {self.items}")
        return popped_item

    def peek(self):
        """Returns the item at the top of the stack without removing it."""
        if self.is_empty():
            print("Error: Stack is empty. No item to peek.")
            return None
        top_item = self.items[-1]
        print(f"Peeked: {top_item}. Stack remains: {self.items}")
        return top_item

    def size(self):
        """Returns the number of items in the stack."""
        return len(self.items)

if __name__ == "__main__":
    my_stack = Stack()

    print("--- Pushing elements ---")
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)

    print("\n--- Peeking at the top element ---")
    my_stack.peek()

    print("\n--- Popping elements ---")
    my_stack.pop()
    my_stack.pop()

    print("\n--- Peeking after pops ---")
    my_stack.peek()

    print("\n--- Popping from an empty stack ---")
    my_stack.pop()
    my_stack.pop()
    my_stack.peek()