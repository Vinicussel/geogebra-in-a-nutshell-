from tkinter import *
from tkinter import ttk
from matplotlib import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

#janela principal
janela = Tk()
janela.title("Funções")
janela.geometry("700x800")

Al = Label(janela, text="A da função")
mais = Label(janela, text="somar a função:")
multi = Label(janela, text="multiplicar a função por: ")
Bl = Label(janela, text="B da função")
Cl = Label(janela, text="C da função")

A  = Entry(janela)
B = Entry(janela)
C = Entry(janela)

def calculo():
    listax= np.array([])
    listay= np.array([])
    angularE = float(A.get())

    linearE = float(B.get())

    for i in range(-101,101):
        listay = np.append(listay, i)
        listax = np.append(listax, angularE*i+linearE)

    figura = plt.Figure()
    grafico = figura.add_subplot(1,1,1)

    canva=FigureCanvasTkAgg(figura, janela)
    canva.get_tk_widget().grid(column=1, row=30)
    grafico.plot(listax, listay)

def calculo2():
    listax= np.array([])
    listay= np.array([])

    angularE = float(A.get())

    linearE = float(B.get())

    constanteE = float(C.get())

    for i in range(-101,101):
        listay = np.append(listay, i)
        listax = np.append(listax, angularE*(i**2) + linearE*i + constanteE)

    figura = plt.Figure()
    grafico = figura.add_subplot()

    canva=FigureCanvasTkAgg(figura, janela)
    canva.get_tk_widget().grid(column=1, row=30)
    grafico.plot(listay, listax)

def calculo3():
    listax= np.array([])
    listay= np.array([])

    angularE = float(A.get())

    linearE = float(B.get())

    for i in range(-101,101):
        listay = np.append(listay, i)
        listax = np.append(listax,angularE**i + linearE)

    figura = plt.Figure()
    grafico = figura.add_subplot()

    canva=FigureCanvasTkAgg(figura, janela)
    canva.get_tk_widget().grid(column=1, row=30)
    grafico.plot(listay, listax)

def calculo4():
    listax= np.array([])
    listay= np.array([])

    angularE = float(A.get())

    for i in range(-101,101):
        listay = np.append(listay, i)
        listax = np.append(listax, angularE*np.log(i))

    figura = plt.Figure()
    grafico = figura.add_subplot()

    canva=FigureCanvasTkAgg(figura, janela)
    canva.get_tk_widget().grid(column=1, row=30)
    grafico.plot(listay, listax)

def calculo5():
    listax= np.array([])
    listay= np.array([])

    angularE = float(A.get())

    for i in range(-101,101):
        listay = np.append(listay, i)
        listax = np.append(listax, angularE*np.log10(i))

    figura = plt.Figure()
    grafico = figura.add_subplot()

    canva=FigureCanvasTkAgg(figura, janela)
    canva.get_tk_widget().grid(column=1, row=30)
    grafico.plot(listay, listax)

criar = Button(janela, text="Calcular", command=calculo)
criar2 = Button(janela, text="Calcular", command=calculo2)
criar3 = Button(janela, text="Calcular", command=calculo3)
criar4 = Button(janela, text="Calcular Logarítmo natural", command=calculo4)
criar5 = Button(janela, text="Calcular Logarítmo base 10", command=calculo5)

def primeiro():
    primeira.grid_forget()
    segunda.grid_forget()
    exponencial.grid_forget()
    logaritmo.grid_forget()
    Al.grid(column=1, row=1)
    A.grid(column=1, row=2)
    Bl.grid(column=1, row=3)
    B.grid(column=1, row=4)
    criar.grid(column=1, row=40)
    volta.grid(column=1, row=39)

def segundo():
    primeira.grid_forget()
    segunda.grid_forget()
    exponencial.grid_forget()
    logaritmo.grid_forget()
    Al.grid(column=1, row=1)
    A.grid(column=1, row=2)
    Bl.grid(column=1, row=3)
    B.grid(column=1, row=4)
    Cl.grid(column=1, row=5)
    C.grid(column=1, row=6)
    criar2.grid(column=1, row=40)
    volta.grid(column=1, row=39)

def exponen():
    primeira.grid_forget()
    segunda.grid_forget()
    exponencial.grid_forget()
    logaritmo.grid_forget()
    Al.grid(column=1, row=1)
    A.grid(column=1, row=2)
    mais.grid(column=1, row=3)
    B.grid(column=1, row=4)
    criar3.grid(column=1, row=40)
    volta.grid(column=1, row=39)

def loga():
    primeira.grid_forget()
    segunda.grid_forget()
    exponencial.grid_forget()
    logaritmo.grid_forget()
    multi.grid(column=1, row=1)
    A.grid(column=1, row=2)
    criar4.grid(column=1, row=40)
    volta.grid(column=1, row=43)
    criar5.grid(column=1, row=41)

def voltar():
    Al.grid_forget()
    Bl.grid_forget()
    Cl.grid_forget()
    A.grid_forget()
    B.grid_forget()
    C.grid_forget()
    criar.grid_forget()
    criar2.grid_forget()
    criar3.grid_forget()
    criar4.grid_forget()
    criar5.grid_forget()
    mais.grid_forget()
    multi.grid_forget()
    primeira.grid(column=1, row=1)
    segunda.grid(column=1, row=2)
    exponencial.grid(column=1, row=3)
    logaritmo.grid(column=1, row=4)


volta = Button(janela, text="Voltar", command=voltar)

primeira = Button(janela, text="Grau 1", command=primeiro)
primeira.grid(column=1, row=1)
segunda = Button(janela, text="Grau 2", command=segundo)
segunda.grid(column=1, row=2)
exponencial = Button(janela, text="exponencial", command=exponen)
exponencial.grid(column=1, row=3)
logaritmo = Button(janela, text="logarítmica", command=loga)
logaritmo.grid(column=1, row=4)

def sair():
    janela.destroy()

bot = Button(janela, text="sair", command=sair)
bot.grid(column=1, row=100)

janela.mainloop()