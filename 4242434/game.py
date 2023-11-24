import tkinter as tk
import random
import json
from settings import *

with open ('cards.json', encoding= 'utf-8') as f:
    cards = json.load(f)

def click1():
    if len(hand) == 0:
        hand.append(random.choice(list(cards.keys())))
    hand.append(random.choice(list(cards.keys())))
    button_1['text'] = 'Добавить карту'
    score = 0
    text = ''
    for i in hand:
         python_image.configure(file='doomgame.png')
         label_2.configure(bg= COLOR_4, fg=COLOR_7)
         score += cards[i]
         text += i + ' '
         label_2['text']= text
         label_4['text']= score
    if score == 21:
        hand.clear()
        python_image.configure(file='doomwin.png')
        label_2.configure(bg=COLOR_7, fg=COLOR_5)
        label_2['text'] = text + "Победа. У вас ровно 21"
    elif score > 21:
        hand.clear()
        python_image.configure(file='doomloose.png')
        label_2.configure(fg=COLOR_2)
        label_2['text'] = text + "Вы проиграли"
    print(score, hand, text)

def click2():
    button_1['text'] = 'Новая игра'
    hand.clear()
    label_2['text'] = "У вас нет карт"
    print(hand)

 

win = tk.Tk()
win.title("Сами пишите ")
win.geometry(f"{400}x{500}")
win.resizable(0, 0)



hand = []


button_1 = tk.Button(text="Новая игра", command=lambda: click1(), font = FONT_1)
button_1.pack()

button_2 = tk.Button(text="Сбросить руку", command=lambda: click2(), font = FONT_1)
button_2.pack()

label_1 = tk.Label(text="Карты", font = FONT_1)
label_1.pack()


label_2 = tk.Label(text="У вас нет карт", font = FONT_1)
label_2.pack()


label_3 = tk.Label(text="Очки", font = FONT_1)
label_3.pack()

label_4 = tk.Label(text="0", font = FONT_1)
label_4.pack()

python_image = tk.PhotoImage(file='doomgame.png')
tk.Label(image=python_image).pack()

win.mainloop()
