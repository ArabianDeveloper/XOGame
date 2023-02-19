from tkinter import *

width = 50
height = 50
mx = 5
my = 5

rows = 3
cols = 3
root = Tk()
btns = []


for y in range(cols):
    btn = Button(root, text=10)
    btn.place(width=width, height=height)
    btns.append(btn)

    for btn in btns:
        if btns.index(btn) - 1 != -1:
            widofpbtn = int(btns[btns.index(btn) - 1].place_info()['width'])
            xofpbtn = int(btns[btns.index(btn) - 1].place_info()['x'])

            heiofpbtn = int(btns[btns.index(btn) - 1].place_info()['height'])
            yofpbtn = int(btns[btns.index(btn) - 1].place_info()['y'])

            btn.place(x=str(widofpbtn + xofpbtn + mx), y=my)
            print(f"""\
                x = {btns[btns.index(btn) - 1].place_info()['x']}
                y = {btns[btns.index(btn) - 1].place_info()['y']}
                width = {btns[btns.index(btn) - 1].place_info()['width']}
                height = {btns[btns.index(btn) - 1].place_info()['height']}
            """)
        else :
            btn.place(x=mx, y=my)

root.mainloop()