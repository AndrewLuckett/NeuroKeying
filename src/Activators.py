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

        if inp > 1:
            return 1
        if inp < 0:
            return 0
        return inp


    def derivative(this,inp):
        if type(inp) == list:
            return this.__listAct__(inp, this.derivative)
        return None


class Sigmoid(Activator):
    def activator(this, inp):
        if type(inp) == list:
            return this.__listAct__(inp, this.activator)
        
        return 1 / (1 + exp(-inp))


    def derivative(this, inp):
        if type(inp) == list:
            return this.__listAct__(inp, this.derivative)
        return None


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

