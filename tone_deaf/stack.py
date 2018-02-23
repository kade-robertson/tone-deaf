from random import shuffle as rshuffle

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
            moves = abs(moves) % len(self.__stk)
            if moves > 0:
                self.__stk = self.__stk[moves:] + self.__stk[:moves]
        else:
            moves = -moves
            self.__stk = self.__stk[moves:] + self.__stk[:moves]
    def item_at(self, index):
        return self.__stk[index]
    def index_of(self, item):
        return self.__stk.index(item)
    def peek(self):
        return self.__stk[-1]
    def reverse(self):
        self.__stk = self.__stk[::-1]
    def shuffle(self):
        rshuffle(self.__stk)
    def sort(self, asc = True):
        self.__stk = sorted(self.__stk)[::2*asc - 1]
