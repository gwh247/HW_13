import tkinter 
import tkinter.messagebox

class PizzaGui:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.place_frame = tkinter.Frame(self.main_window)
        self.toppings_frame = tkinter.Frame(self.main_window)
        self.size_frame = tkinter.Frame(self.main_window)
        self.crust_frame = tkinter.Frame(self.main_window)
        self.name_frame = tkinter.Frame(self.main_window)
        self.buton_frames = tkinter.Frame(self.main_window)


        ##label

        ##place window
        self.place = tkinter.Label(self.place_frame,text='Pappa Johns')
        self.place.pack(side='top')
        self.place_frame.pack(side='top')
        

        #toppings frame
        self.toppings1 = tkinter.Label(self.toppings_frame,text ='Choose toppings')
        #check boxes 
        self.sausage_val = tkinter.IntVar()
        self.peperroni_val = tkinter.IntVar()
        self.onion_val = tkinter.IntVar()

        self.sausage = tkinter.Checkbutton(self.toppings_frame,text='sausage',variable=self.sausage_val)
        self.pepperroni = tkinter.Checkbutton(self.toppings_frame,text='pepperoni',variable=self.peperroni_val)
        self.onion = tkinter.Checkbutton(self.toppings_frame,text='Onion',variable =self.onion_val)
        #pack
        self.toppings1.pack()
        self.sausage.pack(side='left')
        self.pepperroni.pack(side='left')
        self.onion.pack(side='left')

        self.toppings_frame.pack()

        #crust frame
        self.crust_frame = tkinter.Tk() 

        self.crust_label = tkinter.Label(self.crust_frame,text='crust')
        #radio Butons
        self.radio_var = tkinter.IntVar()
        self.rb1 = tkinter.Radiobutton(self.crust_frame,text='regular', variable= self.radio_var, value=0)
        self.rb2 = tkinter.Radiobutton(self.crust_frame,text='Cheesy Crust', variable = self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.crust_frame,text='garlic Crust', variable = self.radio_var,value=3)

        self.crust_label.pack()
        self.rb1.select()
        self.rb1.pack(side='left')
        self.rb2.pack(side='left')
        self.rb3.pack(side='left')
        self.crust_frame.pack()
        
        
        


        #name frame 

        self.name_label = tkinter.Label(self.name_frame,text ='Name')
        self.name_entry = tkinter.Entry(self.name_frame,width=15)
        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')
        self.name_frame.pack(side='top')
        #button frame 

        self.calc_button = tkinter.Button(self.buton_frames,text='Calculate Order',command=self.total_cost)
        self.quit_button = tkinter.Button(self.buton_frames, text='Quit', command=self.main_window.destroy)
        #pack
        self.calc_button.pack(side='right')
        self.quit_button.pack(side='left')
        self.buton_frames.pack()
        
       
        tkinter.mainloop()


    def total_cost(self):
        message = "your total is: "
        total = 0

        if self.sausage_val.get() ==1:
                total += 2
        if self.peperroni_val.get() ==1:
                total += 2 
        if self.onion_val.get() ==1:
                total += 2 
        tkinter.messagebox.showinfo('Total', "your total is " + str(total))
        tkinter.mainloop()



pizza = PizzaGui()
