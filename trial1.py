import tkinter as tk
import tkinter.messagebox

entryList = list()


class myGui:
    def __init__(self):
        self.window = tk.Tk() #creates first prompt page
        self.window.geometry("500x100") #width x height
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
        self.button_1.pack(side="bottom")

        tk.mainloop()

    def createEntries(self):
        num = int(self.entry_1.get())

        self.window.destroy()

        self.window2 = tk.Tk()
        self.window2.title("Inventory Editor")
        self.window2.geometry("300x200")

        self.label_2 = tk.Label(self.window2, text="Add inventory Here")
        self.label_2.pack()
        self.button_2 = tk.Button(
            self.window2, text="Submit", command=self.dispEntry)
        self.button_2.pack()

        labelList = list() #currently unused
        ind = 1 #indicator or counter

        first = 1
        for numb in range(num): #creates the amount of entries user wants
            self.label = tk.Label(self.window2, text=f"Entry {ind}")
            self.label.pack()
            self.item = tk.Entry(self.window2) 
            self.item.pack()
            ind += 1
            entryList.append(self.item.get())
        tk.mainloop()

    def dispEntry(self):
        self.window2.destroy()

        self.window3 = tk.Tk()
        self.window3.geometry("200x200")
        self.window3.title = "Entry results"
        self.txt = tk.Text() #find a better widget to hold text. Permanent text.
        self.txt.insert(tk.END, f"{entryList}") #currently just displays ['','',...]
        self.txt.pack()

        tk.mainloop()


mygui = myGui()
