from tkinter import *
from PIL import ImageTk, Image
from add import addGames
from view import viewGames
from delete import deleteGames
from rentout import issueGames
from returnGame import returnGame
import psycopg2

con = psycopg2.connect(
    host="localhost",
    database="GameStop",
    user="postgres",
    password="asd010203")

cur = con.cursor()

# Create the window and initiate title and size
base = Tk()
base.title('GameStop')
base.minsize(width=400, height=400)
base.geometry('800x600')

# Add the background image for the window
background_img = Image.open('bg.jpg')
[img_width, img_height] = background_img.size
img = ImageTk.PhotoImage(background_img)

Canvas1 = Canvas(base)
Canvas1.create_image(350, 400, image=img)
Canvas1.config(bg='white', width=img_width, height=img_height)
Canvas1.pack(expand=True, fill=BOTH)

# Create Head Frame
headingFrame1 = Frame(base, bg='yellow', bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.15)
headingLabel1 = Label(headingFrame1, text='GameStop Rental', bg='yellow', fg='black', font=('Arial', 15))
headingLabel1.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(base, text='Add Game', bg='yellow', fg='black', command=addGames)
btn1.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.08)

btn2 = Button(base, text='Delete Game', bg='yellow', fg='black',command=deleteGames)
btn2.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.08)

btn3 = Button(base, text='View Game Inventory', bg='yellow', fg='black', command=viewGames)
btn3.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.08)

btn4 = Button(base, text='Rent Out Game', bg='yellow', fg='black', command=issueGames)
btn4.place(relx=0.3, rely=0.6, relwidth=0.4, relheight=0.08)

btn5 = Button(base, text='Return Game', bg='yellow', fg='black', command=returnGame)
btn5.place(relx=0.3, rely=0.7, relwidth=0.4, relheight=0.08)

base.mainloop()
