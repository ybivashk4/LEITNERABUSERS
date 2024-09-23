import tkinter as tk
from PIL import Image, ImageTk

__all__ = ['ScrolledText']


class ScrolledText(tk.Text):
    def __init__(self, master=None, **kw):
        self.frame = tk.Frame(master)
        self.vbar = tk.Scrollbar(self.frame)
        self.vbar.pack(side=tk.RIGHT, fill=tk.Y)

        kw.update({'yscrollcommand': self.vbar.set})
        tk.Text.__init__(self, self.frame, **kw)
        self.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.vbar['command'] = self.yview

        # Copy geometry methods of self.frame without overriding Text
        # methods -- hack!
        text_meths = vars(tk.Text).keys()
        methods = vars(tk.Pack).keys() | vars(tk.Grid).keys() | vars(tk.Place).keys()
        methods = methods.difference(text_meths)

        for m in methods:
            if m[0] != '_' and m != 'config' and m != 'configure':
                setattr(self, m, getattr(self.frame, m))

    def __str__(self):
        return str(self.frame)

root = tk.Tk()

root.title("coreset")

header = tk.Frame(root)
main = tk.Frame(root)
footer = tk.Frame(root, relief="solid", highlightthickness = 2, 
                  highlightbackground = "#8B6CFE", highlightcolor = "#8B6CFE")
flag_mouse = 0
flag_theme = 0
que_answ = [{i: "" for i in range(1, 6)} for _ in range(5)] # вопрос и ответы разделены ?corset?
def mouse(event):
    global flag_mouse
    if (flag_mouse):
        event.widget["bg"] = "#d3d3d3"
        event.widget["fg"] = "#000000"
    else:
        event.widget["bg"] = "#8B6CFE"
        event.widget["fg"] = "#FFFFFF"
    flag_mouse = (flag_mouse + 1) % 2
        
