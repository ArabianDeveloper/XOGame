from tkinter import *
import webbrowser as wbe

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

        if btn1["text"] == btn4["text"] and btn4["text"] == btn7["text"] and btn1["text"] != "":
            if btn1["text"] == 'X' or btn1["text"] == 'O':
                wins(btn1, btn4, btn7, btn1["text"])
        
        if btn2["text"] == btn5["text"] and btn5["text"] == btn8["text"] and btn2["text"] != "":
            if btn2["text"] == 'X' or btn2["text"] == 'O':
                wins(btn2, btn5, btn8, btn2["text"])

        if btn3["text"] == btn6["text"] and btn6["text"] == btn9["text"] and btn3["text"] != "":
            if btn3["text"] == 'X' or btn3["text"] == 'O':
                wins(btn3, btn6, btn9, btn3["text"])


        if btn1["text"] == btn2["text"] and btn2["text"] == btn3["text"] and btn1["text"] != "":
            if btn1["text"] == 'X' or btn1["text"] == 'O':
                wins(btn1, btn2, btn3, btn1["text"])
        
        if btn4["text"] == btn5["text"] and btn5["text"] == btn6["text"] and btn4["text"] != "":
            if btn4["text"] == 'X' or btn4["text"] == 'O':
                wins(btn4, btn5, btn6, btn4["text"])

        if btn7["text"] == btn8["text"] and btn7["text"] == btn9["text"] and btn7["text"] != "":
            if btn7["text"] == 'X' or btn7["text"] == 'O':
                wins(btn7, btn8, btn9, btn7["text"])

        
        if btn1["text"] == btn5["text"] and btn5["text"] == btn9["text"] and btn1["text"] != "":
            if btn1["text"] == 'X' or btn1["text"] == 'O':
                wins(btn1, btn5, btn9, btn1["text"])

        if btn7["text"] == btn5["text"] and btn7["text"] == btn3["text"] and btn7["text"] != "":
            if btn7["text"] == 'X' or btn7["text"] == 'O':
                wins(btn3, btn5, btn7, btn7["text"])

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

    dash.configure(bg=bgs[1], fg=fgs[1])
    clr.configure(bg=bgs[1], fg=fgs[1])


# Variables
dor = "X"
winner = ""
winnerbtns = []
g = 0
win = False
t = False
FONT = ("Tajawal", 26)
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
    60,
]

heights = [
    60,
]


# Window settings
root = Tk()
root.geometry("360x290")
root.resizable(False, False)
root.title("V[1.1] (X O) المطور العربي - لعبة")
root.iconbitmap("H:\\Tutorials\\Tutorials\\X O Game\\tic-tac-toe.ico")


# First Row

# Dashboard
dash = Label(root, text=dor, bg=bgs[0], fg=fgs[0], font=("Tajawal", 20, 'bold'))
dash.place(x = 20, y=10, height=40, width=170)

# Buttons

# Column 1
btn1 = Button(root, command=lambda:play(btn1))
btn1.place(x = 20, y = 60)
btn2 = Button(root, command=lambda:play(btn2))
btn2.place(x = 20, y = 115)
btn3 = Button(root, command=lambda:play(btn3))
btn3.place(x = 20, y = 170)

# Column 2
btn4 = Button(root, command=lambda:play(btn4))
btn4.place(x = 75, y = 60)
btn5 = Button(root, command=lambda:play(btn5))
btn5.place(x = 75, y = 115)
btn6 = Button(root, command=lambda:play(btn6))
btn6.place(x = 75, y = 170)

# Column 3
btn7 = Button(root, command=lambda:play(btn7))
btn7.place(x = 130, y = 60)
btn8 = Button(root, command=lambda:play(btn8))
btn8.place(x = 130, y = 115)
btn9 = Button(root, command=lambda:play(btn9))
btn9.place(x = 130, y = 170)

btns = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

for btn in btns:
    btn.configure(text="", font=FONT, bg=bgs[0], fg=fgs[0], cursor="hand2", relief="groove")
    btn.place(width=widths[0], height=heights[0])

# Clear Button
clr = Button(root, text="إعادة", bg=bgs[0], fg=fgs[0], font=("Tajawal", 18, 'bold'), command=lambda:clear(btns), cursor="hand2")
clr.place(x = 20, y=240, height=40, width=170)

# Bio Lable
bio = """\
       محمد الشعيلي مطور
     بايثون ومتخصص في النظم
    الخلفية للمواقع الألكترونية
"""

bilab = Label(root, text=bio, font=("Tajawal", 10))
bilab.place(x=190, y=110)

# Themes
thlab = Label(root, text="الأوضاع", font=("Tajawal", 10))
thlab.place(x=255, y=10)

thbtn1 = Button(root, bg='#474442', command=lambda:chtheme('#474442', '#bfbfbf', 'black', 'white', 'gray', 'whitesmoke'), cursor="hand2")
thbtn1.place(x=220, y=40, width=50, height=50)

thbtn4 = Button(root, bg="#d9cec8", command=lambda:chtheme("#d9cec8", '#474442', '#d9cec8', '#474442', "gray", "whitesmoke"), cursor="hand2")
thbtn4.place(x=280, y=40, width=50, height=50)


# Github Button
ghim = PhotoImage(file="H:\\Tutorials\\Tutorials\\X O Game\\github-logo.png")
resghim = ghim.subsample(3,3)
lnkbtn1 = Button(root, image=resghim, text="  GitHub", command=lambda:wbe.open("https://github.com/ArabianDeveloper"), font=("Tajawal", 11), cursor="hand2", compound=LEFT)
lnkbtn1.place(x=210, y=180, width=130, height=60)

# Rights Label
rilab = Label(root, text="جميع الحقوق محفوظة ©", font=("Tajawal", 10))
rilab.place(x=210, y=250)

root.mainloop()