from Matrices import *


class Net:
    dimension = [] #dimension[0] is how many inputs
    #All other cells describe how many neurons in layer
    layers = [] #List of matrices
    learningRate = 0.2
    
    def __init__(this, **kwargs):
        #print(kwargs)
        if kwargs.get("layers"): #matrices
            this.layers = kwargs.get("layers")
            for i in this.layers:
                this.dimension.append(i.getSize()[0] - 1)
            this.dimension.append(this.layers[-1].getSize()[1])
        elif kwargs.get("dat"):
            pass #list of 2d arrays to be turned into matrices
        elif kwargs.get("dimensions"):
            this.dimension = kwargs.get("dimensions")
            for i in range(len(this.dimension)-1):
                this.layers.append(
                    Matrix((this.dimension[i+1],this.dimension[i]+1)))
        else:
            raise Exception("Insuficient arguments")

        if kwargs.get("learningRate"):
            this.learningRate = kwargs.get("learningRate")
                
    def getOutput(this,inp):
        if type(inp) == list:
            inp = Matrix((len(inp),1),inp)
        if type(inp) == Matrix and inp.getSize() != (this.dimension[0]+1,1):
            print("Bad input size")
            return

        for layer in this.layers:
            #print("P: "+str(inp))
            out = layer * inp
            
            out = out.getRaw()
            out.insert(0,1.0)
            inp = Matrix((len(out),1),out)

        return inp

    def learn(this,inp,out):

        return True
