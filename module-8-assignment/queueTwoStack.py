stack1 = []
stack2 = []

def enqueue(value):
    stack1.append(value)

def dequeue():
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())
    if stack2:
        print(stack2.pop())

def front():
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())
    if stack2:
        print(stack2[-1])

operations = [
    (1, 10),
    (1, 20),
    (3,),
    (2,),
    (3,),
    (2,)
]

for op in operations:
    if op[0] == 1:
        enqueue(op[1])
    elif op[0] == 2:
        dequeue()
    elif op[0] == 3:
        front()
