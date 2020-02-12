from Matrices import *
import Activators

class Net:
    dimension = [] #dimension[0] is how many inputs
    #All other cells describe how many neurons in layer
    
    layers = [] #List of matrices
    
    def __init__(this, **kwargs):
        if kwargs.get("layers"): #List of matrices
            this.layers = kwargs.get("layers")
            this.dimension.append(this.layers[0].getSize()[1] - 1)
            for i in this.layers:
                this.dimension.append(i.getSize()[0])
            
        elif kwargs.get("dat"): #list of 2d arrays to be turned into matrices
            pass
        
        elif kwargs.get("dimensions"): #list of ints
            #creates empty matrices of depth int
            this.dimension = kwargs.get("dimensions")
            for i in range(len(this.dimension) - 1):
                this.layers.append(
                    Matrix((this.dimension[i + 1], this.dimension[i] + 1)))
                
        else: #Needs some kind of init data
            raise Exception("Insuficient arguments")

        this.learningRate = kwargs.get("learningRate") or 0.2
        this.activator = kwargs.get("activator") or Activators.Linear()
                
    def getOutput(this, inp): #Dont forget bias value
        if type(inp) == list:
            inp = Matrix((len(inp), 1), inp)
        if type(inp) != Matrix:
            raise Exception("Invalid argument type")
        if inp.getSize() != (this.dimension[0] + 1, 1):
            raise Exception("Bad input size")

        for layer in this.layers:
            #print("P: "+str(inp))
            out = layer * inp
            out = out.getRaw() #Get as array
            out = this.activator.activator(out) #Apply activator
            
            inp = out.copy() #Save out for output incase last and temp use inp
            inp.insert(0, 1.0) #Add 1 at at start as bias for next
            inp = Matrix((len(inp), 1), inp) #turn into matrix and overwrite inp

        return Matrix((len(out), 1), out)

    def learn(this, inp, targetOut):
        if type(inp) == list:
            inp = Matrix((len(inp), 1), inp)
        if type(targetOut) == list:
            targetOut = Matrix((len(targetOut), 1), targetOut)
        if type(inp) != Matrix or type(targetOut) != Matrix:
            raise Exception("Invalid argument type")
        if inp.getSize() != (this.dimension[0] + 1, 1):
            raise Exception("Bad input size")
        if targetOut.getSize() != (this.dimension[-1], 1):
            raise Exception("Bad output size")

        outs = []

        for layer in this.layers:
            #print("P: "+str(inp))
            out = layer * inp
            out = out.getRaw() #Get as array
            out = this.activator.activator(out) #Apply activator

            outs.append(Matrix((len(out), 1), out))
            
            inp = out.copy() #Save out for output incase last and temp use inp
            inp.insert(0, 1.0) #Add 1 at at start as bias for next
            inp = Matrix((len(inp), 1), inp) #turn into matrix and overwrite inp

        print("To do")
        return outs




