## Arbol B by Alejandro Martos
class Nodo:
    def __init__(self,t):
        self.hijos=list()
        self.llaves = list()
        self.hoja=1
        self.n=0
        ## t = 2
        ## making space in the lists
        for k in range(2*t):
            self.llaves.append([None])
            print (self.llaves)
        for k in range(2*t+1):
            self.hijos.append([None])

class ArbolB:
    ## Tree constructor
    def __init__(self,gradoMinimo):
        ## grado maximo = t
        self.t=gradoMinimo
        self.raiz = None

    def bTreeCreate(self):
        if (self.raiz ==None):
            self.raiz=Nodo(self.t)
            ## initialize root node object but it's still empty
            print(self.raiz)
        return self.raiz

    def bTreeSplitShild(self,x,i):
        z=Nodo(self.t)
        print(z)
        y= x.hijos[i]
        print(y)
        z.hoja=y.hoja
        z.n=self.t-1

        for j in range(1,self.t):
            z.llaves[j]=y.llaves[j+self.t]
            print(z.llaves)
            y.llaves[j+self.t]=None

        if y.hoja == 0:
            for j in range(1,self.t+1):
                z.hijos[j]=y.hijos[j+self.t]
                y.hijos[j+self.t]=None
        y.n=self.t-1
        for j in range(x.n+1,i,-1):
            x.hijos[j+1]=x.hijos[j]
        x.hijos[i+1]=z

        for j in range(x.n,i-1,-1):
            x.llaves[j+1]=x.llaves[j]
        x.llaves[i]=y.llaves[self.t]
        y.llaves[self.t]=None
        x.n=x.n+1



    def bTreeInsertNonFull(self,x,k):
        i=x.n
        ## i is the possition of the index of keys in the node
        print(i)
        if x.hoja==1:
            while (i>=1) and  (k < x.llaves[i]):
                x.llaves[i+1] = x.llaves[i]
                i=i-1
            x.llaves[i+1]=k
            x.n=x.n+1
               # escribir a disco
        else:
            # Nodo es hoja
            while (i>=1) and (k< x.llaves[i]):
                i=i-1
            i=i+1
             #leer disco
            if x.hijos[i].n == 2*self.t-1:
                self.bTreeSplitShild(x,i)
                if k> x.llaves[i]:
                    i+i+1
            self.bTreeInsertNonFull(x.hijos[i],k)

    def bTreeInsert(self,nodo,k):
        r=self.raiz
        #nodo lleno
        if r.n == 2*self.t-1:
            s=Nodo(self.t)
            self.raiz=s
            s.hoja=0
            s.n=0
            s.hijos[1]=r
            self.bTreeSplitShild(s,1)
            self.bTreeInsertNonFull(s,k)
        else:
            self.bTreeInsertNonFull(r,k)



    def imprimeNodo(self,nodo):
        for i in range(1,2 + self.t,1):
            if (nodo.llaves[i] !=None):
                print(nodo.llaves[i])



BT = ArbolB(2)
actual=BT.bTreeCreate()
##print ("se insertara B")
###print(BT.raiz.llaves)
##BT.bTreeInsert(actual,ord("B"))
##print("Se insertara T")
##BT.bTreeInsert(actual,ord("T"))
##print("Se insertara H")
##BT.bTreeInsert(actual,ord("H"))
####print("Imprime raiz")
##print("Printing Node")
##BT.imprimeNodo(BT.raiz)
####Root node is not filled yet
##print("Se insertara M")
##BT.bTreeInsert(actual,ord("M"))
##print(BT.raiz.llaves)
##print(BT.raiz.hijos[1].llaves)
##print(BT.raiz.hijos[2].llaves)
##print("Se insertara O")
##BT.bTreeInsert(actual,ord("O"))
##print("Se insertara C")
##BT.bTreeInsert(actual,ord("C"))
##print("Se insertara P")
##BT.bTreeInsert(actual,ord("P"))
##print(BT.raiz.llaves)
##print(BT.raiz.hijos[1].llaves)
##print(BT.raiz.hijos[2].llaves)
##print(BT.raiz.hijos[3].llaves)

print ("se insertara 6")
BT.bTreeInsert(actual,6)
print ("se insertara 4")
BT.bTreeInsert(actual,4)
print ("se insertara 10")
BT.bTreeInsert(actual,10)
print ("se insertara 14")
BT.bTreeInsert(actual,14)
print ("se insertara 2")
BT.bTreeInsert(actual,2)
print ("se insertara 5")
BT.bTreeInsert(actual,5)
print ("se insertara 8")
BT.bTreeInsert(actual,8)
print ("se insertara 12")
BT.bTreeInsert(actual,12)
print ("se insertara 16")
BT.bTreeInsert(actual,16)
