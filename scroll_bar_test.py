import tkinter as tk
import tkinter.messagebox

# Git bash cd command cd c:/Users/mengi/OneDrive/Desktop/Car_Inventory_Proj

# in general looks could be better. But they are secondary
# defining list that will hold entry results
entryList = list()
# why not make separate lists for each entry point


class myGui:
    def __init__(self):
        self.window1 = tk.Tk()  # creates first prompt page
        self.window1.geometry("500x100")  # width x height
        self.window1.title("How many items")

        self.label_1 = tk.Label(
            self.window1, text="How many items do you want to add to inventory?"
        )
        self.entry_1 = tk.Entry(self.window1)
        self.button_1 = tk.Button(
            self.window1,
            text="Submit",
            command=self.createEntries,  # calls the create etnries method. But why is it self.createEntries instead of createEntries only. prolly because if not it would look for a method unrelated to the instance created. self. makes sure it runs the method in the class definition being referenced.
        )
        self.label_1.pack(side="left")
        self.entry_1.pack(side="left")
        self.button_1.pack(side="bottom")

        tk.mainloop()

    def createEntries(self):
        num = int(self.entry_1.get())  # gets the value entered

        self.window1.destroy()  # closes window1

        self.window2 = tk.Tk()
        self.window2.title("Inventory Editor")
        self.window2.geometry("300x100")

        # self.label_2 = tk.Label(self.window2, text="Add Cars Here")
        # self.label_2.pack() #Put Entry ns in their own frame. Withing each car Entry there should be 4 entry widgets: branc, model, year, MPG

        # scroll bar define
        self.scroll_bar = tk.Scrollbar(self.window2, orient="vertical")
        self.scroll_bar.pack(side="right", fill="y")

        self.canvas = tk.Canvas(self.window2, yscrollcommand=self.scroll_bar.set)
        self.canvas.pack(side="left", fill="both", expand=True)

        # container frame
        self.container = tk.Frame(self.canvas)
        self.canvas.create_window(0, 0, anchor="nw", window=self.container)

        self.scroll_bar.config(command=self.canvas.yview)  # confugres scroll bar

        accum = 0  # indicator for row number
        counter = 1  # indicator for how long the loop must run

        ency = {}
        ency_var = 0

        while counter <= num:
            # for numb in range(num): #creates the amount of entries user wants
            # 4 entry points.
            ency[f"{ency_var}"] = f"self.txt{counter}_label_1"
            ency[f"{ency_var+1}"] = f"self.txt{counter}_label_2"
            ency[f"{ency_var+2}"] = f"self.txt{counter}_label_3"
            ency[f"{ency_var+3}"] = f"self.txt{counter}_label_4"
            ency[f"{ency_var+4}"] = f"self.txt{counter}_1"
            ency[f"{ency_var+5}"] = f"self.txt{counter}_2"
            ency[f"{ency_var+6}"] = f"self.txt{counter}_3"
            ency[f"{ency_var+7}"] = f"self.txt{counter}_4"

            self.entry_indicator = tk.Label(self.container, text=f"Entry {counter}")
            self.entry_indicator.grid(row=accum, column=1, sticky="w")
            ency[f"{ency_var}"] = tk.Label(self.container, text="Brand")
            ency[f"{ency_var}"].grid(row=accum + 1, column=0, sticky="w")
            ency[f"{ency_var+1}"] = tk.Label(self.container, text="Model")
            ency[f"{ency_var+1}"].grid(row=accum + 1, column=1, sticky="w")
            ency[f"{ency_var+2}"] = tk.Label(self.container, text="Year")
            ency[f"{ency_var+2}"].grid(row=accum + 1, column=2, sticky="w")
            ency[f"{ency_var+3}"] = tk.Label(self.container, text="MPG")
            ency[f"{ency_var+3}"].grid(row=accum + 1, column=3, sticky="w")

            ency[f"{ency_var+4}"] = tk.Entry(self.container)
            ency[f"{ency_var+4}"].grid(row=accum + 2, column=0)
            ency[f"{ency_var+5}"] = tk.Entry(self.container)
            ency[f"{ency_var+5}"].grid(row=accum + 2, column=1)
            ency[f"{ency_var+6}"] = tk.Entry(self.container)
            ency[f"{ency_var+6}"].grid(row=accum + 2, column=2)
            ency[f"{ency_var+7}"] = tk.Entry(self.container)
            ency[f"{ency_var+7}"].grid(row=accum + 2, column=3)

            # we need to change the attribute names here or find ways to make them change. Because all corresponding entry points have the same variable. It would produce conflict

            accum += 3
            counter += 1
            ency_var +=8

        self.button_2 = tk.Button(self.canvas, text="Submit", command=self.dispEntry)
        self.button_2.pack()

        self.container.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        tk.mainloop()

    def dispEntry(self):

        # not showing in permanent text. it is editable
        # Use messagebox here
        self.window2.destroy()

        # for loop that fetches the entered items. Runs num times
        self.window3 = tk.Tk()
        self.window3.geometry("200x200")
        self.window3.title = "Entry results"

        # self.txt = tk.Text() #find a better widget to hold text. Permanent text.
        # self.txt.insert(tk.END, f"{entryList}") #currently just displays ['','',...]. (That's cus the list is empty)
        # self.txt.pack()
        # give them a display of all they entered and a question of are you sure you want to enter... into the database. Then have Submit or Edit Entry buttons.
        tk.mainloop()


mygui = myGui()
