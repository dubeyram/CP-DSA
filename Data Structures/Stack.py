# Stack implementation in python

# A stack is an object (an abstract data type - ADT) that allows the following operations:

# Push: Add an element to the top of a stack
# Pop: Remove an element from the top of a stack
# IsEmpty: Check if the stack is empty
# IsFull: Check if the stack is full
# Peek: Get the value of the top element without removing it


# Creating a stack
def create_stack():
    stack = []
    return stack

# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0

# Adding items into the stack
def push(stack, item):
    if full(stack):
        return "Stack is full"

    stack.append(item)
    print("pushed item: " + item)

# Removing an element from the stack
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()
#Peak of the stack
def peek(stack):
        if not check_empty(stack):
            return stack[-1]

#Check if stack is full
def full(self):
    return len(stack)==6

stack = create_stack()
push(stack, "A")
push(stack, "B")
push(stack, "C")
push(stack, "D")
push(stack, "C1")
push(stack, "D1")
print("Peek of Stack:" ,peek(stack))
print("Pop the top Elment",pop(stack))
print("stack after pushing all element: " + str(stack))


'''
####Stack Applications###
Although stack is a simple data structure to implement, it is very powerful. The most common uses of a stack are:

To reverse a word - 

Put all the letters in a stack and pop them out. Because of the LIFO order of stack, you will get the letters in reverse order.

In compilers -

 Compilers use the stack to calculate the value of expressions like 2 + 4 / 5 * (7 - 9) by converting the expression to prefix or postfix form.


In browsers -

 The back button in a browser saves all the URLs you have visited previously in a stack. Each time you visit a new page, it is added on 
 top of the stack. When you press the back button, the current URL is removed from the stack and the previous URL is accessed.
 '''
