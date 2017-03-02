from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        c = self.alinhamento()
        self.msg = Label(self, text=c)
        self.msg.pack ()
        #self.bye = Button (self, text="Bye", command=self.quit)
        self.bye = Button(self, text="Bye", command=self.alinhamento)
        self.bye.pack ()
        self.pack()

    def alinhamento(self):
        concat = '{:<100}\n'.format("alinhado à esquerda, ocupando 60 posições")
        concat += '{:>100}\n'.format("alinhado à direita, ocupando 60 posições")
        concat += '{:^100}\n'.format("centralizado, ocupando 60 posições")
        concat += '{:.^100}\n'.format("cetralizado ao alterar caractere de espaçamento")
        print(concat)
        return concat
app = Application()
mainloop()


print("%d dias para copa"%(100))
print("{} dias para copa".format(100))
print("{dias} dias para copa".format(dias=100))

'''...alinhamento...'''


print(())
print(())
print(())
print(())