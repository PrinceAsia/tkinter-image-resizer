import os
import tkinter as tk
from PIL import Image
from tkinter import CENTER, Frame, messagebox, filedialog

class AppWindow:
    def __init__(self, object):
        self.openImages()
        self.resizeImageInterface()
        menyu = tk.Menu(app)
        app.configure(menu=menyu)
        menyu1 = tk.Menu(menyu)
        menyu.add_cascade(label='Fayl', menu=menyu1)
        menyu1.add_command(label='Dastur haqida', command=self.about)
        menyu1.add_command(label='Mualliflar', command=self.author)
        self.my_files = []

    def about(self):
        tk.messagebox.showinfo(title='Dastur haqida', message="Image resizer - rasmlar o‘lchamini avtomatik o‘zgartirish dasturi\nRahbar: Mallayev Oybek")
    def author(self):
        tk.messagebox.showinfo(title='Dastur mualliflari', message="Ganiyev Anvarjon Abduhalil o‘g‘li")
    
    def openImages(self):
        self.s_canvas = tk.Canvas(app, width='450', height='350', bg='gray')
        self.s_canvas.pack(side='left')
        self.s_sarlavha = tk.Label(app, text='Rasmlarni yuklab olish uchun papkani ko‘rsating', font='30')
        self.s_sarlavha.place(x=50, y=15)
        self.s_btn_ochish = tk.Button(self.s_canvas, text='Papkani ochish', command=self.openFolder)
        self.s_btn_ochish.place(x=30, y=50)
        self.s_entry_fayl = tk.Entry(self.s_canvas, font='Times 12 normal', width='35')
        self.s_entry_fayl.place(x=130, y=50)
        self.s_txt_info = tk.Text(self.s_canvas, height=13, width=48)
        self.s_txt_info.place(x=30, y=100)

    def openFolder(self):
        self.folder = filedialog.askdirectory(initialdir=os.path.normpath("C://"), title="Example")
        self.s_entry_fayl.insert(0, self.folder)
        all_files = os.listdir(path=self.folder)
        self.s_txt_info.insert('1.0', '\t\tRASMLAR RO‘YHATI\n')
        for f in all_files:
            if '.jpg' in f.lower():
                self.my_files.append(f)
        print(self.my_files)
        for i in range(len(self.my_files)):
            iindex = str(i+2) + '.0'
            self.s_txt_info.insert(iindex, str(i+1) + '.  ' + self.my_files[i] + '\n')
    


    def showMsgProporsinality(self):
        tk.messagebox.showinfo(title='Diqqat!!!', message="   Rasm eni yoki bo‘yidan faqat bittasi foydalanuvchi tomonidan kiritilishi kerak.\nQolgan tomoni shunga proporsional tarzda aniqlanadi, aks holda rasm ko‘rinishi buzilishi mumkin!")
        
    def resizeImage(self):
        for img in self.my_files:
            new_Size = int(self.r_entry_fayl.get())
            user_Side = self.options.get()
            original_Image = Image.open(self.folder + '/' + img)
            org_Width, org_Height = original_Image.size
            new_width = new_Size if user_Side=='Eni=' else int((new_Size * org_Width) / org_Height)
            new_height = new_Size if user_Side=='Bo‘yi=' else int((new_Size * org_Height) / org_Width)
            new_Image = original_Image.resize((new_width, new_height))
            new_Image.save(fp=user_Side + str(new_Size) + '_' + img)

    
    def resizeImageInterface(self):
        self.r_canvas = tk.Canvas(app, width='450', height='350', bg='gray')
        self.r_canvas.pack(side='left')
        self.r_sarlavha = tk.Label(app, text='Kerakli parametrlarni sozlash va o‘lchamlarni o‘zgartirish', font='30')
        self.r_sarlavha.place(x=480, y=15)
        self.r_btn_ochish = tk.Button(self.r_canvas, text='O‘rnatish:', command=self.showMsgProporsinality)
        self.r_btn_ochish.place(x=30, y=50)
        
        self.options = tk.StringVar(app)
        self.options.set('Eni=')
        self.r_options = tk.OptionMenu(app, self.options, 'Eni=', 'Bo‘yi=')
        self.r_options.place(x=550, y=70)
        
        self.r_entry_fayl = tk.Entry(self.r_canvas, font='Times 12 normal', width='10')
        self.r_entry_fayl.place(x=190, y=50)
        
        self.r_btn_ochish = tk.Button(self.r_canvas, text='O‘ZGARTIRISH', command=self.resizeImage, font='Times 12 bold')
        self.r_btn_ochish.place(x=290, y=47)

        self.r_txt_info = tk.Text(self.r_canvas, height=13, width=48)
        self.r_txt_info.place(x=30, y=100)
    

app = tk.Tk()
app.title('Image resizer - rasmlar o‘lchamini avtomatik o‘zgartirish dasturi')
w = app.winfo_screenwidth() # Ekran eni
h = app.winfo_screenheight() # Ekran bo‘yi
w = w//2 # Ekran markazi
h = h//2 # koordinatalari
w = w - 450
h = h - 200
app.geometry('900x400+{}+{}'.format(w, h))
app.resizable(0,0)
app.configure(background='gray')# yoki app['bg'] = 'gray'
dastur = AppWindow(app)
app.mainloop()