from math import exp #Global since sigmoid may be called a lot

def __listAct(inp,func): #Bad code maybe
    #But I wanted the functions themselves to look clean
    out = []
    for i in inp:
        out.append(func(i))
    return out

def linear(inp):
    if type(inp) == list:
        return __listAct(inp,linear)
        
    if inp > 1:
        return 1
    if inp < 0:
        return 0
    return inp

def sigmoid(inp):
    if type(inp) == list:
        return __listAct(inp,sigmoid)

    return 1 / ( 1 + exp(-inp))

def rectlin(inp): #Linear but uncapped positive
    if type(inp) == list:
        return __listAct(inp,rectlin)
        
    if inp < 0:
        return 0
    return inp