def add_func(event):
    
    editor = tk.Toplevel(root)
    editor.title("editor")
    editor.geometry('250x470')# Размеры всего приложения
    editor.resizable(width=False, height=False)# Запрет на изменение размеров
    
    name_theme = tk.Frame(editor)
    questions = tk.Frame(editor)
    save_and_exit = tk.Frame(editor)
    lab_name = tk.Label(name_theme, width=100, text="Введите название темы")
    entr_name = tk.Entry(name_theme, width = 100)
    
    lab_que = tk.Label(questions, width=100, text="Ввеидте 6 вопросов/ответов")
    
    frame_que1 = tk.Frame(questions)
    entr_que1 = tk.Entry(frame_que1, width = 15)
    entr_answ1 = tk.Entry(frame_que1, width = 15)
    
    frame_que2 = tk.Frame(questions)
    entr_que2 = tk.Entry(frame_que2, width = 15)
    entr_answ2 = tk.Entry(frame_que2, width = 15)
    
    frame_que3 = tk.Frame(questions)
    entr_que3 = tk.Entry(frame_que3, width = 15)
    entr_answ3 = tk.Entry(frame_que3, width = 15)
    
    frame_que4 = tk.Frame(questions)
    entr_que4 = tk.Entry(frame_que4, width = 15)
    entr_answ4 = tk.Entry(frame_que4, width = 15)
    
    frame_que5 = tk.Frame(questions)
    entr_que5 = tk.Entry(frame_que5, width = 15)
    entr_answ5 = tk.Entry(frame_que5, width = 15)
    
    frame_que6 = tk.Frame(questions)
    entr_que6 = tk.Entry(frame_que6, width = 15)
    entr_answ6 = tk.Entry(frame_que6, width = 15)
    
    def save_func():
        global flag_theme
        
        flag_theme += 1
        name = entr_name.get()
        if (flag_theme == 1):
            theme1["borderwidth"] = 2
            theme1["text"] = name
            que_answ[0][1] = entr_que1.get() + "?corset?" + entr_answ1.get()
            que_answ[0][2] = entr_que2.get() + "?corset?" + entr_answ2.get()
            que_answ[0][3] = entr_que3.get() + "?corset?" + entr_answ3.get()
            que_answ[0][4] = entr_que4.get() + "?corset?" + entr_answ4.get()
            que_answ[0][5] = entr_que5.get() + "?corset?" + entr_answ5.get()
            que_answ[0][6] = entr_que5.get() + "?corset?" + entr_answ5.get()
        if (flag_theme == 2):
            theme2["borderwidth"] = 2
            theme2["text"] = name
            que_answ[1][1] = entr_que1.get() + "?corset?" + entr_answ1.get()
            que_answ[1][2] = entr_que2.get() + "?corset?" + entr_answ2.get()
            que_answ[1][3] = entr_que3.get() + "?corset?" + entr_answ3.get()
            que_answ[1][4] = entr_que4.get() + "?corset?" + entr_answ4.get()
            que_answ[1][5] = entr_que5.get() + "?corset?" + entr_answ5.get()
            que_answ[1][6] = entr_que5.get() + "?corset?" + entr_answ5.get()
        if (flag_theme == 3):
            theme3["borderwidth"] = 2
            theme3["text"] = name
            que_answ[2][1] = entr_que1.get() + "?corset?" + entr_answ1.get()
            que_answ[2][2] = entr_que2.get() + "?corset?" + entr_answ2.get()
            que_answ[2][3] = entr_que3.get() + "?corset?" + entr_answ3.get()
            que_answ[2][4] = entr_que4.get() + "?corset?" + entr_answ4.get()
            que_answ[2][5] = entr_que5.get() + "?corset?" + entr_answ5.get()
            que_answ[2][6] = entr_que5.get() + "?corset?" + entr_answ5.get()
        if (flag_theme == 4):
            theme4["borderwidth"] = 2
            theme4["text"] = name
            que_answ[3][1] = entr_que1.get() + "?corset?" + entr_answ1.get()
            que_answ[3][2] = entr_que2.get() + "?corset?" + entr_answ2.get()
            que_answ[3][3] = entr_que3.get() + "?corset?" + entr_answ3.get()
            que_answ[3][4] = entr_que4.get() + "?corset?" + entr_answ4.get()
            que_answ[3][5] = entr_que5.get() + "?corset?" + entr_answ5.get()
            que_answ[3][6] = entr_que5.get() + "?corset?" + entr_answ5.get()
        if (flag_theme == 5):
            theme5["borderwidth"] = 2
            theme5["text"] = name
            que_answ[4][1] = entr_que1.get() + "?corset?" + entr_answ1.get()
            que_answ[4][2] = entr_que2.get() + "?corset?" + entr_answ2.get()
            que_answ[4][3] = entr_que3.get() + "?corset?" + entr_answ3.get()
            que_answ[4][4] = entr_que4.get() + "?corset?" + entr_answ4.get()
            que_answ[4][5] = entr_que5.get() + "?corset?" + entr_answ5.get()
            que_answ[4][6] = entr_que5.get() + "?corset?" + entr_answ5.get()
        
    save_and_exit_but = tk.Button(save_and_exit, bg="#8B6CFE", fg="#FFFFFF", width=100, height=3, text="Сохранить и выйти", command=save_func)
    
    name_theme.pack(pady=10)
    questions.pack(pady=10)
    save_and_exit.pack(pady=10)
    lab_name.pack(side=tk.TOP, padx=7)
    entr_name.pack(side=tk.TOP, padx=7)
    
    lab_que.pack(side=tk.TOP, padx=5, pady=5)
    
    frame_que1.pack(side=tk.TOP, padx=5, pady=5)    
    frame_que2.pack(side=tk.TOP, padx=5, pady=5)
    frame_que3.pack(side=tk.TOP, padx=5, pady=5)
    frame_que4.pack(side=tk.TOP, padx=5, pady=5)
    frame_que5.pack(side=tk.TOP, padx=5, pady=5)
    frame_que6.pack(side=tk.TOP, padx=5, pady=5)
    
    entr_que1.pack(side=tk.LEFT, padx=10, pady=2)
    entr_answ1.pack(side=tk.LEFT, padx=10, pady=2)
    
    entr_que2.pack(side=tk.LEFT, padx=10, pady=2)
    entr_answ2.pack(side=tk.LEFT, padx=10, pady=2)
    
    entr_que3.pack(side=tk.LEFT, padx=10, pady=2)
    entr_answ3.pack(side=tk.LEFT, padx=10, pady=2)
    
    entr_que4.pack(side=tk.LEFT, padx=10, pady=2)
    entr_answ4.pack(side=tk.LEFT, padx=10, pady=2)
    
    entr_que5.pack(side=tk.LEFT, padx=10, pady=2)
    entr_answ5.pack(side=tk.LEFT, padx=10, pady=2)
    
    entr_que6.pack(side=tk.LEFT, padx=10, pady=2)
    entr_answ6.pack(side=tk.LEFT, padx=10, pady=2)
    
    
    save_and_exit_but.pack(side=tk.LEFT, padx=5, pady=5)
    

