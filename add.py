from tkinter import *
from tkinter import messagebox
import psycopg2

from returnGame import returnGame

def register():
    gid = gameID.get()
    title = gameTitle.get()
    studio = gameStudio.get()
    status = gameStatus.get().lower()
    insertGames = 'INSERT INTO ' + gameTable + " VALUES('"+gid+"', '"+title+"', '"+studio+"', '"+status+"')"
    try:
        cur.execute(insertGames)
        con.commit()
        messagebox.showinfo('Success, game is added')
    except:
        messagebox.showinfo('Oops, the game is not added, there is an error')
    
    base.destroy()

def addGames():
    global gameID, gameTitle, gameStudio, gameStatus, Canvas1, con, cur, gameTable, base
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
    headingLabel1 = Label(headingFrame1, text='Add Games', bg='yellow', fg='black', font=('Arial', 15))
    headingLabel1.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Create Label Frame
    labelFrame = Frame(base, bg='yellow')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    label1 = Label(labelFrame, text='Game ID: ', bg='yellow', fg='black')
    label1.place(relx=0.03, rely=0.2, relwidth=0.4, relheight=0.08)
    gameID = Entry(labelFrame)
    gameID.place(relx=0.3,rely=0.2, relwidth=0.6, relheight=0.08)

    label2 = Label(labelFrame, text='Game Title: ', bg='yellow', fg='black')
    label2.place(relx=0.03, rely=0.4, relwidth=0.4, relheight=0.08)
    gameTitle = Entry(labelFrame)
    gameTitle.place(relx=0.3,rely=0.4, relwidth=0.6, relheight=0.08)

    label3 = Label(labelFrame, text='Game Studio: ', bg='yellow', fg='black')
    label3.place(relx=0.03, rely=0.6, relwidth=0.4, relheight=0.08)
    gameStudio = Entry(labelFrame)
    gameStudio.place(relx=0.3,rely=0.6, relwidth=0.6, relheight=0.08)

    label4 = Label(labelFrame, text='Rental Status (Avai/Rented): ', bg='yellow', fg='black')
    label4.place(relx=0.03, rely=0.8, relwidth=0.4, relheight=0.08)
    gameStatus = Entry(labelFrame)
    gameStatus.place(relx=0.3,rely=0.8, relwidth=0.6, relheight=0.08)

    # Submit Button
    BtnSubmit = Button(base, text='Submit', bg='yellow', fg='red', command=register)
    BtnSubmit.place(relx=0.2, rely=0.85, relwidth=0.2, relheight=0.1)
    # Quit Button
    BtnQuit = Button(base, text='Quit', bg='yellow', fg='red', command=base.destroy)
    BtnQuit.place(relx=0.6, rely=0.85, relwidth=0.2, relheight=0.1)

    base.mainloop()
