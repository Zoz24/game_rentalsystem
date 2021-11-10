from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import psycopg2

def viewGames():

    con = psycopg2.connect(
    host="localhost",
    database="GameStop",
    user="postgres",
    password="asd010203")

    cur = con.cursor()
    gameTable = 'games'

    base = Tk()
    base.title('GameStop')
    base.minsize(width=400, height=400)
    base.geometry('800x600')

 

    Canvas1 = Canvas(base)
    Canvas1.config(bg='green')
    Canvas1.pack(expand=True, fill=BOTH)

    # Create Head Frame
    headingFrame1 = Frame(base, bg='yellow', bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.15)
    headingLabel1 = Label(headingFrame1, text='View Games', bg='yellow', fg='black', font=('Arial', 15))
    headingLabel1.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Create Label Frame
    labelFrame = Frame(base, bg='yellow')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    label = Label(labelFrame, text='%-30s%-40s%-40s%-30s'%('GID','Title','Studio','Status'), bg='yellow', fg='black')
    label.place(relx=0.07,rely=0.1)
    Label(labelFrame, text = "-------------------------------------------------------------------------------------",bg='yellow',fg='black').place (relx=0.05,rely=0.2)

    getGames = 'SELECT * from ' + gameTable 
    y = 0.25

    
    try:
        cur.execute(getGames)
        con.commit()
        for i in cur:
            Label(labelFrame, text='%-30s%-40s%-45s%-30s'%(i[0], i[1], i[2], i[3]), bg='yellow', fg='black').place(relx=0.07,rely=y)
            y += 0.12
    except:
        messagebox.showinfo('Unable to fetch files from database, check for error')

    # Quit Button
    BtnQuit = Button(base, text='Quit', bg='yellow', fg='red', command=base.destroy)
    BtnQuit.place(relx=0.38, rely=0.85, relwidth=0.2, relheight=0.1)


    base.mainloop()
