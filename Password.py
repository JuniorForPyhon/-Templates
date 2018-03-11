#------------------------------#
#                              #
#      Only the template       #
#       please complete        #
#------------------------------#
from tkinter import *
from tkinter import messagebox
import pickle
from tkinter import ttk

root = Tk()
root.geometry("300x400")
root.title("Sign in")

def registr():
    text = Label(text="Sing up")
    text_log = Label(text="Enter your login")
    redistr_log = Entry()
    text_password = Label(text= "Enter your password")
    registr_password = Entry(show="*")
    text_password2 = Label(text="Re-enter your password")
    registr_password2 = Entry(show="*")
    button_registr = ttk.Button(text="Sing up", command=lambda: save())
    text.pack()
    text_log.pack()
    redistr_log.pack()
    text_password.pack()
    registr_password.pack()
    text_password2.pack()
    registr_password2.pack()
    button_registr.pack()

    def save():
        log_and_password = {}
        log_and_password[redistr_log.get()] = registr_password.get()
        s =open("Login.txt", "wb")
        pickle.dump(log_and_password, s)
        s.close()
        log()

def log():
    text_enter_log = Label(text="Your login:")
    enter_log = Entry()
    text_enter_password = Label(text="Your password:")
    enter_password = Entry(show="*")
    botton_enter = ttk.Button(text="Sing in", command=lambda: prover())
    botton_register = ttk.Button(text="Sing up", command=lambda: registr())
    text_enter_log.pack()
    enter_log.pack()
    text_enter_password.pack()
    enter_password.pack()
    botton_enter.pack()
    botton_register.pack()

    def prover():
        s = open("Login.txt", "rb")
        a = pickle.load(s)
        s.close()
        if enter_log.get() in a:
           if enter_password.get() == a[enter_log.get()]:
               messagebox.showinfo("Sing in", "You are logged in")
           else:
               messagebox.showerror("Sing in", "Error!")
        else:
            messagebox.showerror("Sing in", "Error!")


log()

root.mainloop()
