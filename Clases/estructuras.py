import numpy as np
class dinamico():
    def __init__(self):
        self.espacio=1
        self.tam=0
        self.arreglo=np.empty(self.espacio,dtype=int)
    def __len__(self):
        return self.tam
    def add(self,nuevo):
        if self.tam<self.espacio:
            self.arreglo[self.tam]=nuevo
            self.tam+=1
        else:
            self.espacio*=2
            newA=np.empty(self.espacio,dtype=int)
            for i in range(self.tam):
                newA[i]=self.arreglo[i]
            newA[self.tam]=nuevo
            self.tam+=1
            self.arreglo=newA
    
    def remove_last(self):
        
        if self.tam == 0:
            return IndexError
        else:
            self.arreglo[self.tam -1]=0      
            self.tam -=1
            mien=self.espacio /2
            mien=int(mien /2)
            
            if self.espacio > self.tam *2:
                self.espacio=(self.espacio /2) +mien
                self.espacio=int(self.espacio)
                newA=np.empty(self.espacio , dtype=int)
            else:
                newA=np.empty(self.espacio , dtype=int)
                
    def remove_first(self):
        
        if self.tam == 0:
            return IndexError
            
        else:
            mien=self.espacio /2
            mien=int(mien /2)
            
            if self.espacio > self.tam *2:
                self.espacio=(self.espacio /2 )+mien
                self.espacio=int(self.espacio)
                
                print(self.espacio)
                nuevoA=np.empty(self.espacio , dtype=int)
                
            else:
                nuevoA=np.empty(self.espacio , dtype=int)
                
            
            for i in range (self.tam -1):
               nuevoA[i]=self.arreglo[i +1]
                
            nuevoA[self.tam] =0
            self.tam -=1
            self.arreglo =nuevoA  
            
    def __str__(self):
        print("Espacio: {0}\tElementos: {1}".format(self.espacio,self.tam))
        return " ".join([str(x) for x in self.arreglo[:self.tam]])
        
    def func(self):
        return "-".join([str(x) for x in self.arreglo[:self.tam]])
        
    def __getitem__(self,pos):
        if 0<=pos<self.tam:
            return self.arreglo[pos]
        else:
            raise IndexError
    