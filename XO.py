from tkinter import *
from tkinter import messagebox
def play(btn):
    global dor
    global win
    global winner
    global t
    global g
    global btns
    if not win and not t:
        if btn["text"] == "":
            btn.configure(text=dor)
            if dor == "O":
                dor = "X"
            else:
                dor = "O"
        dash.configure(text = dor)

        if btns[0]["text"] == btns[1]["text"] and btns[1]["text"] == btns[2]["text"] and btns[0]["text"] != "":
            if btns[0]["text"] == 'X' or btns[0]["text"] == 'O':
                wins(btns[0], btns[1], btns[2], btns[0]["text"])
        
        if btns[3]["text"] == btns[4]["text"] and btns[4]["text"] == btns[5]["text"] and btns[3]["text"] != "":
            if btns[3]["text"] == 'X' or btns[3]["text"] == 'O':
                wins(btns[3], btns[4], btns[5], btns[3]["text"])

        if btns[6]["text"] == btns[7]["text"] and btns[7]["text"] == btns[8]["text"] and btns[6]["text"] != "":
            if btns[6]["text"] == 'X' or btns[6]["text"] == 'O':
                wins(btns[6], btns[7], btns[8], btns[6]["text"])


        if btns[0]["text"] == btns[3]["text"] and btns[3]["text"] == btns[6]["text"] and btns[0]["text"] != "":
            if btns[0]["text"] == 'X' or btns[0]["text"] == 'O':
                wins(btns[0], btns[3], btns[6], btns[0]["text"])
        
        if btns[1]["text"] == btns[4]["text"] and btns[4]["text"] == btns[7]["text"] and btns[1]["text"] != "":
            if btns[1]["text"] == 'X' or btns[1]["text"] == 'O':
                wins(btns[1], btns[4], btns[7], btns[1]["text"])

        if btns[2]["text"] == btns[5]["text"] and btns[2]["text"] == btns[8]["text"] and btns[2]["text"] != "":
            if btns[2]["text"] == 'X' or btns[2]["text"] == 'O':
                wins(btns[2], btns[5], btns[8], btns[2]["text"])

        
        if btns[0]["text"] == btns[4]["text"] and btns[4]["text"] == btns[8]["text"] and btns[0]["text"] != "":
            if btns[0]["text"] == 'X' or btns[0]["text"] == 'O':
                wins(btns[0], btns[4], btns[8], btns[0]["text"])

        if btns[2]["text"] == btns[4]["text"] and btns[2]["text"] == btns[6]["text"] and btns[2]["text"] != "":
            if btns[2]["text"] == 'X' or btns[2]["text"] == 'O':
                wins(btns[6], btns[4], btns[2], btns[2]["text"])

def wins(win1, win2, win3, winner):
    global win
    win = True
    winnerbtns.clear()
    winnerbtns.append(win1)
    winnerbtns.append(win2)
    winnerbtns.append(win3)
    for winbtn in winnerbtns:
        winbtn.configure(bg = bgs[2], fg = fgs[2])
    dash.configure(text=f"{winner} فاز")

def chtheme(bg, fg, bg2, fg2, bg3, fg3):
    bgs[0] = bg
    bgs[1] = bg2
    bgs[2] = bg3
    fgs[0] = fg
    fgs[1] = fg2
    fgs[2] = fg3

    for btn in btns:
        btn.configure(bg=bgs[0], fg=fgs[0])

    if win:
        for winbtn in winnerbtns:
            winbtn.configure(bg = bgs[2], fg = fgs[2])

    for item in items:
        item.configure(bg=bgs[1], fg=fgs[1])
    


def clear(btnsE):
    global win
    global dor
    global t
    global g
    for btn in btnsE:
        btn.configure(text = "", bg = bgs[0], fg = fgs[0])
    dor = "X"
    t = False
    g = 0
    dash.configure(text=dor)
    win = False

# About Window
def about():
    about = "لعبة (Tic Tac Toe) الأصدار 2.0 \n المطور العربي - جميع الحقوق محفوظة ©"
    msg = messagebox.showinfo("حول اللعبة", message=about)
# Variables
dor = "X"
winner = ""
winnerbtns = []
g = 0
win = False
t = False
rows = 3
cols = 3
my = 5
mx = 5
FONT = ("Tajawal", 28)
bgs = [
    "#d9cec8",
    "#d9cec8",
    "gray"
]

fgs = [
    "#474442",
    "#474442",
    "whitesmoke"
]

widths = [
    4,
]

heights = [
    1,
]

# Window settings
root = Tk()
root.geometry("500x340")
root.resizable(False, False)
root.title("V[2] (X O) المطور العربي - لعبة")
root.iconbitmap("H:\\Tutorials\\Tutorials\\X O Game\\assets\\tic-tac-toe.ico")

GFrame = Frame(root)
GFrame.place(x=20, y=20)

btns = []

for y in range(rows):
    for x in range(cols):
        btn = Button(GFrame, width = widths[0], height = heights[0])
        btn.grid(row=y, column=x, padx=mx, pady=my)
        btns.append(btn)

for btn in btns:
    btn.configure(text = '', font=FONT, bg=bgs[0], fg=fgs[0], cursor="hand2", relief="groove")

btns[0].configure(command = lambda:play(btns[0]))
btns[1].configure(command = lambda:play(btns[1]))
btns[2].configure(command = lambda:play(btns[2]))
btns[3].configure(command = lambda:play(btns[3]))
btns[4].configure(command = lambda:play(btns[4]))
btns[5].configure(command = lambda:play(btns[5]))
btns[6].configure(command = lambda:play(btns[6]))
btns[7].configure(command = lambda:play(btns[7]))
btns[8].configure(command = lambda:play(btns[8]))


# Dashboard
dash = Label(root, text=dor, bg=bgs[0], fg=fgs[0], font=("Tajawal", 20, 'bold'))
dash.place(x = 320, y=30, height=40, width=170)

# Clear Button
clr = Button(root, text="إعادة", bg=bgs[0], fg=fgs[0], font=("Tajawal", 18, 'bold'), command=lambda:clear(btns), cursor="hand2")
clr.place(x = 320, y=80, height=40, width=170)


# Themes
thfra = Frame(root)
thfra.place(x=320, y=135, width=170, height=100)

thlab = Label(thfra, text="السمات", font=("Tajawal", 14))
thlab.pack(fill=X)

thbtn1 = Button(thfra, bg='#474442', command=lambda:chtheme('#474442', '#bfbfbf', 'black', 'white', 'gray', 'whitesmoke'), cursor="hand2")
thbtn1.place(x=20, y=40, width=60, height=50)

thbtn4 = Button(thfra, bg="#d9cec8", command=lambda:chtheme("#d9cec8", '#474442', '#d9cec8', '#474442', "gray", "whitesmoke"), cursor="hand2")
thbtn4.place(x=90, y=40, width=60, height=50)

# Rights Label
rilab = Label(root, text="جميع الحقوق محفوظة ©", font=("Tajawal", 10))
rilab.place(x=335, y=300)

# About Window
abo = Button(root, text="حول", bg=bgs[0], fg=fgs[0], font=("Tajawal", 18, 'bold'), command=about, cursor="hand2")
abo.place(x = 320, y=250, height=40, width=170)


items = [dash, clr, abo]
labels = [thlab, rilab]
root.mainloop()