import tkinter as tk 
from tkinter import ttk
import os
import time

    
cerceve = tk.Tk()

tk.Label(cerceve, text="Kaç Saat Sonra Kapanacağını Giriniz").grid(row=0)
saatsecim = ttk.Combobox(cerceve, 
                            values=[1,2,3,4])
print(dict(saatsecim)) 
saatsecim.grid(column=0, row=1)
saatsecim.current(1)
secim=10
def bilgisayari_kapat():
    global secim
    if(saatsecim.get()=="1"):
       
       secim=3600
    elif(saatsecim.get()=="2"):
        
        secim=7200
    elif(saatsecim.get()=="3"):
        
        secim=10800
    elif(saatsecim.get()=="4"):
   
        secim=14400
    else:
        print=("değer gir")
    intedon=int(secim)
    time.sleep(intedon)
    os.system("notepad")
    bilgisayari_kapat()
tk.Button(cerceve, 
          text='Başlat', 
          command=bilgisayari_kapat).grid(row=3, column=0, sticky=tk.W, pady=4)
cerceve.mainloop()
