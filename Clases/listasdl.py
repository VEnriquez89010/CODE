from time import sleep
class nodo():
    
    def __init__(self,valor):
        self.value=valor
        self.sig=None
        self.ant=None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.sig

    def set_value(self,valor):
        self.value=valor

    def set_next(self,siguiente):
        self.sig=siguiente

    def get_last(self):
        return self.ant

    def set_last(self,anterior):
        self.ant = anterior
        
        
class listas():
    
    def __init__(self):
        self.nexto=nodo('nexto')
        self.prev=nodo('prev')
        self.nexto.set_next(self.prev)
        self.prev.set_last(self.nexto)

    def get_nexto(self):
        return self.nexto
        

    def set_nexto(self,cabecera):
        self.nexto=cabecera
        
    def __len__(self):
        cont=0
        explorer=self.nexto.sig
        while explorer is not self.prev:
            cont+=1
            explorer=explorer.sig
        return cont
        
    def add(self,valor):
        newNodo=nodo(valor)
        newNodo.sig=self.nexto.sig
        self.nexto.sig.ant=newNodo
        newNodo.ant=self.nexto
        self.nexto.sig=newNodo
     
    def remove_last(self):
        if self.prev.ant is not self.nexto:
            self.prev.ant=self.prev.ant.ant
            self.prev.ant.sig=self.prev
            
    def remove_first(self):
        if self.prev.ant is not self.nexto:
            self.nexto.sig=self.nexto.sig.sig
            self.nexto.sig.ant=self.nexto
                
    def is_empty(self):
        return self.nexto.sig is self.prev

    def __getitem__(self,pos):
        if self.__len__()<pos:
            raise IndexError
        explorer=self.nexto.sig
        for i in range(pos):
            explorer=explorer.sig
        return explorer.value
        
    def add_last(self,valor):

        newNodo=nodo(valor)
        newNodo.ant=self.prev.ant
        self.prev.ant=newNodo
        newNodo.sig=self.prev

    def to_print(self):
        aux=self.prev
        contar=0
        while aux != None:
            if contar==0:
                print (aux.ant.value)
            else:
                print(aux.value)
            #Aún imprime nexto
            if aux.value==self.nexto:
                return None
            
            aux=aux.ant
            contar +=1
            
    def get(self,elem):
        contador=0
        
        aux = self.prev
       
        while aux != None:
            
            if contador ==elem:
                print(aux.value)
                return None
                
            aux= aux.ant
            
            contador+=1
            
    def find(self,elem):
        contador=0
        
        aux = self.prev
       
        while aux != None:
            
            if aux.value ==elem:
                print("Sí existe ",elem)
                print("Posición ",contador +1)
                return None
                
            aux= aux.ant
            
            contador+=1
        print("No existe ",elem)
        
    def incluye(self,elem):
        aux = self.prev
        conta =0
        while aux != None:
            
            palabra=aux.value
            if palabra[0]==elem:
                print (palabra)
                conta+=1
            aux= aux.ant
    