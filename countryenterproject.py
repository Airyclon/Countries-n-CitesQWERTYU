from tkinter import *
import random
root = Tk()

root.title("Countries & City!")
root.geometry("500x500")

enter_country = Entry(root)
enter_country.place(relx = 0.5, rely = 0.2, anchor = CENTER)
enter_capital = Entry(root)
enter_capital.place(relx = 0.5, rely = 0.3, anchor = CENTER)

instructions = Label(root, text = "Write your Country & City!")
countrylist = Label(root)
capitallist = Label(root)
random_number_label = Label(root)
random_number_label2 = Label(root)
country = Label(root)
capital = Label(root)
chosencountry = Label(root)
chosencapital = Label(root)

list1 = []
list2 = []

def addcountry():
    country = enter_country.get()
    list1.append(country)
    countrylist["text"] = "Ur Country List- " + str(list1)
    capital = enter_capital.get()
    list2.append(capital)
    capitallist["text"] = "Ur City List- " + str(list2)

def random_number_country():
    length = len(list1)
    random_no = random.randint(0, length-1)
    random_number_label["text"] = str(random_no)
    generated_random_number = list1[random_no]
    chosencountry["text"] = "ur country is- " + str(generated_random_number)
    length2 = len(list2)
    random_no2 = random.randint(0, length2-1)
    random_number_label2["text"] = str(random_no2)
    generated_random_number2 = list2[random_no2]
    chosencapital["text"] = "ur city is- " + str(generated_random_number2)

instructions.place(relx = 0.5, rely = 0.1, anchor=CENTER)

btn = Button(root, text = "Add to Country & City list", command = addcountry)
btn.place(relx = 0.5, rely = 0.4, anchor=CENTER)

countrylist.place(relx = 0.5, rely = 0.5, anchor=CENTER)
capitallist.place(relx = 0.5, rely = 0.6, anchor=CENTER)

btn1 = Button(root, text = "Who is the lucky Country and City?", command = random_number_country)
btn1.place(relx = 0.5, rely = 0.7, anchor=CENTER)

random_number_label.place(relx = 0.4, rely = 0.7, anchor=CENTER)
random_number_label2.place(relx = 0.6, rely = 0.7, anchor=CENTER)
chosencountry.place(relx = 0.5, rely = 0.8, anchor = CENTER)
chosencapital.place(relx = 0.5, rely = 0.9, anchor = CENTER)

root.mainloop()