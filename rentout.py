from tkinter import *
from tkinter import messagebox
import psycopg2


con = psycopg2.connect(
host="localhost",
database="GameStop",
user="postgres",
password="asd010203")
cur = con.cursor()
gidList = []
gameTable = 'games'
rentTable = 'games_out'


def issue():
    
    
    gid = gameID.get()
    rentTo = renter.get()

    BtnSubmit.destroy()
    labelFrame.destroy()
    label1.destroy()
    gameID.destroy()
    renter.destroy()
    
    extractGid = "select gid from "+gameTable
    try:
        cur.execute(extractGid)
        con.commit()
        for i in cur:
            gidList.append(i[0])
        
        if gid in gidList:
            checkAvail = "select status from "+gameTable+" where gid = '"+gid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
            if 'avai' in check:
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Book ID not present")
            return
    except:
        messagebox.showinfo("Error","Can't fetch Game IDs")
        return
    
    issueSql = "insert into "+rentTable+" values ('"+gid+"','"+rentTo+"')"
    
    updateStatus = "update "+gameTable+" set status = 'rented' where gid = '"+gid+"'"
    try:
        if gid in gidList and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Game is rented out Successfully")
            base.destroy()
        else:
            gidList.clear()
            messagebox.showinfo('Message',"Game is Already rented")
            base.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")

    
    gidList.clear()

def issueGames():
    global BtnSubmit, BtnQuit, labelFrame, gameID, renter, label1, base, base, Canvas1, status, con, cur

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
    headingLabel1 = Label(headingFrame1, text='Rent Out Games', bg='yellow', fg='black', font=('Arial', 15))
    headingLabel1.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Create Label Frame
    labelFrame = Frame(base, bg='yellow')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    # Create Label
    label1 = Label(labelFrame, text='Game ID: ', bg='yellow', fg='black')
    label1.place(relx=0.03, rely=0.3, relwidth=0.4, relheight=0.08)
    gameID = Entry(labelFrame)
    gameID.place(relx=0.3,rely=0.3, relwidth=0.6, relheight=0.08)

    label2 = Label(labelFrame, text='Renter: ', bg='yellow', fg='black')
    label2.place(relx=0.03, rely=0.5, relwidth=0.4, relheight=0.08)
    renter = Entry(labelFrame)
    renter.place(relx=0.3,rely=0.5, relwidth=0.6, relheight=0.08)

    # Submit Button
    BtnSubmit = Button(base, text='Submit', bg='yellow', fg='red', command=issue)
    BtnSubmit.place(relx=0.2, rely=0.85, relwidth=0.2, relheight=0.1)
    # Quit Button
    BtnQuit = Button(base, text='Quit', bg='yellow', fg='red', command=base.destroy)
    BtnQuit.place(relx=0.6, rely=0.85, relwidth=0.2, relheight=0.1)

    base.mainloop()
