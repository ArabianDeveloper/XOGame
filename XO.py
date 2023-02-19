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
                win = True
                winner = btn1["text"]
                winnerbtns.clear()
                winnerbtns.append(btn1)
                winnerbtns.append(btn4)
                winnerbtns.append(btn7)
                for winbtn in winnerbtns:
                    winbtn.configure(bg = bgs[2], fg = fgs[2])
                dash.configure(text=f"{winner} فاز")
        
        if btn2["text"] == btn5["text"] and btn5["text"] == btn8["text"] and btn2["text"] != "":
            if btn2["text"] == 'X' or btn2["text"] == 'O':
                win = True
                winner = btn2["text"]
                winnerbtns.clear()
                winnerbtns.append(btn2)
                winnerbtns.append(btn5)
                winnerbtns.append(btn8)
                for winbtn in winnerbtns:
                    winbtn.configure(bg = bgs[2], fg = fgs[2])
                dash.configure(text=f"{winner} فاز")

        if btn3["text"] == btn6["text"] and btn6["text"] == btn9["text"] and btn3["text"] != "":
            if btn3["text"] == 'X' or btn3["text"] == 'O':
                win = True
                winner = btn3["text"]
                winnerbtns.clear()
                winnerbtns.append(btn3)
                winnerbtns.append(btn6)
                winnerbtns.append(btn9)
                for winbtn in winnerbtns:
                    winbtn.configure(bg = bgs[2], fg = fgs[2])
                dash.configure(text=f"{winner} فاز")



        if btn1["text"] == btn2["text"] and btn2["text"] == btn3["text"] and btn1["text"] != "":
            if btn1["text"] == 'X' or btn1["text"] == 'O':
                win = True
                winner = btn1["text"]
                winnerbtns.clear()
                winnerbtns.append(btn1)
                winnerbtns.append(btn2)
                winnerbtns.append(btn3)
                for winbtn in winnerbtns:
                    winbtn.configure(bg = bgs[2], fg = fgs[2])
                dash.configure(text=f"{winner} فاز")
        
        if btn4["text"] == btn5["text"] and btn5["text"] == btn6["text"] and btn4["text"] != "":
            if btn4["text"] == 'X' or btn4["text"] == 'O':
                win = True
                winner = btn4["text"]
                winnerbtns.clear()
                winnerbtns.append(btn4)
                winnerbtns.append(btn5)
                winnerbtns.append(btn6)
                for winbtn in winnerbtns:
                    winbtn.configure(bg = bgs[2], fg = fgs[2])
                dash.configure(text=f"{winner} فاز")

        if btn7["text"] == btn8["text"] and btn7["text"] == btn9["text"] and btn7["text"] != "":
            if btn7["text"] == 'X' or btn7["text"] == 'O':
                win = True
                winner = btn7["text"]
                winnerbtns.clear()
                winnerbtns.append(btn7)
                winnerbtns.append(btn8)
                winnerbtns.append(btn9)
                for winbtn in winnerbtns:
                    winbtn.configure(bg = bgs[2], fg = fgs[2])
                dash.configure(text=f"{winner} فاز")


        
        if btn1["text"] == btn5["text"] and btn5["text"] == btn9["text"] and btn1["text"] != "":
            if btn1["text"] == 'X' or btn1["text"] == 'O':
                win = True
                winner = btn1["text"]
                winnerbtns.clear()
                winnerbtns.append(btn1)
                winnerbtns.append(btn5)
                winnerbtns.append(btn9)
                for winbtn in winnerbtns:
                    winbtn.configure(bg = bgs[2], fg = fgs[2])
                dash.configure(text=f"{winner} فاز")

        if btn7["text"] == btn5["text"] and btn7["text"] == btn3["text"] and btn7["text"] != "":
            if btn7["text"] == 'X' or btn7["text"] == 'O':
                win = True
                winner = btn7["text"]
                winnerbtns.clear()
                winnerbtns.append(btn3)
                winnerbtns.append(btn5)
                winnerbtns.append(btn7)
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
    fgs[0] = fg
    bgs[1] = bg2
    fgs[1] = fg2
    bgs[2] = bg3
    fgs[2] = fg3

    for btn in btns:
        btn.configure(bg=bgs[0], fg=fgs[0])

    if win:
        for winbtn in winnerbtns:
            winbtn.configure(bg = bgs[2], fg = fgs[2])

    dash.configure(bg=bgs[1], fg=fgs[1])
    clr.configure(bg=bgs[1], fg=fgs[1])


