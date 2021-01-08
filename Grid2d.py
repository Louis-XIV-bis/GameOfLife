import numpy as np
class Grid2d():
    """Class for manipulate 2D grid"""
    def __init__(self,xdim=10,ydim=10):
        self.xdim=xdim
        self.ydim=ydim
        self.tab = [[0]*self.ydim for x in range(self.xdim)]
    
    def get_dim(self):
        """Return the two dimensions of the grid"""
        return self.xdim,self.ydim
    
    def get_value_at(self,i,j):
        res = -1
        if 0 <= i <self.xdim and 0 < j < self.ydim :
            res=self.tab[i][j]
        else:
            res=-1
        return res
    
    def set_value_at(self,i,j,value):
        res=0
        try:
            self.tab[i][j]=value
        except IndexError:
            res=-1
        return res
    
    def get_neighs_values(self,i,j):
        """Return a list of all neighbours values (i,j include)"""
        res=[]
        if 0 <= i <self.xdim and 0 < j < self.ydim :
            for ineigh in [-1,0,1]:
                if 0 <= i + ineigh <self.xdim :
                    for jneigh in [-1,0,1] :
                        if 0 <= j + jneigh < self.ydim :
                            res.append(self.tab[i+ineigh][j+jneigh])
        return res
    
    def debug(self):
        for i in range(self.xdim):
            print(self.tab[i])

    def generate(self):
        for i in range(self.xdim):
            for j in range(self.ydim) :
                self.set_value_at(i,j,np.random.randint(2))
