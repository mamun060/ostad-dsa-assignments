# 1 - initialize empty stack 
# 2 - traverse the array from right to left
# 3 - pop from the stack until find a smallest element
# 4 - If stack is empty return -1 

def nse(arr, n):
    stack = []
    result = [-1] * n # convert all element to the -1
    for i in range( n - 1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result

print(nse([1,3,4,2,5,1], 6))