dor = "X"
winner = ""
winnerbtns = []
g = 0
win = False
t = False
FONT = ("Tajawal", 24)
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

root = Tk()
root.geometry("350x280")
root.resizable(False, False)
root.title("V[1.0] (X O) المطور العربي - لعبة")
root.iconbitmap("H:\\Tutorials\\Tutorials\\X O Game\\tic-tac-toe.ico")


dash = Label(root, text=dor, bg=bgs[0], fg=fgs[0], font=("Tajawal", 18, 'bold'))
dash.place(x = 20, y=10, height=40, width=160)


btn1 = Button(root, text="", font=FONT, command=lambda:play(btn1), cursor="hand2")
btn1.place(x = 20, y = 60, width=50, height=50)
btn2 = Button(root, text="", font=FONT, command=lambda:play(btn2), cursor="hand2")
btn2.place(x = 20, y = 115, width=50, height=50)
btn3 = Button(root, text="", font=FONT, command=lambda:play(btn3), cursor="hand2")
btn3.place(x = 20, y = 170, width=50, height=50)

btn4 = Button(root, text="", font=FONT, command=lambda:play(btn4), cursor="hand2")
btn4.place(x = 75, y = 60, width=50, height=50)
btn5 = Button(root, text="", font=FONT, command=lambda:play(btn5), cursor="hand2")
btn5.place(x = 75, y = 115, width=50, height=50)
btn6 = Button(root, text="", font=FONT, command=lambda:play(btn6), cursor="hand2")
btn6.place(x = 75, y = 170, width=50, height=50)

btn7 = Button(root, text="", font=FONT, command=lambda:play(btn7), cursor="hand2")
btn7.place(x = 130, y = 60, width=50, height=50)
btn8 = Button(root, text="", font=FONT, command=lambda:play(btn8), cursor="hand2")
btn8.place(x = 130, y = 115, width=50, height=50)
btn9 = Button(root, text="", font=FONT, command=lambda:play(btn9), cursor="hand2")
btn9.place(x = 130, y = 170, width=50, height=50)

btns = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]


clr = Button(root, text="إعادة", bg=bgs[0], fg=fgs[0], font=("Tajawal", 18, 'bold'), command=lambda:clear(btns), cursor="hand2")
clr.place(x = 20, y=230, height=40, width=160)


bio = """\
       محمد الشعيلي مطور
     بايثون ومتخصص في النظم
    الخلفية للمواقع الألكترونية
"""

bilab = Label(root, text=bio, font=("Tajawal", 10))
bilab.place(x=180, y=110)

ghim = PhotoImage(file="H:\\Tutorials\\Tutorials\\X O Game\\github-logo.png")
resghim = ghim.subsample(3,3)
lnkbtn1 = Button(root, image=resghim, text="  GitHub", command=lambda:wbe.open("https://github.com/ArabianDeveloper"), font=("Tajawal", 11), cursor="hand2", compound=LEFT)
lnkbtn1.place(x=200, y=180, width=130, height=60)

thlab = Label(root, text="الأوضاع", font=("Tajawal", 10))
thlab.place(x=245, y=10)

thbtn1 = Button(root, bg='#474442', command=lambda:chtheme('#474442', '#bfbfbf', 'black', 'white', 'gray', 'whitesmoke'), cursor="hand2")
thbtn1.place(x=210, y=40, width=50, height=50)

thbtn4 = Button(root, bg="#d9cec8", command=lambda:chtheme("#d9cec8", '#474442', '#d9cec8', '#474442', "gray", "whitesmoke"), cursor="hand2")
thbtn4.place(x=270, y=40, width=50, height=50)

rilab = Label(root, text="جميع الحقوق محفوظة ©", font=("Tajawal", 9))
rilab.place(x=200, y=250)

for btn in btns:
    btn.configure(bg=bgs[0], fg=fgs[0])


root.mainloop()