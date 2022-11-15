from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
language = ['French', 'English']
#-------------- WINDOW --------------#

window = Tk()
window.title('Flash Cards')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

#-------------- CSV --------------#

try:
    data = pandas.read_csv("files/words_to_learn.csv")
except FileNotFoundError :
    start_data = pandas.read_csv("files/french_words.csv")
    words_list = start_data.to_dict(orient="records")
except pandas.errors.EmptyDataError:
    again = messagebox.askokcancel(title='Flash Card',
                                   message='It seems you have learned all the flash cards! \nDo you want to start all over again?')
    if again:
        start_data = pandas.read_csv("files/french_words.csv")
        words_list = start_data.to_dict(orient="records")
    else:
        window.destroy()
else:
    words_list = data.to_dict(orient="records")

print(words_list)

#-------------- FUNCTIONS --------------#


def random_word(languages):
    global current_card
    try:
        current_card = random.choice(words_list)
    except IndexError:
        messagebox.showinfo(title='Flash Cards', message='Congratulations! You learned all the flash cards!')
        window.destroy()
    else:
        current_word = current_card[languages]
        canvas.itemconfig(word, text=current_word)


def flip_cards():
    canvas.itemconfig(img, image=back_img)
    canvas.itemconfig(title, fill='white')
    canvas.itemconfig(word, fill='white', text=current_card[language[1]])
    canvas.itemconfig(title, text=language[1])


def another_card():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(img, image=front_img)
    canvas.itemconfig(title, fill='black')
    canvas.itemconfig(word, fill='black', text=random_word(language[0]))
    canvas.itemconfig(title, text=language[0])
    timer = window.after(3000, flip_cards)


def correct_word():
    try:
        words_list.remove(current_card)
    except ValueError:
        messagebox.showinfo(title='Flash Cards', message='Congratulations! You learned all the flash cards!')
    else:
        to_learn = pandas.DataFrame(words_list)
        to_learn.to_csv('files/words_to_learn.csv', index=False)
        another_card()


#-------------- FRONT CARD --------------#


canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
img = canvas.create_image(400, 263, image=front_img)
title = canvas.create_text(400, 150, text=language[0], font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, text='initial error', font=('Ariel', 60, 'bold'))
canvas.grid(column=0, columnspan=2, row=0)

x_image = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, command=another_card)
x_button.grid(column=0, row=1)

y_image = PhotoImage(file="images/right.png")
y_button = Button(image=y_image, highlightthickness=0, command=correct_word)
y_button.grid(column=1, row=1)

random_word(language[0])
timer = window.after(3000, flip_cards)

window.mainloop()