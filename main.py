import tkinter
from tkinter import *

root = Tk()
root.title("ToDo_App")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []


def add_task():
    task = task_entry.get()
    task_entry.delete(0, END)
    
    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)


def reader():
    try:
        global task_list
        with open("tasks.txt") as file:
            tasks = file.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)
    except FileNotFoundError:
        file = open("tasks.txt", "w")
        file.close()


def delete_task():
    global task_list
    entery = str(listbox.get(ANCHOR))
    if entery in task_list:
        task_list.remove(entery)
        with open('tasks.txt', 'w') as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")

        listbox.delete( ANCHOR)


# icon
iconPhoto = PhotoImage(file="Image/task.png")
root.iconphoto(False, iconPhoto)


topbarrPhoto = PhotoImage(file="image/topbar.png")
Label(root,image=topbarrPhoto).pack()

dockImage = PhotoImage(file="image/dock.png")
Label(root,image=dockImage,bg="#32405b").place(x=30,y=25)

noteImage = PhotoImage(file="image/task.png")
Label(root,image=noteImage,bg="#32405d").place(x=340,y=25)

heading = Label(root,text="ALL TASK",font="arial 20 bold",fg="white",bg="#32405b").place(x=130,y=20)
frame = Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button = Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#5a95ff",fg="#fff",bd=0, command=add_task)
button.place(x=300,y=0)


#listbox
frame1= Frame(root, bd=3,width=700,height=280,bg="#32405d")
frame1.pack(pady=(160,0))

listbox= Listbox(frame1,font=('arial',12),width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side= RIGHT ,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

reader()


#delete
delete_icon = PhotoImage(file="Image/delete.png")
delete = Button(root, image=delete_icon, bd=0, command=delete_task).pack(side=BOTTOM,pady=13)


root.mainloop()

