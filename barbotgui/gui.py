import tkinter
from barbotstuff import *


class BarBotApp(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self._frame = None
        self.switch_frame(MainMenu)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        print('packed new frame')


class MainMenu(tkinter.Frame, BarBotApp):
    def __init__(self, master):
        self.master = master

        tkinter.Frame.__init__(self, self.master)

        self.title_label = tkinter.Label(self, text='\nMainMenu\n')
        self.quit_button = tkinter.Button(self, text='Quit', command=self.quit)
        self.submit_button1 = tkinter.Button(self, text='Choose a cocktail',
                                             command=lambda: self.master.switch_frame(ChooseCocktail))
        self.submit_button2 = tkinter.Button(self, text='NextPage',
                                             command=lambda: self.master.switch_frame(NextPage))

        self.title_label.grid(row=0, columnspan=2)
        self.submit_button1.grid(row=4, column=0)
        self.submit_button2.grid(row=4, column=1)
        self.quit_button.grid(row=4, column=2)


class ChooseCocktail(tkinter.Frame, BarBotApp):
    def __init__(self, master):
        self.master = master
        tkinter.Frame.__init__(self, master)

        self.title_label = tkinter.Label(self, text='\nFrontPage\n')
        self.canvas = tkinter.Canvas(self, borderwidth=0)
        self.cocktail_list = tkinter.Frame(self.canvas, bg='lightblue')
        self.scrollbar = tkinter.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.title_label.pack()
        self.scrollbar.pack(side='right', fill='y')
        self.canvas.pack(side='left', fill='both', expand=True)
        self.canvas.create_window((4,4), window=self.cocktail_list,
                                  anchor='sw', tags='self.cocktail_list')

        self.cocktail_list.bind('<Configure>', self.onFrameConfigure)

        self.populate()

    def populate(self):
        cocktail_buttons = {}
        for cocktail in COCKTAILS.keys():
            cocktail_buttons[cocktail] = tkinter.Button(self.cocktail_list, text=cocktail,
                                                        command=Make(cocktail))
            print(cocktail_buttons[cocktail]['command'])
            cocktail_buttons[cocktail].configure(command=lambda: cocktail_buttons[cocktail]['command'].print_cocktail())
            cocktail_buttons[cocktail].pack(side='bottom', fill='both')
            print(cocktail_buttons[cocktail]['command'])
            print(cocktail_buttons[cocktail]['text'])

        print(cocktail_buttons)

    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))


class NextPage(tkinter.Frame, BarBotApp):
    def __init__(self, master):
        self.master = master
        tkinter.Frame.__init__(self, master)

        self.title_label = tkinter.Label(self, text='\nNextPage\n')
        self.quit_button = tkinter.Button(self, text='Quit', command=self.quit)
        self.submit_button1 = tkinter.Button(self, text='MainMenu',
                                             command=lambda: self.master.switch_frame(MainMenu))
        self.submit_button2 = tkinter.Button(self, text='FrontPage',
                                             command=lambda: self.master.switch_frame(FrontPage))

        self.title_label.grid(row=0, columnspan=2)
        self.submit_button1.grid(row=4, column=0)
        self.submit_button2.grid(row=4, column=1)
        self.quit_button.grid(row=4, column=2)


def main():
    app = BarBotApp()
    app.minsize(width=500, height=500)
    app.title('BarBotApp')
    app.mainloop()


if __name__ == '__main__':
    main()
