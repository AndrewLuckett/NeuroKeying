
class Matrix:
    def __init__(this, size, dat = []):
        this.vals = []
        this.height = size[0]
        this.width = size[1]
        
        if len(dat) == 0:
            this.vals = [0 for i in range(this.height * this.width)] 
        elif len(dat) == this.width * this.height:
            this.vals = dat.copy()
        elif len(dat) == this.width: #Assuming 2d
            for i in dat:
                this.vals.extend(i)
        else:
            raise Exception("Cannot read data")
        

    def scalarMult(this, val):
        if type(val) not in [int,float]:
            raise Exception("Cant mult type " + str(type(val)))
        
        out = []
        for j in this.vals:
            out.append(j * val)
        return Matrix(this.getSize(), out)


    def __mul__(this, other):
        if type(other) != Matrix:
            return this.scalarMult(other)
                
        otherSize = other.getSize()
        
        if this.width != otherSize[0]:
            raise Exception("Cant mult " + str(this.getSize()) + " with " + str(otherSize))
        
        outSize = (this.height, otherSize[1])
        out = []

        #Super slow
        for i in range(outSize[0]):
            for j in range(outSize[1]):
                cell = 0
                for k in range(this.width):
                    cell += this.getValue((i,k)) * other.getValue((k,j))
                out.append(cell)
                
        return Matrix(outSize, out)


    def __add__(this, other):
        otherSize = other.getSize()
        
        if this.getSize() != otherSize:
            raise Exception("Cant add " + str(this.getSize()) + " with " + str(otherSize))
        
        new = []
        for i,j in zip(this.vals, other.getRaw()):
            new.append(i + j)
        return Matrix(otherSize, new)


    def __sub__(this, other):
        otherSize = other.getSize()
        
        if this.getSize() != otherSize:
            raise Exception("Cant subtract " + str(this.getSize()) + " with " + str(otherSize))
        
        new = []
        for i,j in zip(this.vals, other.getRaw()):
            new.append(i - j)
        return Matrix(otherSize, new)

    
    def getRaw(this):
        return this.vals


    def getValue(this, pos):
        return this.vals[pos[0] * this.width + pos[1]]


    def getSize(this):
        return (this.height, this.width)


    def __repr__(this):
        out = "Matrix("
        for i in range(this.height):
            t = i * this.width
            out += this.vals[t: t + this.width].__repr__()
            out += ","
            
        out = out[:-1] + ")" #lazy
        return out
