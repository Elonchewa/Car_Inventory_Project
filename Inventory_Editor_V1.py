# Take a car Brand name, model, make year, and MPG
# even multiple models of the same brand
# adds the data to a file called Car Inventory

import sqlite3
import tkinter as tk


class myGui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("How many items")

        self.label_1 = tk.Label(
            self.window, text="How many items do you want to add to inventory?"
        )
        self.entry_1 = tk.Entry(self.window)
        self.button_1 = tk.Button(
            self.window, text="Submit", command=self.createEntries
        )
        self.label_1.pack(side="left")
        self.entry_1.pack(side="left")
        self.button_1.pack()

        tk.mainloop()

    def createEntries(self):
        num = int(self.entry_1.get())

        self.window.destroy()

        self.window2 = tk.Tk()
        self.window2.title("Inventory Editor")
        self.window2.geometry("300x200")

        self.label_2 = tk.Label(self.window2, text="Add inventory Here")
        self.label_2.pack()

        entryList = list()
        labelList = list()
        ind = 1

        first = 1
        for numb in range(num):
            self.label = tk.Label(self.window2, text=f"Entry {ind}")
            self.label.pack()
            self.item = tk.Entry(self.window2)
            self.item.pack()
            ind += 1


class Car:
    def __init__(self, brand, model, year, mpg):
        self.brand = brand
        self.model = model
        self.year = year
        self.mpg = mpg


def askCar():
    brand = input("Input brand of car.")
    model = input("Input model of car.")
    year = input("Input year of car.")
    mpg = input("Input mpg of car.")

    return brand, model, year, mpg


def inp_doc(list):
    inventory = open("Car Inventory.txt", "a")
    inventory.write("\n")
    for row in list:
        for col in range(len(row)):
            w = str(row[col])
            inventory.write(f"{w} \t")
        inventory.write("\n")
    inventory.close()


inv_list = []

reps = int(input("How many cars would you like to enter into inventory?"))
for num in range(reps):
    inner_list = []
    for num in range(1):
        brand = input("Input brand of car.")
        model = input("Input model of car.")
        year = input("Input year of car.")
        mpg = input("Input mpg of car.")
        car = Car(brand, model, year, mpg)
        inner_list.append(car.brand)
        inner_list.append(car.model)
        inner_list.append(car.year)
        inner_list.append(car.mpg)
    inv_list.append(inner_list)

inp_doc(inv_list)
