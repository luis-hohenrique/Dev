from tkinter import*


class Application:
    def __init__(self, master=None):
        self.fonte1 = ("Arial"), ("13")

        self.espaço1 = Frame(master)
        self.espaço1["pady"] = 30
        self.espaço1.pack()

        self.espaço2 = Frame(master)
        self.espaço2["padx"] = 30
        self.espaço2.pack()

        self.espaço3 = Frame(master)
        self.espaço3["padx"] = 30
        self.espaço3.pack()

        self.espaço4 = Frame(master)
        self.espaço4["padx"] = 30
        self.espaço4.pack()

        self.espaço5 = Frame(master)
        self.espaço5["padx"] = 30
        self.espaço5.pack()

        self.espaço6 = Frame(master)
        self.espaço6["padx"] = 30
        self.espaço6.pack()
        
        self.espaço7 = Frame(master)
        self.espaço7["padx"] = 30
        self.espaço7.pack()

        self.titulo = Label(self.espaço1, text="Cálculo IMC - Índice de massa corporal")
        self.titulo["font"] = ("Arial", "10", "bold",)
        self.titulo.pack()

        self.digitoLabel = Label(self.espaço2, text="Nome do paciente:", font=self.fonte1,)
        self.digitoLabel.pack(fill='x')
        self.digito = Entry(self.espaço2)
        self.digito["width"] = 30
        self.digito["font"] = self.fonte1
        self.digito.pack(fill='x')

        self.digito2Label = Label(self.espaço3, text="Peso(KG):", font=self.fonte1)
        self.digito2Label.pack(fill='x')

        self.digito2 = Entry(self.espaço3)
        self.digito2["width"] = 30
        self.digito2["font"] = self.fonte1
        self.digito2.pack(fill='x')


        self.digito3Label = Label(self.espaço2, text="Endereço Completo:", font=self.fonte1)
        self.digito3Label.pack(fill='y')

        self.digito3 = Entry(self.espaço2)
        self.digito3["width"] = 30
        self.digito3["font"] = self.fonte1
        self.digito3.pack( fill='y')

        self.digito4Label = Label(self.espaço3, text="Altura(ex:1.75):", font=self.fonte1)
        self.digito4Label.pack(fill='x')

        self.digito4 = Entry(self.espaço3)
        self.digito4["width"] = 30
        self.digito4["font"] = self.fonte1
        self.digito4.pack( fill='x')

        #Resultado
        self.imcLabel = Label(self.espaço4, text="Resultado:", font=self.fonte1)
        self.imcLabel.pack(side=LEFT)

        self.imcValor = Label(self.espaço5, text="", font=self.fonte1)
        self.imcValor.pack(side=RIGHT)

        #botão
        self.calcular = Button(self.espaço6)
        self.calcular["text"] = "CALCULAR"
        self.calcular["font"] = ("Calibri", "10")
        self.calcular["width"] = 12
        self.calcular["command"] = self.calcula
        self.calcular.pack()


        

    
    def calcula(self):
        peso = self.digito2.get()
        altura = self.digito4.get()

        resp = (float(peso))/(float(altura)*float(altura))

        if peso:
            self.imcValor["text"] = round(resp,3)

root = Tk()
Application(root)
root.mainloop()