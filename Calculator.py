from tkinter import *
from tkinter import ttk
from matplotlib import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

#janela principal
janela = Tk()
janela.title("Funções")
janela.geometry('600x700')

#função do primeiro

ass = Label(janela, text='A').grid(column=1, row=1)
angular_entrada = Entry(janela)
angular_entrada.grid(column=1, row=2)

bss = Label(janela, text='B').grid(column=1, row=3)
linear_entrada = Entry(janela)
linear_entrada.grid(column=1, row=4)

css = Label(janela, text='C').grid(column=1, row=5)
constante_entrada = Entry(janela)
constante_entrada.grid(column=1, row=6)

angularE = angular_entrada.get()

linearE = linear_entrada.get()

constanteE = constante_entrada.get()

listax= np.array([])
listay= np.array([])

def clicar1():
    listax= np.array([])
    listay= np.array([])
    angularE = float(angular_entrada.get())

    linearE = float(linear_entrada.get())

    for i in range(-101,101):
        listay = np.append(listay, i)
        listax = np.append(listax, angularE*i+linearE)

    figura = plt.Figure()
    grafico = figura.add_subplot(1,1,1)

    canva=FigureCanvasTkAgg(figura, janela)
    canva.get_tk_widget().grid(column=1, row=30)
    grafico.plot(listax, listay)

def clicar2():
    listax= np.array([])
    listay= np.array([])

    angularE = float(angular_entrada.get())

    linearE = float(linear_entrada.get())

    constanteE = float(constante_entrada.get())

    for i in range(-101,101):
        listay = np.append(listay, i)
        listax = np.append(listax, angularE*(i**2) + linearE*i + constanteE)

    figura = plt.Figure()
    grafico = figura.add_subplot()

    canva=FigureCanvasTkAgg(figura, janela)
    canva.get_tk_widget().grid(column=1, row=30)
    grafico.plot(listay, listax)

bot = Button(janela, text="função do primeiro grau", command=clicar1)
bot.grid(column=1, row=10)

bot = Button(janela, text="função do segundo grau", command=clicar2)
bot.grid(column=1, row=11)

def sair():
    janela.destroy()

bot = Button(janela, text="sair", command=sair)
bot.grid(column=1, row=100)

janela.mainloop()
#é isso por hoje pe-pe-pe-pe-pessoall!!!
