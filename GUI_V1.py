import tkinter as tk
import tkinter.messagebox
# Git bash cd command cd c:/Users/mengi/OneDrive/Desktop/Car_Inventory_Proj

# in general looks could be better. But they are secondary
# defining list that will hold entry results
entryList = list()
# why not make separate lists for each entry point


class myGui:
    def __init__(self):
        self.window1 = tk.Tk() #creates first prompt page
        self.window1.geometry("500x100") #width x height
        self.window1.title("How many items")

        self.label_1 = tk.Label(
            self.window1, text="How many items do you want to add to inventory?"
        )
        self.entry_1 = tk.Entry(self.window1)
        self.button_1 = tk.Button(
            self.window1, text="Submit", command=self.createEntries #calls the create etnries method. But why is it self.createEntries instead of createEntries only. prolly because if not it would look for a method unrelated to the instance created. self. makes sure it runs the method in the class definition being referenced. 
        )
        self.label_1.pack(side="left")
        self.entry_1.pack(side="left")
        self.button_1.pack(side="bottom")

        tk.mainloop()

    def createEntries(self):
        num = int(self.entry_1.get()) #gets the value entered

        self.window1.destroy() #closes window1

        self.window2 = tk.Tk()
        self.window2.title("Inventory Editor")
        self.window2.geometry("300x200")

        self.label_2 = tk.Label(self.window2, text="Add Cars Here")
        self.label_2.pack() #Put Entry ns in their own frame. Withing each car Entry there should be 4 entry widgets: branc, model, year, MPG

        accum = 1 #indicator or counter

        for numb in range(num): #creates the amount of entries user wants
            self.container = tk.Frame(self.window2)
            self.container.pack()
            self.label = tk.Label(self.container, text=f"Entry {accum}")
            self.label.pack()

            # 4 entry points. You should do grid here
            self.txt_label_1 = tk.Label(self.container, text="Brand")
            self.txt_1 = tk.Entry(self.container)
            self.txt_label_1.pack()
            self.txt_1.pack()
            self.txt_label_2 = tk.Label(self.container, text="Model")
            self.txt_2 = tk.Entry(self.container)
            self.txt_label_2.pack()
            self.txt_2.pack()
            self.txt_label_3 = tk.Label(self.container, text="Year")
            self.txt_3 = tk.Entry(self.container)
            self.txt_label_3.pack()
            self.txt_3.pack()
            self.txt_label_4 = tk.Label(self.container, text="MPG")
            self.txt_4 = tk.Entry(self.container)
            self.txt_label_4.pack()
            self.txt_4.pack()

            accum += 1

        self.button_2 = tk.Button(
            self.window2, text="Submit", command=self.dispEntry)
        self.button_2.pack()    
        tk.mainloop()

    def dispEntry(self):
        # not showing in permanent text. it is editable
        # Use messagebox here
        self.window2.destroy()

        # for loop that fetches the entered items. Runs num times
        self.window3 = tk.Tk()
        self.window3.geometry("200x200")
        self.window3.title = "Entry results"
        self.txt = tk.Text() #find a better widget to hold text. Permanent text.
        self.txt.insert(tk.END, f"{entryList}") #currently just displays ['','',...]. (That's cus the list is empty) 
        self.txt.pack()

        tk.mainloop()

mygui = myGui()