def theme_func1(event):
    if "?corset?" in que_answ[0][1]:
        theme1 = tk.Toplevel(root)
        theme1.title("просмоторщик")
        theme1.geometry('500x360')# Размеры всего приложения
        frame = tk.Frame(theme1)
        labQ = tk.Label(frame, text="Вопрос:")
        labA = tk.Label(frame, text="Ответ:")
        
        frame.pack(side=tk.TOP, pady=5, padx=5)
        labQ.pack(side=tk.LEFT, padx=20)
        labA.pack(side=tk.LEFT, padx=20)
        for i in range(1, 7):
            if "?corset?" in que_answ[0][i]:
                q_n_a = tk.Frame(theme1)
                answer = tk.Frame(q_n_a)
                question = tk.Frame(q_n_a)
                
                stext_q = ScrolledText(master=question, width=30, height=5)
                stext_q.insert(tk.END, que_answ[0][i].split("?corset?")[1])
                
                stext_a = ScrolledText(master=answer, width=30, height=5)
                stext_a.insert(tk.END, que_answ[0][i].split("?corset?")[0])
                
                q_n_a.pack(side=tk.TOP, padx=5)
                answer.pack(side=tk.LEFT, padx=5)
                question.pack(side=tk.LEFT, padx=5)
                stext_q.pack(side=tk.LEFT, padx=5)
                stext_a.pack(side=tk.LEFT, padx=5)
        
def theme_func2(event):
    if "?corset?" in que_answ[0][1]:
        theme2 = tk.Toplevel(root)
        theme2.title("просмоторщик")
        theme2.geometry('500x360')# Размеры всего приложения
        frame = tk.Frame(theme2)
        labQ = tk.Label(frame, text="Вопрос:")
        labA = tk.Label(frame, text="Ответ:")
        
        frame.pack(side=tk.TOP, pady=5, padx=5)
        labQ.pack(side=tk.LEFT, padx=20)
        labA.pack(side=tk.LEFT, padx=20)
        for i in range(1, 7):
            if "?corset?" in que_answ[0][i]:
                q_n_a = tk.Frame(theme2)
                answer = tk.Frame(q_n_a)
                question = tk.Frame(q_n_a)
                
                stext_q = ScrolledText(master=question, width=30, height=5)
                stext_q.insert(tk.END, que_answ[0][i].split("?corset?")[1])
                
                stext_a = ScrolledText(master=answer, width=30, height=5)
                stext_a.insert(tk.END, que_answ[0][i].split("?corset?")[0])
                
                q_n_a.pack(side=tk.TOP, padx=5)
                answer.pack(side=tk.LEFT, padx=5)
                question.pack(side=tk.LEFT, padx=5)
                stext_q.pack(side=tk.LEFT, padx=5)
                stext_a.pack(side=tk.LEFT, padx=5)

def theme_func3(event):
    if "?corset?" in que_answ[0][1]:
        theme3 = tk.Toplevel(root)
        theme3.title("просмоторщик")
        theme3.geometry('500x360')# Размеры всего приложения
        frame = tk.Frame(theme3)
        labQ = tk.Label(frame, text="Вопрос:")
        labA = tk.Label(frame, text="Ответ:")
        
        frame.pack(side=tk.TOP, pady=5, padx=5)
        labQ.pack(side=tk.LEFT, padx=20)
        labA.pack(side=tk.LEFT, padx=20)
        for i in range(1, 7):
            if "?corset?" in que_answ[0][i]:
                q_n_a = tk.Frame(theme3)
                answer = tk.Frame(q_n_a)
                question = tk.Frame(q_n_a)
                
                stext_q = ScrolledText(master=question, width=30, height=5)
                stext_q.insert(tk.END, que_answ[0][i].split("?corset?")[1])
                
                stext_a = ScrolledText(master=answer, width=30, height=5)
                stext_a.insert(tk.END, que_answ[0][i].split("?corset?")[0])
                
                q_n_a.pack(side=tk.TOP, padx=5)
                answer.pack(side=tk.LEFT, padx=5)
                question.pack(side=tk.LEFT, padx=5)
                stext_q.pack(side=tk.LEFT, padx=5)
                stext_a.pack(side=tk.LEFT, padx=5)

def theme_func4(event):
    if "?corset?" in que_answ[0][1]:
        theme4 = tk.Toplevel(root)
        theme4.title("просмоторщик")
        theme4.geometry('500x360')# Размеры всего приложения
        frame = tk.Frame(theme4)
        labQ = tk.Label(frame, text="Вопрос:")
        labA = tk.Label(frame, text="Ответ:")
        
        frame.pack(side=tk.TOP, pady=5, padx=5)
        labQ.pack(side=tk.LEFT, padx=20)
        labA.pack(side=tk.LEFT, padx=20)
        for i in range(1, 7):
            if "?corset?" in que_answ[0][i]:
                q_n_a = tk.Frame(theme4)
                answer = tk.Frame(q_n_a)
                question = tk.Frame(q_n_a)
                
                stext_q = ScrolledText(master=question, width=30, height=5)
                stext_q.insert(tk.END, que_answ[0][i].split("?corset?")[1])
                
                stext_a = ScrolledText(master=answer, width=30, height=5)
                stext_a.insert(tk.END, que_answ[0][i].split("?corset?")[0])
                
                q_n_a.pack(side=tk.TOP, padx=5)
                answer.pack(side=tk.LEFT, padx=5)
                question.pack(side=tk.LEFT, padx=5)
                stext_q.pack(side=tk.LEFT, padx=5)
                stext_a.pack(side=tk.LEFT, padx=5) 

