'''
Bong!
2 player, one wit arrow keys other uses WS, working printed score. variable bounce angles (acually bounces?) rounded paddle expect it isnot round. sped slider or lv based sped.
'''

import tkinter 
from tkinter import *
root = tkinter.Tk()
import random as R
import math

player_1_score = -1
player_2_score = -1
score_to_win = 10
p1bot_toggle = tkinter.IntVar()
p2bot_toggle = tkinter.IntVar()
speed_intvar = tkinter.IntVar()
speed_intvar.set(1)
r = 10
x = 150
y = 150
X= 0
direction = 0.5 
direction_list = [-.9,-.8,-.7,-.6,-.5,-.4,-.3,-.2,-.1,.1,.2,.3,.4,.5,.6,.7,.8,.9]

def resetscores():
  global player_1_score
  global player_2_score
  player_1_score = 0
  player_2_score = 0
  play_again.grid_forget()
  text3.config(text='Score ' +str(score_to_win) +'\n points\n to win!')
  text.config(text='P1 Score :\n' + '0')
  text2.config(text='P2 Score :\n' + '0')
  animate()

speed_slider = tkinter.Scale(root, from_=10, to=0, variable=speed_intvar)
speed_slider.grid(row=1, column=0, sticky=tkinter.W)
labelfont = ('times', 50, 'bold')
text = tkinter.Label(root,fg="White",bg='black', text='P1 Score :\n' + '0')
text.grid(row=0, column =0)
text2 = tkinter.Label(root, fg="White",bg='black', text='P2 Score :\n' + '0')
text2.grid(row=0, column =2)
text3 = tkinter.Label(root, fg="white",bg='black', text='Score ' +str(score_to_win) +'\n points\n to win!')
text3.grid(row=2,column=0)
p1bot = tkinter.Checkbutton(root, text='P1 bot', variable=p1bot_toggle)
p1bot.grid(row=1,column=2)
p2bot = tkinter.Checkbutton(root, text='P2 bot', variable=p2bot_toggle)
p2bot.grid(row=2,column=2)
canvas = tkinter.Canvas(root, width=600, height=600, background='#FFFFFF')
canvas.grid(row=0, rowspan=3, column=1)
canvas.config(bg='gray', bd=5, relief='groove')
play_again = tkinter.Button(root, text='Play again?', bg = 'Black', fg ='White', command=resetscores)
play_again.grid(row=2,column=1)
play_again.grid_forget()

half_court_line = canvas.create_rectangle(295,0,305,600, outline='#FFFFFF', fill='#FFFFFF')
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r, outline='#000000', fill='#00FFFF')
player_2 = canvas.create_rectangle(580, 580, 560, 405, outline='#000000', fill='#00FFFF')
player_1 = canvas.create_rectangle(40, 195, 20, 20, outline='#000000', fill='#00FFFF')
ball_color = '#00FFFF'

def color_change():
  global ball_color
  hexlist = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
  ball_color = '#' + R.choice(hexlist) + R.choice(hexlist) + R.choice(hexlist) + R.choice(hexlist) + R.choice(hexlist) + R.choice(hexlist)
  canvas.itemconfig(circle_item, fill=ball_color)
  canvas.itemconfig(player_1, fill=ball_color)
  canvas.itemconfig(player_2, fill=ball_color)


def animate():
  global X
  global player_1_score
  global player_2_score
  global direction_list
  X += 1
  if player_1_score >= score_to_win:
    text3.config(text='Player 1\n Wins!')
    play_again.grid(row=2,column=1)

  elif player_2_score >= score_to_win:
    text3.config(text='Player 2\n Wins!')
    play_again.grid(row=2,column=1)

  else:
    global direction
    velocity_x = (speed_intvar.get() * math.cos(direction))/6 
    velocity_y = (speed_intvar.get() * math.sin(direction))/6 
    canvas.move(circle_item, velocity_x, velocity_y)
    x1, y1, x2, y2 = canvas.coords(circle_item)
    x3, y3, x4, y4 = canvas.coords(player_2)
    x5, y5, x6, y6 = canvas.coords(player_1)
    if X%R.randint(200,300) == 0 and p2bot_toggle.get() == 1:
      canvas.move(player_2, 0, (y1-y3)-R.randint(0,100))

    if X%R.randint(200,300) == 0 and p1bot_toggle.get() == 1:
      canvas.move(player_1, 0, (y1-y5)-R.randint(0,100))

    if int(x2)==int(x3) and int(y3)<int(y1) and int(y2)<int(y4):
      direction = 2*direction
      color_change()

    if int(x1)==int(x6) and int(y5)<int(y1) and int(y2)<int(y6):
      direction = direction+180
      color_change()

    if x2>canvas.winfo_width():
      player_1_score += 1
      text.configure(text='P1 Score :\n' + str(player_1_score))
      direction = R.choice(direction_list)
      canvas.move(circle_item, -300, 300-y1)
    elif x1<0:
      player_2_score += 1 
      text2.configure(text='P2 Score :\n' + str(player_2_score))
      canvas.move(circle_item, 300, 300-y1)

    if y2>canvas.winfo_height() or y1<0: 
      direction = -direction
      color_change()
  
    canvas.after(1, animate)

#Player nonsense

def callback(event):
  canvas.focus_set()

def p1_up(event):
  p1x1, p1y1, p1x2, p1y2 = canvas.coords(player_1)
  if p1y1 > 10:
    canvas.move(player_1, 0, -25)

def p1_down(event):
  p1x1, p1y1, p1x2, p1y2 = canvas.coords(player_1)
  if p1y2 < 590:
    canvas.move(player_1, 0, 25)

def p2_up(event):
  p2x1, p2y1, p2x2, p2y2 = canvas.coords(player_2)
  if p2y1 > 10:
    canvas.move(player_2, 0, -25)

def p2_down(event):
  p2x1, p2y1, p2x2, p2y2 = canvas.coords(player_2)
  if p2y2 < 590:
    canvas.move(player_2, 0, 25)

canvas.bind("<Button-1>", callback) 
canvas.bind("w", p1_up)
canvas.bind("s", p1_down)
canvas.bind("<Up>", p2_up)
canvas.bind("<Down>", p2_down)

animate()

root.title("Bong!")
root.mainloop()