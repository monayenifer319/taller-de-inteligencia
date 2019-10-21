#!/usr/bin/env python
# coding: utf-8

# In[211]:


from tkinter import *
from tkinter import ttk
from random import choice
from numpy import array, dot, random, exp, float
import matplotlib.pyplot as plt

#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


# In[247]:


def perceptron():
    ventanaP = Toplevel(ventana)
    ventana.iconify()
    ventanaP.title("Perceptron")
    ventanaP.geometry("900x500")
  #***************************   captura de datos   ********************************************
    sesgo=sesgoBaEntr.get()
    entrena = entrenamientoEntr.get()
    valS = valEntradaEntry.get()
    valE = valSalidaEntry.get()
    print("Datos: ",sesgo,entrena,valS,valE)
    
    activacion = lambda x:0 if x < 0 else 1
    
    #Set  Entrenamiento
    entrenamiento = [
        (array([0,0,1]),0),
        (array([0,1,1]),1),
        (array([1,0,1]),1),
        (array([1,1,1]),1)
    ]
    w = random.rand(3)
    errores = []
    esperados = []
    bahias = float(sesgo)
    n = int(entrena)
    print(bahias,n)
    
    #Entrenamiento
    for i in range(n):
        x, esperado = choice(entrenamiento)
        resultado = dot(w, x)
        esperados.append(esperado)
        error = esperado - activacion(resultado)
        errores.append(error)
        #Ajuste
        w += bahias * error * x
    
    for x, _ in entrenamiento:
        resultado = dot(w, x)
        print("{}: {} -> {}".format(x[:3], resultado, activacion(resultado)))   
        print("{}: {} -> {}".format(x[:3], resultado, activacion(resultado)))
        #print(resultado)

    graficaEr = plt.plot(errores,'-',color='red')
    graficaEs = plt.plot(esperados,'*', color='green')
    
   # mostarEr = (graficaEr)
    #mostarEr.place(x=20,y=30)
    


    


# In[284]:


#********************************  Red simple  ***********************************************************
   
  #***************************   captura de datos   ********************************************
class RedNeuronal():
    
    def __init__(self):
        self.pesos_signaticos = 2 * random.random((3,1)) - 1
        
    #funcion de activacion
    def __sigmoide(self, x):
        return 1 / (1 + exp(-x))
    
    def __sigmoide_derivado(self, x):
        return x * (1 - x)
    
    #entrenamiento
    def datas(self,sesgoBaEntr, entrenamientoEntr):
        
        self.sesgo = self.sesgoBaEntr.get()
        self.entrena = self.entrenamientoEntr.get()
       # valS = valEntradaEntry.get()
        #valE = valSalidaEntry.get()
        print("Datos: ",self.sesgo,self.entrena)
        
        
        
         #entrenamiento
    def entrenamiento(self,entradas,salidas,numero_iteraciones):
        print("hasta aqui llego")
        errores = []
        resulEsperados = []
        for i in range(numero_iteraciones):
            salida = self.pensar(entradas)
            error = salidas - salida
            ajuste = dot(entradas.T, error * self.__sigmoide_derivado(salida))
            self.pesos_signaticos += ajuste
            
            esperado = choice(salidas)  
            errores.append(error)
            resulEsperados.append(esperado)
            
        plt.plot(error,'-',color='red')
        plt.plot(resulEsperados,'*', color='green')
           # print(error)
            
    def pensar(self,entrada):
        return self.__sigmoide(dot(entrada, self.pesos_signaticos))
    
 # set de entrenamiento
if __name__ == '__main__':
    red_neuronal = RedNeuronal()
    entradas = array([[1,1,1],
                      [0,1,0], 
                      [0,1,1], 
                      [1,0,1]])
    
    salidas = array([[1,1,0,1]]).T
    
    red_neuronal.entrenamiento(entradas,salidas,500)
    
    print(red_neuronal.pesos_signaticos)
    print(red_neuronal.pensar(array([1,0,0])))
     


# In[286]:



ventana = Tk()
ventana.geometry("900x800")
ventana.title("Taller #2 IA")
#ventana.config(backgroun="black")
mainTitle = Label(text="TALLER INTELIGENCIA ARTIFICIAL", font=("",20), fg="blue")
mainTitle.place(x=250,y=30)

sesgoBaEntry =  IntVar()
entrenamientoEntry = IntVar()
valEntradaEntry = IntVar()
valSalidaEntry = IntVar()

funcionAct = Label(ventana,text="Funcion de activacion", font=(14), padx=10, pady=6).place(x=300,y=150)
sesgoBa = Label(ventana,text="Sesgo de bahias ", padx=30, font=(14), pady=6).place(x=300,y=200)
entrenamiento = Label(ventana,text="# iteraciones ", font=(14), padx=35, pady=6).place(x=300,y=250)
valEntrada = Label(ventana,text="Valores de entrada ", font=(14), padx=25, pady=6).place(x=300,y=300)
valSalida = Label(ventana,text="Valores de salida ", font=(14), padx=30, pady=6).place(x=300,y=350)

funcionActEntry = ttk.Combobox(ventana)
funcionActEntry.place(x=500,y=155)
funcionActEntry['values'] = ('Sigmoidal','TANH', 'RELU')
funcionActEntry.current(0)

 #***************************   cajas de texto  ********************************************
sesgoBaEntr = Entry(textvariable = sesgoBaEntry)
sesgoBaEntr.place(x=500,y=205)
sesgoBaEntr.place()

entrenamientoEntr = Entry(textvariable=entrenamiento)
entrenamientoEntr.place(x=500,y=260)
entrenamientoEntr.place()

valEntradaEntry = Entry(textvariable=valEntradaEntry)
valEntradaEntry.place(x=500,y=305)
valEntradaEntry.place()

valSalidaEntry = Entry(textvariable=valSalidaEntry)
valSalidaEntry.place(x=500,y=355)
valSalidaEntry.place()


 
#boton_mostrar = Button(text = "captura",command=prueba).place(x=100,y=100)



percep = Button(ventana,text="Perceptron",bg="blue", font=(14), padx=10, pady=6, command=perceptron).place(x=300,y=500)
simple = Button(ventana,text="Red simple",bg="green", font=(14), padx=10, pady=6, command=entrenamiento).place(x=450,y=500)
#multiple = Button(ventana,text="Red multiple",bg="blue", font=(14), padx=10, pady=6, command=RedMultiple).place(x=600,y=500)
cerrar = Button(ventana,text="Cerrar", bg="red", font=(14), padx=60, pady=6, command=ventana.destroy).place(x=400,y=600)
ventana.mainloop()


# In[ ]:





# In[ ]:




