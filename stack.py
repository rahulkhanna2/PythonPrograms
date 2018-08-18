ls = []
global top
top = 0

def show():
        if len(ls) == 0:
            top = None
            return "list is empty"
        
        else:
            global top
            return ls ,("top_ptr:",ls[top-1])

def push(x):
    global top
    ls.append(x)
    top += 1
    
def pop():
    global top
    ls.pop()
    top -= 1
