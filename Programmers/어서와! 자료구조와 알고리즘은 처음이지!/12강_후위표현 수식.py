class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer_lst = []
    for s in S :
        if s.isalpha() :
            answer_lst.append(s)
        else :
            if opStack.isEmpty() :
                opStack.push(s)
            elif s == '(' :
                opStack.push(s)
            elif s == ')' :
                op = opStack.pop()
                while op != '(' :
                    answer_lst.append(op)
                    op = opStack.pop()
            elif prec[opStack.peek()] < prec[s] :
                opStack.push(s)
            else :
                while not opStack.isEmpty() :
                    if prec[opStack.peek()] >= prec[s] :
                        op = opStack.pop()
                        answer_lst.append(op)
                    else :
                        break
                opStack.push(s)

    while not opStack.isEmpty() :
        op = opStack.pop()
        answer_lst.append(op)

    answer = ''.join(answer_lst)
    return answer
