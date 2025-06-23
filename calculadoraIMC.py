from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Cores
coRcinza = "#474747"
coRbranco = "#ffffff"
coRvermelho = "#9e0000"
coRamarelo = "#ffbf00"
coRamarelo2 = "#bd8e00"
coRpreto = '#000000'

def fcalcularIMC():
    altura = float(e_altura.get())
    peso = float(e_peso.get())

    imc = round(peso / (altura * altura), 2)
    caixa_resultado1.config(text=imc)

    if imc < 18.5:
        l_resultado.config(text="Abaixo do peso")
    elif 18.5 <= imc <= 24.9:
        l_resultado.config(text="Peso normal")
    elif 25 <= imc <= 29.9:
        l_resultado.config(text="Sobrepeso")
    else:
        l_resultado.config(text="Obesidade")




janela = Tk()
janela.title('Calculadora IMC')
janela.geometry('400x400')
janela.configure(bg=coRcinza)
janela.resizable(False, False)

style = ttk.Style(janela)
style.theme_use("clam")

frame_cima = Frame(janela, width=400, height=50, bg=coRpreto, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=400, height=350, bg=coRcinza, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

l_calcIMC = Label(frame_cima, text='Calculadora IMC', height=1, anchor=N, font=('Ivy 20 bold'),bg=coRpreto, fg=coRamarelo)
l_calcIMC.place(x=90, y=5)


l_linha = Label(frame_cima, text='', height=1, width=200, anchor=NE, font=('Ivy 5'), bg=coRamarelo)
l_linha.place(x=0, y=45)


l_altura = Label(frame_baixo, text="Altura (m):", height=1, anchor=NW, font=("Ivy 12 bold"),bg=coRcinza, fg=coRbranco)
l_altura.place(x=15, y=20)

e_altura = Entry(frame_baixo, width=4, justify='left', font=("", 30),highlightbackground=coRpreto, relief="solid")
e_altura.place(x=14, y=45)


l_peso = Label(frame_baixo, text="Peso (kg):", height=1, anchor=NW, font=("Ivy 12 bold"), bg=coRcinza, fg=coRbranco)
l_peso.place(x=15, y=110)

e_peso = Entry(frame_baixo, width=4, justify='left', font=("", 30),highlightbackground=coRpreto, relief="solid")
e_peso.place(x=14, y=135)


botao_res = Button(frame_baixo, text='Calcular', width=40, height=1, bg=coRcinza, fg=coRbranco, font=("Ivy 12"), relief=RAISED, overrelief=RIDGE, command=fcalcularIMC)
botao_res.place(x=14, y=235)


l_resultadot = Label(frame_baixo, text="Resultado:", height=1, anchor=NW, font=("Ivy 12 bold"), bg=coRcinza, fg=coRbranco)
l_resultadot.place(x=240, y=20)

caixa_resultado = Label(frame_baixo, text='', height=4, width=17, anchor=NW, font=('Ivy 10'), bg=coRamarelo2, highlightbackground=coRpreto, relief='solid')
caixa_resultado.place(x=240, y=45)


linha_meio = Label(frame_baixo, text='', height=100, font=('Ivy 1'), bg=coRcinza, relief=RIDGE)
linha_meio.place(x=190, y=11)


l_resultado = Label(frame_baixo, text="", height=1, anchor=NW, font=("Ivy 12 bold"),justify='center', bg=coRcinza, fg=coRpreto,highlightbackground=coRpreto, relief='solid')
l_resultado.place(x=250, y=120)


caixa_resultado1 = Label(frame_baixo, text='', height=2, width=5, anchor=NW, font=('Ivy 15'), bg=coRamarelo2)
caixa_resultado1.place(x=290, y=60)

janela.mainloop()
