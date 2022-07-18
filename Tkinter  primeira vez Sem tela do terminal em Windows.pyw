from tkinter import * # importação da classe

janela = Tk() #chamdo a classe
janela.title("Programa Cálculo de Notas para Aprovação.") #titulo no topo da janela

lbSubTitulo = Label(janela, text="Caro(a) usuário(a) digite suas notas. / "
                                 "A média cálculada e >> 6 <<") # label titulo dentro da janela
lbSubTitulo.place(x=30, y=10) # possição do label na janela

def bt_click():  # função para usar as variaveis e calculos
    print("bt_click") # imporessão do comando

    av1 = float(avalF1.get())  #variaveis
    bim1 = float(bimest1.get())
    av2 = float(avalF2.get())
    bim2 = float(bimest2.get())
    lbResultado["text"] = ((av1+bim1)/2+(av2+bim2)/2)/2 # teste cálculo

    if (lbResultado["text"] < 6):  # condição apresentada no label
        lbResultado2["text"] = "Você vai ter que fazer o Exame final"
    else:
        lbResultado2["text"] = "PARABENS!!!  Você foi aprovado(a). "

avalF1 = Entry(janela) # comando para captura do que digitar na janela
avalF1.place(x=260, y=50)

lbavf1 = Label(janela, text="Digite a nota da 1º Avaliação formativa:  ") # label para informação na janela
lbavf1.place(x=30, y=50)

bimest1 = Entry(janela)
bimest1.place(x=260, y=80)

lbBimst1 = Label(janela, text="Digite a nota da 1º Avaliação Bimestral: ")
lbBimst1.place(x=30, y=80)

avalF2 = Entry(janela)
avalF2.place(x=260, y=110)

lbavf2 = Label(janela, text="Digite a nota da 2º Avaliação formativa:  ")
lbavf2.place(x=30, y=110)

bimest2 = Entry(janela)
bimest2.place(x=260, y=140)

lbBimst2 = Label(janela, text="Digite a nota da 2º Avaliação Bimestral: ")
lbBimst2.place(x=30, y=140)

bt = Button(janela, text="CALCULAR", width=15, command= bt_click) # botão com o nome e o comando nome Figurativo "bt_click"
bt.place(x=130, y= 170) # poissição do botão na janela

lbInfResul = Label(janela, text="Caro(a) Aluno(a) a sua nota é: ")
lbInfResul.place(x=30, y=210)

lbResultado = Label(janela, text="Aguardando Calculo") #label para mudar a informação na tela
lbResultado.place(x=200, y=210)

lbResultado2 = Label(janela, text=" Situação. ")
lbResultado2.place(x=30, y=240)

janela.geometry("430x320+350+200") # tamanho x,Y  e possição da janela na tela esquerda p/ direita, decima /p baixo em pixel
janela.mainloop() # para o loop da janela