# from time import sleep
class nodo():
    
    def __init__(self,valor):
        self.value=valor
        self.next=None
    
    def get_value(self):
        return self.value
        
    def get_next(self):
        return self.next
    
    def set_value(self,valor):
        self.value=valor
        
    def set_next(self,siguiente):
        self.next=siguiente
        
class lista():
    
    def __init__(self):
        self.head=None
    
    def get_head(self):
        return self.head
        
    def set_head(self,cabeza):
        self.head= cabeza
        
    def add(self,valor):
        eslabon=nodo(valor)
        #sleep(.01)
        eslabon.set_next(self.head)
        self.set_head(eslabon)
        
    def is_empty(self):
        return self.head ==None
        
    def __len__(self):
        contador=0
        explorador=self.head
        while explorador!=None:
            contador+=1
            explorador=explorador.next
        return contador
        
    def __getitem__(self,pos):
        if self.__len__()<pos:
            raise IndexError
        explorador=self.head
        for i in range(pos):
            explorador=explorador.next
        return explorador.value
        
    def add_last(self,valor):
        eslabon=nodo(valor)
        explorador=self.head
        if explorador==None:
            self.head=eslabon
        else:
            while explorador.next !=None:
                #sleep(.01)
                explorador=explorador.next
            explorador.next=eslabon
    
    def del_last(self):
        explorador=self.head
        explorer=explorador
        
        while explorador.next != None:
            explorer = explorador
            explorador= explorador.next
            
        explorer.next=None
        
            
    def to_print(self,pos):
        print ("-----")
        aux = self.head
        conta=0
        
        if pos==1:
            print(aux.get_value())
        else:
            for i in range(pos-1):
                
                aux=aux.next
            
        if aux != None:
                print(aux.get_value())
                
    def to_printo(self):
        aux = self.head
        contador1=0
        frase=""
        
        while aux != None:
            frase=frase+"+"+aux.value
            aux= aux.next
            contador1 +=1
            
        return frase

       
       
            
    def find(self,elem):
        contador=0
        
        aux = self.head
       
        while aux != None:
            
            if aux.value ==elem:
                print("Sí existe ",elem)
                print("Posición ",contador +1)
                return None
                
            aux= aux.next
            
            contador+=1
        print("No existe ",elem)

        