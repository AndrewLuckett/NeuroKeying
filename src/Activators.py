from math import exp  # Global since sigmoid may be called a lot

"""
Pattern of:

class name(Activator):
    def activator(in):
        return out

    def derivative(in):
        return out

more so static than OO
Just a grouping of two related funcs
functional prog?
"""


class Activator:  
    def __listAct__(this, inp, func):
        out = []
        for i in inp:
            out.append(func(i))
        return out


class Linear(Activator):
    def activator(this,inp):
        if type(inp) == list:
            return this.__listAct__(inp, this.activator)

        return inp


    def derivative(this,inp):
        if type(inp) == list:
            return this.__listAct__(inp, this.derivative)
        return 1


class Sigmoid(Activator):
    def singlesig(this,inp):
        if inp > 100:
            return 1
        if inp < -100:
            return 0
        return 1 / (1 + exp(-inp))
        

    
    def activator(this, inp):
        if type(inp) == list:
            return this.__listAct__(inp, this.activator)
        
        return this.singlesig(inp)


    def derivative(this, inp):
        if type(inp) == list:
            return this.__listAct__(inp, this.derivative)
        sso = this.singlesig(inp)
        return sso * (1 - sso)


class Rectlin(Activator):
    def activator(this, inp):
        if type(inp) == list:
            return this.__listAct__(inp, this.activator)
        
        if inp < 0:
            return 0
        return inp


    def derivative(this, inp):
        if type(inp) == list:
            return this.__listAct__(inp, this.derivative)
        return None

