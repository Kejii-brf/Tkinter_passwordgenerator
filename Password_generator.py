#Şifre oluşturucu

from tkinter import *
from tkinter import messagebox
import string
from random import *

def şifre():
    yazdır.delete(0, END)
    minimum = int(entgiriş1.get())
    maximum = int(entgiriş2.get())
    platform = str(entgiriş3.get())
    try:
        characters = string.ascii_letters + string.punctuation  + string.digits
        password =  "".join(choice(characters) for x in range(randint(minimum, maximum)))
        newpassword = "".join([platform, ":", " ", password])
        yazdır.insert(END, f"{newpassword}")
        Şifreler = open("Şifreler.txt", "a")
        Şifreler.write(newpassword + "\n")
        Şifreler.write("\n")
        Şifreler.write("_______________________________________________" + "\n")
        Şifreler.close()
        messagebox.showinfo("Başarılı!","Yeni şifreniz başarıyla kaydedildi!")    
    except:
        messagebox.showinfo("Hata!","Şifreniz kaydedilemedi!")
    

pencere = Tk()
pencere.title("PassGenerator")
pencere.geometry("500x300")
pencere.resizable(FALSE, FALSE)
pencere.configure(bg="light gray")

Pass = Label(pencere, text="~Password Generator~", font="Verdana 15 bold", bg="light gray")
Pass.pack()

lblgiriş1 = Label(pencere, text="Minimum karakter sayısı →", font="Verdana 12 italic", bg="light gray")
lblgiriş1.place(x=8, y=50)

lblgiriş2 = Label(pencere, text="Maximum karakter sayısı →", font="Verdana 12 italic", bg="light gray")
lblgiriş2.place(x=8, y=90)

lblgiriş3 = Label(pencere, text="Hangi platform için →", font="Verdana 12 italic", bg="light gray")
lblgiriş3.place(x=8, y=130)

entgiriş1 = Entry(pencere, font="Verdana 12 bold", fg="light blue", bg="gray")
entgiriş1.place(x=240, y=53)

entgiriş2 = Entry(pencere, font="Verdana 12 bold", fg="light blue", bg="gray")
entgiriş2.place(x=240, y=93)

entgiriş3 = Entry(pencere, font="Verdana 12 bold", fg="light blue", bg="gray")
entgiriş3.place(x=240, y=133)

oluştur = Button(pencere, text="Oluştur!", font="Verdana 12 bold", bg="gray", command=şifre)
oluştur.place(x=200, y=180)

yazdır = Listbox(pencere, font="Verdana 10 bold", bg="gray", fg="white", width=28, height=2)
yazdır.place(x=115, y=230)




pencere.mainloop()
