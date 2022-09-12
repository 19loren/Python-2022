#bibliotecas importadas:

from tkinter import *       #tkinter - interface
import tkinter as tk
from tkinter import messagebox
from tkinter.tix import Select 


# cores
co0 = "#f0f3f5"  #preto
co1 = "#feffff"  #branco
co2 = "#63b7e1"  #azul
co3 = "#38576b"  #valor
co4 = "#403d3d"  #letra
co5 = "#a0dcfa"  #cor resultado na janela de Cálculo de IMC

# criando Primeira Janela
janela_login = Tk()
janela_login.title('IMC + Calorias')
janela_login.geometry("310x300")
janela_login.configure(background = co1)
janela_login.resizable(width = False, height = False)

# dividindo Primeira Janela
frame_cima = Frame(
    janela_login,
    width = 310, height = 50, bg = co1, relief = 'flat'
    )
frame_cima.grid(
    row = 0, column = 0, pady = 1, padx = 0, sticky = NSEW
    )

frame_baixo = Frame(
    janela_login,
    width = 310, height = 250, bg = co1, relief = 'flat'
    )
frame_baixo.grid(row = 1, column = 0, pady = 1, padx = 0, sticky = NSEW)

# configurando o frame de cima LOGIN
label_nome = Label(
    frame_cima,
    text = 'LOGIN', anchor = NE, font = ('Ivy 25'), bg = co1
    )
label_nome.place(x = 5, y = 5)

label_linha = Label(
    frame_cima,
    text = '', width = 280, height = 1, anchor = NW, font = ('Ivy 1'), bg = co2, fg = co4
    )
label_linha.place(x = 10, y = 42)

credenciais = ['', '']

def calcular_calorias_form():
    janela_calorias = Tk()
    janela_calorias.title('Formulário Calorias')
    janela_calorias.geometry("310x300")
    janela_calorias.configure(background = co1)
    janela_calorias.resizable(width = False, height = False)

    label_peso = Label(
        janela_calorias,
        text = 'Informe seu peso, em kg: ', anchor = NW, font = ('Ivy 10'), bg = co1, fg = co4
        )
    label_peso.place(x = 20, y = 7)
    entry_peso = Entry(
        janela_calorias,
        width = 7, justify ='center', font = (" ", 15), highlightthickness = 1, relief = 'solid'
        )
    entry_peso.place(x = 23, y = 27)

    label_quant_cal = Label(
        janela_calorias,
        text = 'Quantas calorias você ingeriu hoje?', anchor = NW, font = ('Ivy 10'), bg = co1, fg = co4
        )
    label_quant_cal.place(x = 20, y = 57)
    entry_quant_cal = Entry(
        janela_calorias,
        width = 7, justify ='center', font = (" ", 15), highlightthickness = 1, relief = 'solid'
        )
    entry_quant_cal.place(x = 23, y = 77)

    label_idade = Label(
        janela_calorias,
        text = 'Informe sua idade: ', anchor = NW, font = ('Ivy 10'), bg = co1, fg = co4
        )
    label_idade.place(x = 20, y = 107)
    entry_idade = Entry(
        janela_calorias,
        width = 7, justify ='center', font = (" ", 15), highlightthickness = 1, relief = 'solid'
        )
    entry_idade.place(x = 23, y = 127)
    
    label_genero = Label(
        janela_calorias,
        text = 'Informe seu gênero: ', anchor = NW, font = ('Ivy 10'), bg = co1, fg = co4
        )
    label_genero.place(x = 20, y = 157)

    entry_genero = StringVar(janela_calorias)
    entry_genero.set("F") # default value

    w = OptionMenu(janela_calorias, entry_genero, "F", "M")
    w.pack()
    w.config(width = 7)
    w.place(x = 23, y = 177)

    label_resultado_quant_cal = Label(
        janela_calorias, 
        text = ' ', width = 37, height = 1, padx = 0, pady = 12, relief = 'flat', anchor = 'center', font = ('Ivy 10 bold'), bg = co5, fg = co4
        )
    label_resultado_quant_cal.place(x = 5, y = 250)


    #Calorias ideais para as mulheres -----------------
    def calcular_calorias_ideais():
        #transformando str em float----------------
        peso = float(entry_peso.get())
        quant_cal = float(entry_quant_cal.get())
        idade = float(entry_idade.get())
        genero = entry_genero.get()

        if genero == 'F':
            if idade >= 18 and idade <= 30:
                caloriasIdeais = (0.062 * peso + 2.036) * 239
        
            elif idade >= 31 and idade <= 40:
                caloriasIdeais = (0.034 * peso + 3.538) * 239

    #Ideais para os homens--------------------------
        else:
            if idade >= 18 and idade <= 30:
                caloriasIdeais = (0.063 * peso + 2.896) * 239
        
            elif idade >= 31 and idade <= 40:
                caloriasIdeais = (0.048 * peso + 3.653) * 239

            return caloriasIdeais

        label_resultado_calorias_ideais = Label(
            janela_calorias,
            text = '---', width = 30, height = 1, padx = 6, pady = 12, relief = 'flat', anchor = 'center', font = ('Ivy 11 bold'), bg = co5, fg = co0
            )
        label_resultado_calorias_ideais.place(x = 5, y = 250)

        # label_resultado_texto_calorias_ideais = Label(
        #     janela_calorias,
        #     text = ' ', width = 37, height = 1, padx = 0, pady = 12, relief = 'flat', anchor = 'center', font = ('Ivy 10 bold'), bg = co5, fg = co4
        #     )
        # label_resultado_texto_calorias_ideais.place(x = 5, y = 250)

        # label_resultado_texto_calorias_ideais = (f"A recomendação de calorias a serem ingeridas no dia é: {caloriasIdeais:.1f} cal")
        
        #Comparação com as calorias ideais e ingeridas-----------------
        def comparacao_calorias(caloriasIdeais):
            if caloriasIdeais == quant_cal:
                 print("\n\tVocê ingeriu a quantidade ideal de calorias diárias!")
        
            elif quant_cal > caloriasIdeais:
                diferenca = quant_cal - caloriasIdeais
                print(f"\n\tVocê ingeriu {diferenca:.2f} calorias a mais do que o ideal")
        
            elif quant_cal < caloriasIdeais:
                diferenca = caloriasIdeais - quant_cal
                print(f"\n\tVocê ingeriu {diferenca:.2f} calorias a menos do que o ideal")


        label_resultado_texto_calorias_ideais = (f"A recomendação de calorias a serem ingeridas no dia é: {caloriasIdeais:.1f} cal")

    btn_calcular = Button(
        janela_calorias,
        command = calcular_calorias_ideais, text = 'Calcular', width = 36, height = 1, anchor = 'center', font = ('Ivy 10 bold'), bg = co2, fg = co1,
        overrelief = RIDGE, relief = RAISED
        )
    btn_calcular.place(x = 5, y = 217)

    janela_calorias.mainloop()


