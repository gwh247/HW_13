import tkinter 
import tkinter.messagebox

class PizzaGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Order')

        self.place_frame = tkinter.Frame(self.main_window)
        self.toppings_frame = tkinter.Frame(self.main_window)
        self.size_frame = tkinter.Frame(self.main_window)
        self.crust_frame = tkinter.Frame(self.main_window)
        self.name_frame = tkinter.Frame(self.main_window)
        self.buton_frames = tkinter.Frame(self.main_window)
        self.pizza_size = tkinter.Frame(self.main_window)


        ##label

        ##place window
        self.place = tkinter.Label(self.place_frame,text='Thank you for choosing Pappa Johns!')
        self.place.pack(side='left')
        self.place_frame.pack(side='top')

        ##size frame 
        self.size_label = tkinter.Label(self.pizza_size,text='Choose your size', font=('Comic Sans',8, 'bold'),fg= 'green')
        #radio Butons
        self.radio_var1 = tkinter.IntVar()
        self.rb4 = tkinter.Radiobutton(self.pizza_size,text='10 inch', variable= self.radio_var1, value=0)
        self.rb5 = tkinter.Radiobutton(self.pizza_size,text='16 inch', variable = self.radio_var1, value=5)
        self.rb6 = tkinter.Radiobutton(self.pizza_size,text='18 inch', variable = self.radio_var1,value=6)

        self.size_label.pack()
        self.rb4.select()
        self.rb4.pack(side='left')
        self.rb5.pack(side='left')
        self.rb6.pack(side='left')
        self.pizza_size.pack()

        #crust size 
        self.crust_label = tkinter.Label(self.crust_frame,text='Choose your crust', font=('Comic Sans',8, 'bold'),fg= 'green')
        #radio Butons
        self.radio_var = tkinter.IntVar()
        self.rb1 = tkinter.Radiobutton(self.crust_frame,text='Regular', variable= self.radio_var, value=0)
        self.rb2 = tkinter.Radiobutton(self.crust_frame,text='Stuffed Crust', variable = self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.crust_frame,text='Garlic Crust', variable = self.radio_var,value=3)

        self.crust_label.pack()
        self.rb1.select()
        self.rb1.pack(side='left')
        self.rb2.pack(side='left')
        self.rb3.pack(side='left')
        self.crust_frame.pack()
        

        

        #toppings frame
        self.toppings1 = tkinter.Label(self.toppings_frame,text ='Choose toppings',font=('Comic Sans',8, 'bold'),fg= 'green')
        #check boxes 
        self.sausage_val = tkinter.IntVar()
        self.peperroni_val = tkinter.IntVar()
        self.onion_val = tkinter.IntVar()
        self.bacon_val = tkinter.IntVar()
        self.mushroom_val = tkinter.IntVar()

        self.sausage = tkinter.Checkbutton(self.toppings_frame,text='Sausage',variable=self.sausage_val)
        self.pepperroni = tkinter.Checkbutton(self.toppings_frame,text='Pepperoni',variable=self.peperroni_val)
        self.onion = tkinter.Checkbutton(self.toppings_frame,text='Onion',variable =self.onion_val)
        self.mushroom = tkinter.Checkbutton(self.toppings_frame,text='Mushroom',variable =self.mushroom_val)
        self.bacon = tkinter.Checkbutton(self.toppings_frame,text='Bacon',variable =self.bacon_val)
        
        #pack
        self.toppings1.pack()
        self.sausage.pack(side='left')
        self.pepperroni.pack(side='left')
        self.onion.pack(side='left')
        self.mushroom.pack(side='left')
        self.bacon.pack(side='left')

        self.toppings_frame.pack()
      

       
        
        
        


        #name frame 

        self.name_label = tkinter.Label(self.name_frame,text ='Please enter your name: ', font=('Times New Roman',10, 'bold'))
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
                total += 1
        if self.peperroni_val.get() ==1:
                total += 1 
        if self.onion_val.get() ==1:
                total += 1 
        if self.bacon_val.get() ==1:
                total += 1
        if self.mushroom_val.get() ==1:
                total += 1 
        total += self.radio_var.get()
        total += self.radio_var1.get()

        Customer_name = str(self.name_entry.get())
        
        
        tkinter.messagebox.showinfo('Total', "thank you: " + Customer_name +" your total is " + str(total))
        tkinter.mainloop()
        



pizza = PizzaGui()
