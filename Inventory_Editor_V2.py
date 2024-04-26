import tkinter as tk
import tkinter.messagebox
import sqlite3

# Git bash cd command cd c:/Users/mengi/OneDrive/Desktop/Car_Inventory_Proj

# in general looks could be better. But they are secondary


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
            command=lambda: self.createEntries(),  # calls the create etnries method.
        )
        self.label_1.pack(side="left")
        self.entry_1.pack(side="left")
        self.button_1.pack(side="bottom")

        tk.mainloop()

    def createEntries(self):
        num = int(self.entry_1.get())# gets the value entered. The number of entry sections

        if self.window1.winfo_exists()==1:# closes window1
            self.window1.destroy()

        self.window2 = tk.Tk()
        self.window2.title("Inventory Editor")
        self.window2.geometry("500x100")

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

        ency = {} #dictionary to dynamically hold the entries. Ency just means encyclopedia
        ency_var = 0 #number for the key of the dictionary

        while counter <= num:
            # creates the amount of entry sections user wants
            # 4 entry points.
            

            self.entry_indicator = tk.Label(self.container, text=f"Entry {counter}")
            self.entry_indicator.grid(row=accum, column=1, sticky="w")
            
            #first key for ency is '0'
            ency[f"{ency_var}"] = tk.Label(self.container, text="Brand")
            ency[f"{ency_var}"].grid(row=accum + 1, column=0, sticky="w")
            ency[f"{ency_var+1}"] = tk.Label(self.container, text="Model")
            ency[f"{ency_var+1}"].grid(row=accum + 1, column=1, sticky="w")
            ency[f"{ency_var+2}"] = tk.Label(self.container, text="Year")
            ency[f"{ency_var+2}"].grid(row=accum + 1, column=2, sticky="w")
            ency[f"{ency_var+3}"] = tk.Label(self.container, text="MPG")
            ency[f"{ency_var+3}"].grid(row=accum + 1, column=3, sticky="w")

            #entry points start at ency_var+4 which is 4, goes to 7, and adds 4 to loop back around to the second entry section
            ency[f"{ency_var+4}"] = tk.Entry(self.container)
            ency[f"{ency_var+4}"].grid(row=accum + 2, column=0)
            ency[f"{ency_var+5}"] = tk.Entry(self.container)
            ency[f"{ency_var+5}"].grid(row=accum + 2, column=1)
            ency[f"{ency_var+6}"] = tk.Entry(self.container)
            ency[f"{ency_var+6}"].grid(row=accum + 2, column=2)
            ency[f"{ency_var+7}"] = tk.Entry(self.container)
            ency[f"{ency_var+7}"].grid(row=accum + 2, column=3)

            accum += 3
            counter += 1
            ency_var += 8  # This is to start another cycle
            # after every iteration, all the key-value pairs will be added to ency dictionary.
        
        self.button_2 = tk.Button(
            self.canvas, text="Submit", command=lambda: self.dispEntry(ency, num)
        )
        self.button_2.pack()

        self.container.update_idletasks()  # waits for the creation loop to finish and adds all the entries and labels to the container
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        tk.mainloop()

    def dispEntry(self, ency, num): #this method is ALSO for debugging
        data_list = [] #will be a two dimensional list to group different entry sections
        ency_var = 4  # dictionary key value
        data_list_index = 0
        print(ency['4'])
        # we have 8 elements per entry section: 4 labels and 4 entry points. The entry points are what we are targeting.
        
        # the number of entry sections is the amout of times this loop will run (user inputed it at the beginning)
        for number in range(num):  
            data_list.append([])
            for numb in range(4):
                # adds the Inventory items into a list. For first entry section, for example, ency 4, 5, 6, and 7 are gotten. Then for the next section we start at ency 12
                data_list[data_list_index].append(ency[f"{ency_var}"].get())  
                ency_var += 1
            ency_var += 4  # since 1 is already added to counter after the end of the inner loop we just add 4 here
            data_list_index += 1 #add 1 to make sure data_list has more sub lists added
        
        self.messagebox = tkinter.messagebox.askyesno("Are these correct", f'{data_list}')
        
        # added an if statement to createEntries to handle if User wants to return to entry page in case of error
        if self.messagebox is False:
            self.window2.destroy()
            self.__init__() #runs everything from scratch
            
        else:
            self.window2.destroy()
            #now we start process of adding items to database.
            self.addDb(data_list, num)
            print(data_list)
            
    def addDb(self, data_list, num):
        connection = sqlite3.connect('Inventory.db')
        cursor = connection.cursor()
        table = '''CREATE TABLE IF NOT EXISTS Inventory (
                                    Id INTEGER PRIMARY KEY,
                                    Brand TEXT NOT NULL,
                                    Model TEXT NOT NULL,
                                    Year INTEGER NOT NULL,
                                    Mpg REAL)'''
        cursor.execute(table)
        
        #iterates through the sub-lists of data_list and inputs them into their respective columns
        for data in data_list:
            cursor.execute('INSERT INTO Inventory (Brand, Model, Year, Mpg) VALUES (?,?,?,?)', (data[0],data[1],data[2],data[3]))

        #end commands to close cursor and connection
        cursor.close()
        connection.commit()
        connection.close()
        

mygui = myGui()