def verifica_senha():
    nome = entry_nome.get()
    senha = entry_pass.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo admin')
        Formulario()
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo, ' + credenciais[0])
        Formulario()
    else:
        messagebox.showwarning('Error', 'Verifique o nome e a senha!')


def nova_janela():
    #configurando frame cima
    label_nome = Label(
        frame_cima,
        text = 'Usuario: ' + credenciais[0]
        )
    label_nome.place(x = 5, y = 5)

    label_linha = Label(
        frame_cima,
        text = '', width = 280, anchor = NW, font = ('Ivy 1'), bg = co2, fg = co4
        )
    label_linha.place(x=10, y=5)

    label_nome = Label(
        frame_baixo,
        text = 'Seja bem vindo' + credenciais[0], archor = NE, font = ('Ivy 20'), bg = co1, fg = co4
    )
    label_nome.place(x = 5, y = 105)


# configurando frame de baixo
label_nome = Label(
    frame_baixo,
    text = 'Usuário:', anchor = NW, font = ('Ivy 10'), bg = co1, fg = co4
    )
label_nome.place(x = 10, y = 10)
entry_nome = Entry(
    frame_baixo,
    width = 25, justify = 'left', font = (" ", 15), highlightthickness = 1, relief = 'solid'
    )
entry_nome.place(x = 14, y = 40)

label_pass = Label(
    frame_baixo,
    text = 'Palavra chave: ', anchor = NW, font = ('Ivy 10'), bg = co1, fg = co4
    )
label_pass.place(x = 10, y = 75)
entry_pass = Entry(
    frame_baixo,
    width = 25, justify = 'left', font = (" ", 15), highlightthickness = 1, relief = 'solid', show = '*'
    )
entry_pass.place(x = 14, y = 100)

