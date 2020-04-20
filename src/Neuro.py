from Matrices import *
import Activators

class Net:
    dimension = [] #dimension[0] is how many inputs
    #All other cells describe how many neurons in layer
    
    layers = [] #List of matrices
    
    def __init__(this, **kwargs):
        if kwargs.get("layers"): #List of matrices
            this.layers = kwargs.get("layers")
            #print(len(this.layers))
            this.dimension.append(this.layers[0].getSize()[1])
            for i in this.layers:
                this.dimension.append(i.getSize()[0])
        
        elif kwargs.get("dimensions"): #list of ints
            #creates empty matrices of depth int
            this.dimension = kwargs.get("dimensions")
            for i in range(len(this.dimension) - 1):
                this.layers.append(
                    Matrix((this.dimension[i + 1], this.dimension[i]),None))
                
        else: #Needs some kind of init data
            raise Exception("Insuficient arguments")

        this.biases = kwargs.get("biases") or [Matrix((i,1),[0 for j in range(i)]) for i in this.dimension[1:]]
        this.learningRate = kwargs.get("learningRate") or 0.2
        this.activator = kwargs.get("activator") or Activators.Linear()
                
    def getOutput(this, inp, measure = None): #Dont use bias in input
        if type(inp) == list:
            inp = Matrix((len(inp), 1), inp)
        if type(inp) != Matrix:
            raise Exception("Invalid argument type")
        if inp.getSize() != (this.dimension[0], 1):
            raise Exception("Bad input size")

        for layer, bias in zip(this.layers, this.biases):
            #print("P: "+str(inp))
            out = layer * inp #sum(ins * weights)
            out += bias #Add bias
            out = out.getRaw() #Get as array
            out = this.activator.activator(out) #Apply activator
            
            inp = Matrix((len(out), 1), out) #turn into matrix and overwrite inp

        if(measure):
            se = measure - inp
            se = se.getRaw()
            for i in range(len(se)):
                se[i] *= se[i]
            return inp, sum(se)
        return inp


    def learn(this, inp, targetOut):
        if type(inp) == list:
            inp = Matrix((len(inp), 1), inp)
        if type(inp) != Matrix:
            raise Exception("Invalid input type")
        if inp.getSize() != (this.dimension[0], 1):
            raise Exception("Bad input size")
        
        if type(targetOut) == list:
            targetOut = Matrix((len(targetOut), 1), targetOut)
        if type(targetOut) != Matrix:
            raise Exception("Invalid output type")
        if targetOut.getSize() != (this.dimension[-1], 1):
            raise Exception("Bad output size")

        # Do Forward pass
        outs = []
        inpDat = inp
        for layer, bias in zip(this.layers, this.biases):
            #print("P: "+str(inp))
            out = layer * inpDat #sum(ins * weights)
            out += bias #Add bias
            out = out.getRaw() #Get as array
            out = this.activator.activator(out) #Apply activator
            
            inpDat = Matrix((len(out), 1), out) #turn into matrix and overwrite inp
            outs.append(out)

        # Calculate Errors
        alldeltas = []
        first = True
        prevdelta = targetOut.getRaw()
        for i in range(len(this.layers)-1,-1,-1):
            deltas = []
            size = this.layers[i].getSize()
            
            for neuron in range(size[0]):
                error = 0
                for pdi,pd in enumerate(prevdelta):
                    if first:
                        error = pd - outs[i][neuron]
                    else:
                        error += pd * this.layers[i+1].getValue((pdi,neuron))

                error *= this.activator.derivative(outs[i][neuron])

                deltas.append(error)
                
            alldeltas.append(deltas)
            prevdelta = deltas
            first = False

        alldeltas = list(reversed(alldeltas))
        ins = [inp.getRaw()]
        ins.extend(outs)

        # Update Weights
        for i in range(len(this.layers)):
            size = this.layers[i].getSize()
            
            for n in range(size[0]):
                this.biases[i].setValue((n,0), this.biases[i].getValue((n,0)) + this.learningRate * alldeltas[i][n])
                for a in range(size[1]):
                    dw = this.learningRate * alldeltas[i][n] * ins[i][a]
                    pos = (n,a)
                    
                    this.layers[i].setValue(pos, this.layers[i].getValue(pos) + dw)
            
        return outs,alldeltas

            



