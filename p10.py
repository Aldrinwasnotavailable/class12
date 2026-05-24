# Wap to create a stack for storing only odd numbers out of all the numbers entered by the user.

class OddNumberStack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        if item % 2 != 0:
            self.stack.append(item)
            print(f"Pushed odd number: {item}")
        else:
            print(f"Rejected even number: {item}")

    def pop(self):
        if self.is_empty():
            print("Error: Stack is empty. Cannot pop.")
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Error: Stack is empty. No item to peek.")
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)
    
if __name__ == "__main__":
    odd_stack = OddNumberStack()
    
    while True:
        try:
            num = int(input("Enter a number to push onto the stack (or type 'exit' to quit): "))
            odd_stack.push(num)
        except ValueError:
            print("Exiting...")
            break

    print("\nFinal Stack of Odd Numbers:")
    while not odd_stack.is_empty():
        print(odd_stack.pop())