def Calcular_IMC():
  janela_IMC = tk.Toplevel()
  janela_IMC.title('Formulário IMC')
  janela_IMC.geometry("310x238")
  janela_IMC.configure(background = co1)
  janela_IMC.resizable(width = False, height = False)
  
  label_peso = Label(
      janela_IMC,
      text = 'Informe seu peso, em kg: ', anchor = NW, font = ('Ivy 10'), bg = co1, fg = co4
      )
  label_peso.place(x = 20, y = 7)
  entry_peso = Entry(
      janela_IMC,
      width = 7, justify ='center', font = (" ", 15), highlightthickness = 1, relief = 'solid'
      )
  entry_peso.place(x = 23, y = 27)

  label_altura = Label(
      janela_IMC,
      text = 'Informe sua altura, em metros: ', anchor = NW, font = ('Ivy 10'), bg = co1, fg = co4
      )
  label_altura.place(x = 20, y = 57)
  entry_altura = Entry(
      janela_IMC,
      width = 7, justify = 'center', font = (" ", 15), highlightthickness = 1, relief = 'solid'
      )
  entry_altura.place(x = 23, y = 77)
    
  label_resultado = Label(
      janela_IMC,
      text = '---', width = 32, height = 1, padx = 0, pady = 12, relief = 'flat', anchor = 'center', font = ('Ivy 11 bold'), bg = co5, fg = co0
      )
  label_resultado.place(x = 8, y = 148)

  label_resultado_texto = Label(
      janela_IMC,
      text = 'O seu IMC é: ', 
    width = 36, height = 1, padx = 0, pady = 12, relief = 'flat', anchor = 'center', font = ('Ivy 10 bold'), bg = co5, fg = co4
      )
  label_resultado_texto.place(x = 8, y = 187)
  def calcular():
    peso = float(entry_peso.get())
    altura = float(entry_altura.get())
    imc = peso / altura **2

    if imc < 18.5:
      label_resultado_texto['text'] = ('Seu IMC é: Abaixo do peso')

    elif imc >= 18.5 and imc < 25:
      label_resultado_texto['text'] = ('Seu IMC é: Normal')
    elif imc >= 25 and imc < 30:
      label_resultado_texto['text'] = ("Seu IMC é: Sobrepeso")
    else:
      label_resultado_texto['text'] = ("Seu IMC é: Obesidade")
  

    label_resultado['text'] = "{:.{}f}".format(imc, 2)
                               
    btn_confirmar = Button(
      janela_IMC,
        text = 'resultado IMC:', width = 39, height = 2, font = ('Ivy 8 bold'), bg = co2, fg = co1, 
        relief = RAISED, overrelief = RIDGE
        ) 
  btn_calcular = Button(
      janela_IMC,
      command = calcular, text = 'Calcular', width = 36, height = 1, anchor = 'center', font = ('Ivy 10 bold'), bg = co2, fg = co1,
      overrelief = RIDGE, relief = RAISED,
      )
  btn_calcular.place(x = 5, y = 117)

      
  #funcao calculos calorias -----------------------------------------------
  btn_confirmar.place(x = 13, y = 150)

  
def calcular_calorias():
  janela_calorias = tk.Toplevel()
  janela_calorias.title('Formulário Calorias')
  janela_calorias.geometry("310x300")
  janela_calorias.configure(background = co1)
  janela_calorias.resizable(width = False, height = False)



def Formulario():
    janela_menu = tk.Toplevel()
    janela_menu.title('IMC + Calorias')
    janela_menu.geometry("310x177")
    janela_menu.configure(background = co1)
    janela_menu.resizable(width = False, height = False)
    
    label_nome3 = Label(
        janela_menu,
        text = 'MENU', anchor = NE, font = ('Ivy 25'), bg = co1
        )
    label_nome3.place(x = 5, y = 5)

    label_linha3 = Label(
        janela_menu,
        text = '', width = 280, height = 1, anchor = NW, font = ('Ivy 1'), bg = co2, fg = co4
        )
    label_linha3.place(x = 10, y = 42)

    btn_confirmar = Button(
        janela_menu,
        command = Calcular_IMC, text = 'Calcular IMC', width = 39, height = 2, font = ('Ivy 8 bold'), bg = co2, fg = co1, 
        relief = RAISED, overrelief = RIDGE
        )
    btn_confirmar.place(x = 11, y = 80)
    btn_confirmar = Button(
        janela_menu,
        command = calcular_calorias_form, text = 'Calcular Calorias', width = 39, height = 2, font = ('Ivy 8 bold'), bg = co2, fg = co1, 
        relief = RAISED, overrelief = RIDGE
        )
    btn_confirmar.place(x = 11, y = 120)

btn_confirmar2 = Button(
    frame_baixo,
    command = verifica_senha, text = 'Entrar', width = 39, height = 2, font = ('Ivy 8 bold'), bg = co2, fg = co1,
    relief = RAISED, overrelief = RIDGE
    )
btn_confirmar2.place(x = 11, y = 150)

 
# janela de cadastramento

