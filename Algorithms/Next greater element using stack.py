# Python program to print next greater element using stack

# Stack Functions to be used by printNGE()

def CreateStack():
    stack = []
    # print(stack)
    return stack

def IsEmpty(stack):
    return len(stack)==0

def push(stack,i):
    stack.append(i)

def StackTop(stack):
    return stack[-1]

def pop(stack):
    return stack.pop()

        
def printNGE(arr,n):
    peak = [0]*len(arr)
    stack = CreateStack()
    for i in range(n):
        if IsEmpty(stack):
            push(stack,i)
     
        else:
            if arr[StackTop(stack)]<arr[i]:

                while not IsEmpty(stack) and arr[StackTop(stack)]<arr[i]:
                    
                    a=pop(stack)
                    peak[a]= i-a

                push(stack,i)

            else:
                push(stack,i)
                
    return peak

# Driver code
arr = [73,74,75,71,69,72,76,73]
n=len(arr)
print(printNGE(arr,n))


