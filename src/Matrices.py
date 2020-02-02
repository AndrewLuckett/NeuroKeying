
class Matrix:
    def __init__(this,size,dat=0):
        this.vals = []
        this.height = size[0]
        this.width = size[1]
        if len(dat) == 0:
            this.vals = [0]*this.height*this.width
        elif len(dat) == this.width:
            for i in dat:
                this.vals.extend(i)
        elif len(dat) == this.width * this.height:
            this.vals = dat.copy()
        else:
            raise Exception("Cannot read data")

    def getValue(this,pos):
        return this.vals[pos[0]*this.width + pos[1]]

    def getSize(this):
        return (this.height,this.width)

    def __mul__(this,other):
        otherSize = other.getSize()

        if this.width != otherSize[0]:
            raise Exception("Cant mult")
        
        outSize = (this.height,otherSize[1])

        out = []

        #Super slow
        for i in range(outSize[0]):
            for j in range(outSize[1]):
                cell = 0
                for k in range(this.width):
                    cell += this.getValue((i,k))*other.getValue((k,j))
                out.append(cell)
        return Matrix(outSize,out)

    def __add__(this,other):
        if this.width != otherSize[0]:
            raise Exception("Cant mult")
        
        new = []

        for(
    
    def getRaw(this):
        return this.vals

    def __repr__(this):
        out = "matrix("
        for i in range(this.height):
            t = i*this.width
            out += this.vals[t:t+this.width].__repr__()
            out += ","
            
        out = out[:-1] + ")"
        return out
