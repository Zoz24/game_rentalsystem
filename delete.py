from tkinter import *
from tkinter import messagebox
import psycopg2


def delete():
    gid = gameID.get()
    deleteGameSQL = "DELETE FROM " + gameTable + " WHERE GID = '"+gid+"'" 
    deleteRentedSQL = "DELETE FROM " + rentTable + " WHERE GID = '"+gid+"'"
    try:
        cur.execute(deleteGameSQL)
        con.commit()
        cur.execute(deleteRentedSQL)
        con.commit()
        messagebox.showinfo('Success, the game has been deleted')
    except:
        messagebox.showinfo('Failed, please check ID')
    gameID.delete(0, END)
    base.destroy() 


def deleteGames():

    global gameID, Canvas1, con, cur, gameTable, rentTable, base

    con = psycopg2.connect(
    host="localhost",
    database="GameStop",
    user="postgres",
    password="asd010203")
    cur = con.cursor()

    gameTable = 'games'
    rentTable = 'games_out'
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
    headingLabel1 = Label(headingFrame1, text='Delete Games', bg='yellow', fg='black', font=('Arial', 15))
    headingLabel1.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Create Label Frame
    labelFrame = Frame(base, bg='yellow')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    label1 = Label(labelFrame, text='Game ID: ', bg='yellow', fg='black')
    label1.place(relx=0.03, rely=0.4, relwidth=0.4, relheight=0.08)
    gameID = Entry(labelFrame)
    gameID.place(relx=0.3,rely=0.4, relwidth=0.6, relheight=0.08)

    # Submit Button
    BtnSubmit = Button(base, text='Submit', bg='yellow', fg='red', command=delete)
    BtnSubmit.place(relx=0.2, rely=0.85, relwidth=0.2, relheight=0.1)
    # Quit Button
    BtnQuit = Button(base, text='Quit', bg='yellow', fg='red', command=base.destroy)
    BtnQuit.place(relx=0.6, rely=0.85, relwidth=0.2, relheight=0.1)

    base.mainloop()