def theme_func5(event):
    if "?corset?" in que_answ[0][1]:
        theme5 = tk.Toplevel(root)
        theme5.title("просмоторщик")
        theme5.geometry('500x360')# Размеры всего приложения
        frame = tk.Frame(theme5)
        labQ = tk.Label(frame, text="Вопрос:")
        labA = tk.Label(frame, text="Ответ:")
        
        frame.pack(side=tk.TOP, pady=5, padx=5)
        labQ.pack(side=tk.LEFT, padx=20)
        labA.pack(side=tk.LEFT, padx=20)
        for i in range(1, 7):
            if "?corset?" in que_answ[0][i]:
                q_n_a = tk.Frame(theme5)
                answer = tk.Frame(q_n_a)
                question = tk.Frame(q_n_a)
                
                stext_q = ScrolledText(master=question, width=30, height=5)
                stext_q.insert(tk.END, que_answ[0][i].split("?corset?")[1])
                
                stext_a = ScrolledText(master=answer, width=30, height=5)
                stext_a.insert(tk.END, que_answ[0][i].split("?corset?")[0])
                
                q_n_a.pack(side=tk.TOP, padx=5)
                answer.pack(side=tk.LEFT, padx=5)
                question.pack(side=tk.LEFT, padx=5)
                stext_q.pack(side=tk.LEFT, padx=5)
                stext_a.pack(side=tk.LEFT, padx=5)

plus = ImageTk.PhotoImage(Image.open("files/plus.png"))
cards_img = ImageTk.PhotoImage(Image.open("files/cards.png"))
learn_img = ImageTk.PhotoImage(Image.open("files/learn.png"))
pribil_img = ImageTk.PhotoImage(Image.open("files/pribil.png"))
setting_img = ImageTk.PhotoImage(Image.open("files/setting.png"))


pads = tk.Button(header, width=13, height=1, borderwidth = 0)
boxes = tk.Button(header, width=13, height=1, borderwidth = 0)

pads["text"] = "Колоды"
boxes["text"] = "Ящики"
pads["bg"] = "#d3d3d3"
boxes["bg"] = "#d3d3d3"


main1 = tk.Frame(main)
add = tk.Button(main1, image=plus, relief="flat")
theme1 = tk.Button(main1, width=7, height=5, borderwidth = 0)


main2 = tk.Frame(main)
theme2 = tk.Button(main2, width=7, height=5, borderwidth = 0)
theme3 = tk.Button(main2, width=7, height=5, borderwidth = 0)

main3 = tk.Frame(main)
theme4 = tk.Button(main3, width=7, height=5, borderwidth = 0)
theme5 = tk.Button(main3, width=7, height=5, borderwidth = 0)

cards = tk.Button(footer, image = cards_img, relief="flat")
learn = tk.Button(footer, image = learn_img, relief="flat")
statistic = tk.Button(footer, image = pribil_img, relief="flat")
setting = tk.Button(footer, image = setting_img, relief="flat")




header.pack(pady=15, padx=5)
main.pack()
footer.pack(pady=15, padx=2)

pads.pack(side=tk.LEFT)
boxes.pack(side=tk.LEFT)

main1.pack(side=tk.TOP, pady=10)
add.pack(side=tk.LEFT, padx=10)
theme1.pack(side=tk.LEFT, padx=10)

main2.pack(side=tk.TOP, pady=10)
theme2.pack(side=tk.LEFT, padx=10)
theme3.pack(side=tk.LEFT, padx=10)

main3.pack(side=tk.TOP, pady=10)
theme4.pack(side=tk.LEFT, padx=10)
theme5.pack(side=tk.LEFT, padx=10)

cards.pack(side=tk.LEFT, padx=5, pady=5)
learn.pack(side=tk.LEFT, padx=5, pady=5)
statistic.pack(side=tk.LEFT, padx=5, pady=5)
setting.pack(side=tk.LEFT, padx=5, pady=5)

root.geometry('250x470')# Размеры всего приложения
root.resizable(width=False, height=False)# Запрет на изменение размеров

#Подсветка при наведении
pads.bind("<Button-1>", mouse)
boxes.bind("<Button-1>", mouse)
add.bind("<Button-1>", add_func)
theme1.bind("<Button-1>", theme_func1)
theme2.bind("<Button-1>", theme_func2)
theme3.bind("<Button-1>", theme_func3)
theme4.bind("<Button-1>", theme_func4)
theme5.bind("<Button-1>", theme_func5)
root.mainloop()
