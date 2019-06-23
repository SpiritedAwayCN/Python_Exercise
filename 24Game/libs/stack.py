class Stack:
    def __init__(self):
        self.__stk = []

    def empty(self):
        return self.__stk == []

    def push(self, item):
        return self.__stk.append(item)
    
    def pop(self):
        return self.__stk.pop()

    def top(self):
        return self.__stk[len(self.__stk)-1]
    
    def size(self):
        return len(self.__stk)