def abrir_janelacadastramento():
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title('Cadastro')
    janela_cadastro.geometry("310x500")
    janela_cadastro.configure(background = co1)
    janela_cadastro.resizable(width = False,height = False)

    # frame cima
    label_nome = Label(
        janela_cadastro,
        text = 'CADASTRO', anchor = NE, font = ('Ivy 19') 
        )
    label_nome.place(x = 5, y = 5)

    label_linha = Label(
        janela_cadastro,
        text = '', width = 275, anchor = NW, font = ('Ivy 1'), bg = co2, fg = co4
        )
    label_linha.place(x = 10, y = 45)

    # frame de baixo
    label_nome = Label(
        janela_cadastro,
        text = 'Digite seu Nome: ', anchor = NW, font = ('Ivy 10'), bg = co1, fg = co4
        )
    label_nome.place(x = 10, y = 55)
    entry_nome_cadastro = Entry(
        janela_cadastro, 
        width = 25, justify = 'left', font = (" ", 15), highlightthickness = 1, relief = 'solid' 
        )
    entry_nome_cadastro.place(x = 13, y = 82)

    label_idade = Label(
        janela_cadastro,
        text = 'Idade: ', anchor = NW, font = ('Ivy 10'), bg = co1, fg = co4 
        )
    label_idade.place(x = 10, y = 120)
    entry_idade = Entry(
        janela_cadastro,
        width = 3, justify = 'left', font = (" ", 15), highlightthickness = 1, relief = 'solid'
        )
    entry_idade.place(x = 13, y = 142)

    label_Email = Label(
        janela_cadastro,
        text = 'E-mail:', anchor = NW, font = ('Ivy 10'), bg = co1, fg = co4
        )
    label_Email.place(x = 10, y = 178)
    entry_Email = Entry(
        janela_cadastro,
        width = 25, justify = 'left', font = (" ", 15), highlightthickness = 1, relief = 'solid'
        )
    entry_Email.place(x = 14, y = 200)


    label_CPF = Label(
        janela_cadastro,
        text = 'CPF: ', anchor = NW, font = ('Ivy 10'), bg = co1, fg = co4
        )
    label_CPF.place(x = 10, y = 235)
    entry_CPF = Entry(
        janela_cadastro,
        width = 25, justify = 'left', font = (" ", 15), highlightthickness = 1, relief = 'solid'
        )
    entry_CPF.place(x = 14, y = 255)

    label_telefone = Label(
        janela_cadastro,
        text = 'Telefone: ', anchor = NW, font = ('Ivy 10'), bg = co1, fg = co4
        )
    label_telefone.place(x = 10, y = 290)
    entry_telefone = Entry(
        janela_cadastro, 
        width = 25, justify = 'left', font = (" ", 15), highlightthickness = 1, relief = 'solid'
        )
    entry_telefone.place(x = 14, y = 310)

    label_genero = Label(
        janela_cadastro,text = 'Gênero: ', anchor = NW, font = ('Ivy 10'), bg = co1, fg = co4 
        )
    label_genero.place(x = 10, y = 350)
    entry_genero = Entry(
        janela_cadastro,
        width = 25, justify = 'left', font = (" ", 15), highlightthickness = 1, relief = 'solid'
        )
    entry_genero.place(x = 14, y = 370)
    btn_confirmar = Button(
        janela_cadastro,
        command = lambda: cadastrar_cliente(
            entry_nome_cadastro, entry_idade, entry_CPF, entry_Email, entry_telefone, entry_genero
            ),
        text = 'Criar cadastro', width = 39, height = 2, font = ('Ivy 8 bold'), bg = co2, fg = co1, 
        relief = RAISED, overrelief = RIDGE
        )
    btn_confirmar.place(x=14, y=410)

    btn_confirmar = Button(
        janela_cadastro,
        command = janela_cadastro.destroy, text = 'Voltar ao login', width = 39, height = 2, font = ('Ivy 8 bold'), bg = co2, fg = co1,
        relief = RAISED, overrelief = RIDGE
        )	 
    btn_confirmar.place(x=14, y=450)


def cadastrar_cliente(entry_nome_cadastro, entry_CPF, entry_idade, entry_Email, entry_telefone, entry_genero):
    conn = cx_Oracle.connect('username/password@//hostname:porta/sid')
    cur = conn.cursor()
    sql_insert = "insert into IMC values(:NOME, :CPF, :IDADE, :EMAIL, :TELEFONE, :GENERO)"
    cur.execute(
        sql_insert,
        [entry_nome_cadastro.get(),
        int(entry_CPF.get()),
        int(entry_idade.get()), entry_Email.get(), int(entry_telefone.get()), entry_genero.get()])
    conn.commit()
    conn.close()


btn_confirmar = Button(
    frame_baixo,
    command = abrir_janelacadastramento, text = 'Cadastre-se', width = 39, height = 2, font = ('Ivy 8 bold'), bg = co2, fg = co1, 
    relief = RAISED, overrelief = RIDGE
    )
btn_confirmar.place(x = 11, y = 190)

janela_login.mainloop()