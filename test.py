from tkinter import *

width = 30
height = 30
mx = 5
my = 5

rows = 3
cols = 3
root = Tk()
btns = []


# 1
# for y in range(cols):
#     btn = Button(root, text=10)
#     btn.place(width=width, height=height)
#     btns.append(btn)

#     for btn in btns:
#         if btns.index(btn) - 1 != -1:
#             widofpbtn = int(btns[btns.index(btn) - 1].place_info()['width'])
#             xofpbtn = int(btns[btns.index(btn) - 1].place_info()['x'])

#             heiofpbtn = int(btns[btns.index(btn) - 1].place_info()['height'])
#             yofpbtn = int(btns[btns.index(btn) - 1].place_info()['y'])

#             btn.place(x=str(widofpbtn + xofpbtn + mx), y=my)
#             print(f"""\
#                 x = {btns[btns.index(btn) - 1].place_info()['x']}
#                 y = {btns[btns.index(btn) - 1].place_info()['y']}
#                 width = {btns[btns.index(btn) - 1].place_info()['width']}
#                 height = {btns[btns.index(btn) - 1].place_info()['height']}
#             """)
#         else :
#             btn.place(x=mx, y=my)



# 2

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
    15,
]

heights = [
    1,
]


for y in range(rows):
    for x in range(cols):
        btn = Button(root)
        btn.grid(row=y, column=x, ipadx=widths[0], ipady=heights[0], padx=mx, pady=my)
        btns.append(btn)

for btn in btns:
    btn.configure(text = btns.index(btn), font=FONT, bg=bgs[0], fg=fgs[0], cursor="hand2", relief="groove")

# Buttons

# # Column 1
# btn1 = Button(root, command=lambda:play(btn1))
# btn1.place(x = 20, y = 60)
# btn2 = Button(root, command=lambda:play(btn2))
# btn2.place(x = 20, y = 115)
# btn3 = Button(root, command=lambda:play(btn3))
# btn3.place(x = 20, y = 170)

# # Column 2
# btn4 = Button(root, command=lambda:play(btn4))
# btn4.place(x = 75, y = 60)
# btn5 = Button(root, command=lambda:play(btn5))
# btn5.place(x = 75, y = 115)
# btn6 = Button(root, command=lambda:play(btn6))
# btn6.place(x = 75, y = 170)

# # Column 3
# btn7 = Button(root, command=lambda:play(btn7))
# btn7.place(x = 130, y = 60)
# btn8 = Button(root, command=lambda:play(btn8))
# btn8.place(x = 130, y = 115)
# btn9 = Button(root, command=lambda:play(btn9))
# btn9.place(x = 130, y = 170)

root.mainloop()