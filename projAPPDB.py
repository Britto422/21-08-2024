import tkinter
from tkinter import *
class janela:
   def __init__(self,master = None):
       self.widget1 = Frame(master)
       self.widget1.pack()

       self.msg = Label(self.widget1, text="pagina de usuario")
       self.msg["font"] = ("Verdana", "20", "italic", "bold")
       self.msg.pack()

       self.usuario = Button(self.widget1)
       self.usuario["text"] = "usuario"
       self.usuario["font"] = ("Calibri", "20")
       self.usuario["width"] = 15
       self.usuario["command"] = self.widget1.quit
       self.usuario.pack(side=LEFT)

       self.cidade = Button(self.widget1)
       self.cidade["text"] = "cidade"
       self.cidade["font"] = ("Calibri", "20")
       self.cidade["width"] = 15
       self.cidade["command"] = self.widget1.quit
       self.cidade.pack(side=LEFT)

       self.cliente = Button(self.widget1)
       self.cliente["text"] = "cliente"
       self.cliente["font"] = ("Calibri", "20")
       self.cliente["width"] = 15
       self.cliente["command"] = self.widget1.quit
       self.cliente.pack(side=LEFT)

       self.Fechar = Button(self.widget1)
       self.Fechar["text"] = "Fechar"
       self.Fechar["font"] = ("Calibri", "20")
       self.Fechar["width"] = 15
       self.Fechar["command"] = self.widget1.quit
       self.Fechar.pack(side=LEFT)

root = Tk()
janela(root)
root.mainloop()