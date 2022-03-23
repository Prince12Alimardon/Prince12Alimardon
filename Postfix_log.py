def createStack():
    stack = list()
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if (isEmpty(stack)):
        return False

    return stack.pop()
def size(stack):
    return len(stack)
def top(stack):
    if (isEmpty(stack)):
        return False
    return stack[len(stack) - 1]


stack = createStack()
str1 = input()
l = len(str1)
for i in range(l):
    if str1[i] == '0' or str1[i] == '1':
        a = int(str1[i])
        push(stack, a)
    elif str1[i] == '!':
        a = pop(stack)
        b = not a
        push(stack, b)
    elif str1[i] == '&':
        a = pop(stack)
        b = pop(stack)
        push(stack, a and b)
    elif str1[i] == '|':
        a = pop(stack)
        b = pop(stack)
        push(stack, a or b)
    elif str1[i] == '=':
        a = pop(stack)
        print(a)
    else:
        print('\nERROR\n')
        break
