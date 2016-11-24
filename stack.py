class Stack():
    def __init__(self):
        self.__stk = []
    def __len__(self):
        return len(self.__stk)
    def __str_rep(self, item):
        if type(item) in (int, float):
            return str(item)
        elif type(item) is str:
            if len(item) == 1:
                return "'"+item
            else:
                return '"'+item+'"'
        elif type(item) is list:
            return '['+' '.join(list(map(self.__str_rep, item))) + ']'
    def __str__(self):
        return '['+' '.join(list(map(self.__str_rep, self.__stk))) + ']'
    def pop(self, index=-1):
        return self.__stk.pop(index)
    def push(self, item, index=-1):
        if index == -1: index = len(self)
        self.__stk.insert(index, item)
    def rotate(self, moves=1):
        if moves < 1:
            moves = abs(moves)
            while moves:
                temp = self.__stk.pop(0)
                self.__stk.append(temp)
                moves -= 1
        else:
            while moves:
                temp = self.__stk.pop()
                self.__stk.insert(0, temp)
                moves -= 1
    def item_at(self, index):
        return self.__stk[index]
    def index_of(self, item):
        return self.__stk.index(item)
    def peek(self):
        return self.__stk[-1]
