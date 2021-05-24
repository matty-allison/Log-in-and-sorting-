from tkinter import*
from tkinter import messagebox
root = Tk()
root.title("LOG IN")
root.geometry("600x270")
frame = Frame(root)
root.config(bg="#45c9b1")
namelabel = Label(root, text="Please enter your name:")
namelabel.place(x=100, y=80)
namelabel.config(bg="#45c9b1", font=("Consolas 9 bold"))
name_entry = Entry(root)
name_entry.place(x=305, y=80)
passlabel = Label(root, text="Please enter your password:")
passlabel.place(x=100, y=140)
passlabel.config(bg="#45c9b1", font=("Consolas 9 bold"))
pass_entry = Entry(root, show="*")
pass_entry.place(x=305, y=140)
def exit():
    root.destroy()
def clear():
    pass_entry.delete(0, END)
    name_entry.delete(0, END)
def check():
    username = ["Matthew", "Zaid", "Godwin", "Gary", "Zoe"]
    password = ["1111", "2222", "3333", "4444", "5555"]
    found = False
    for x in range (len(username)):
        if name_entry.get() == username[x] and pass_entry.get() == password[x]:
            found = True
    if found == True:
        messagebox.showinfo("STATUS", "Access Granted Welcome " + str(name_entry.get()))
        root.destroy()
        import nextwindow
    else:
        messagebox.showinfo("ERROR", "Access Denied")

btn = Button(root, text="Log in", borderwidth="5", command=check)
btn.place(x=200, y=200)
btn.config(bg="#338c7b", font=("Consolas 10 bold"))
btn_clear = Button(root, text="Clear", borderwidth="5", command=clear)
btn_clear.place(x=300, y=200)
btn_clear.config(bg="#338c7b", font=("Consolas 10 bold"))
btn_exit = Button(root, text="Exit", borderwidth="5", command=exit)
btn_exit.place(x=400, y=200)
btn_exit.config(bg="#338c7b", font=("Consolas 10 bold"))

root.mainloop()
