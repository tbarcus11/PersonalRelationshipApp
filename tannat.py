'''
Author: Tanner Barcus
Created: 12/22/2022
Purpose: Creating a tkinter app to present images and captions through different seaons and eras of my relationship (I know its cringy/corny).
'''
from tkinter import *       #importing tkinter gui
from PIL import ImageTk, Image      #importing pillow for images

'''Creating the main class for my window'''

class Tannat:
    def __init__(self):
        self.window = Tk()      # self.window becomes the entire base

    def start(self):        # start function that gets called in driver, sets up start page when loading up app.

        self.window.geometry("1000x600")        # basics of the window like size, title, and logo
        self.window.title("Tan Y Nat")
        self.window.config(bg="#e797e8")
        heart = PhotoImage(file="***")
        self.window.iconphoto(True, heart)
        self.window.iconbitmap(r"***")

        logo = PhotoImage(file="***")       # created side logo photoimage for tkinter to use
        leftlabel = Label(self.window, image=logo, bg="#e797e8")        # label that tkinter uses
        leftlabel.image = logo
        leftlabel.place(x=50, y=50)

        logo2 = PhotoImage(file="***")      # other logo used for instructions
        rightlabel = Label(self.window, image=logo2, bg="#e797e8")
        rightlabel.image = logo2
        rightlabel.place(x=675, y=120)

        start_p = Image.open("***")     # middle image used every reset
        rs_start_p = start_p.resize((294, 392))     # resizing using Pillow library
        start_image = ImageTk.PhotoImage(rs_start_p)
        start_img = Label(self.window, image=start_image)
        start_img.place(x=360, y=50)

        var_szn = StringVar()       # main variable for options menu
        szns = ["-Select Season-", "Spring", "Summer", "Fall", "Winter"]        # list defined with seasons
        var_szn.set(szns[0])
        menu1 = OptionMenu(self.window, var_szn, *szns)     # tkinter options menu with list and season variable included
        menu1.place(x=200, y=500)

        var_year = StringVar()      # main varibale for options menu
        years = ["-Select Year", "2017", "2018", "2019", "2020", "2021", "2022"]        # list defined with years
        var_year.set(years[0])
        menu2 = OptionMenu(self.window, var_year, *years)       # another options menu with year list and year variable
        menu2.place(x=460, y=500)

        go_button = Button(self.window, text="Go!", command=lambda: self.go_func(var_szn, var_year, start_img, menu1, menu2, go_button, leftlabel, rightlabel))     # tkinter button including all values needed
        go_button.place(x=730, y=500)

        self.window.mainloop()      # calling main loop
    
    '''start2 is clalled after pressing the reset button. It is the exact same as "start" and has all the same properties, only it must destroy all previous labels and renew the original landing page.'''
    
    def start2(self, i1, i2, i3, t1, t2, t3, tl, rb):
        i1.destroy()
        i2.destroy()
        i3.destroy()
        t1.destroy()
        t2.destroy()
        t3.destroy()
        tl.destroy()
        rb.destroy()

        self.window.geometry("1000x600")
        self.window.title("Tan Y Nat")
        self.window.config(bg="#e797e8")
        heart = PhotoImage(file="***")
        self.window.iconphoto(True, heart)

        logo = PhotoImage(file="***")
        leftlabel = Label(self.window, image=logo, bg="#e797e8")
        leftlabel.image = logo
        leftlabel.place(x=50, y=50)

        logo2 = PhotoImage(file="***")
        rightlabel = Label(self.window, image=logo2, bg="#e797e8")
        rightlabel.image = logo2
        rightlabel.place(x=675, y=120)

        start_p = Image.open("***")
        rs_start_p = start_p.resize((294, 392))
        start_image = ImageTk.PhotoImage(rs_start_p)
        start_img = Label(self.window, image=start_image)
        start_img.place(x=360, y=50)

        var_szn = StringVar()
        szns = ["-Select Season-", "Spring", "Summer", "Fall", "Winter"]
        var_szn.set(szns[0])
        menu1 = OptionMenu(self.window, var_szn, *szns)
        menu1.place(x=200, y=500)

        var_year = StringVar()
        years = ["-Select Year", "2017", "2018", "2019", "2020", "2021", "2022"]
        var_year.set(years[0])
        menu2 = OptionMenu(self.window, var_year, *years)
        menu2.place(x=460, y=500)


        go_button = Button(self.window, text="Go!", command=lambda: self.go_func(var_szn, var_year, start_img, menu1, menu2, go_button, leftlabel, rightlabel))
        go_button.place(x=730, y=500)

        self.window.mainloop()

    '''go_func is ran when the button from start is pressed. It destroys all from the previous window and then takes both var_szn and var_year and runs from that if statement. The comments from the first section can apply to all combinations for season and year.'''
    
    def go_func(self, szn, year, s_i, men1, men2, butt, logo, logo2):
        s_i.destroy()
        men1.destroy()
        men2.destroy()
        butt.destroy()
        logo.destroy()
        logo2.destroy()

        if szn.get() == "Spring":
            if year.get() == "2017":

                self.window.title("Spring 2017")        # setting title for window

                i1_tk = PhotoImage(file="***")      # i1 - image 1 photoimage for tkinter
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")      # i2 - image 2
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")      # i3 - image 3
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")      # t1 - text 1 textbox for captions
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")      # t2 - text 2
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")      #t3 - text 3
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Spring 2017", bg="#e797e8", font="Bold", bd="7", relief="ridge")      # middle label stating season and year
                tl.place(x=442, y=280)

            elif year.get() == "2018":

                self.window.title("Spring 2018")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Spring 2018", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

            elif year.get() == "2019":

                self.window.title("Spring 2019")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Spring 2019", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

            elif year.get() == "2020":

                self.window.title("Spring 2020")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Spring 2020", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

            elif year.get() == "2021":

                self.window.title("Spring 2021")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Spring 2021", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

            elif year.get() == "2022":

                self.window.title("Spring 2022")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Spring 2022", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

        if szn.get() == "Summer":

            if year.get() == "2017":

                self.window.title("Summer 2017")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Summer 2017", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

            elif year.get() == "2018":

                self.window.title("Summer 2018")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Summer 2018", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

            elif year.get() == "2019":

                self.window.title("Summer 2019")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Summer 2019", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

            elif year.get() == "2020":

                self.window.title("Summer 2020")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Summer 2020", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

            elif year.get() == "2021":

                self.window.title("Summer 2021")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Summer 2021", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

            elif year.get() == "2022":

                self.window.title("Summer 2022")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Summer 2022", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

        if szn.get() == "Fall":

            if year.get() == "2017":

                self.window.title("Fall 2017")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Fall 2017", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

            elif year.get() == "2018":

                self.window.title("Fall 2018")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Fall 2018", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

            elif year.get() == "2019":

                self.window.title("Fall 2019")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Fall 2019", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

            elif year.get() == "2020":

                self.window.title("Fall 2020")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Fall 2020", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

            elif year.get() == "2021":

                self.window.title("Fall 2021")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Summer 2021", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

            elif year.get() == "2022":

                self.window.title("Fall 2022")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Fall 2022", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

        if szn.get() == "Winter":

            if year.get() == "2017":

                self.window.title("Winter 2017")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Winter 2017", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

            elif year.get() == "2018":

                self.window.title("Winter 2018")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Winter 2018", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

            elif year.get() == "2019":

                self.window.title("Winter 2019")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Winter 2019", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

            elif year.get() == "2020":

                self.window.title("Winter 2020")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Winter 2020", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

            elif year.get() == "2021":

                self.window.title("Winter 2021")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Winter 2021", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

            elif year.get() == "2022":

                self.window.title("Winter 2022")

                i1_tk = PhotoImage(file="***")
                i1 = Label(self.window, image=i1_tk)
                i1.image = i1_tk
                i1.place(x=50, y=50)

                i2_tk = PhotoImage(file="***")
                i2 = Label(self.window, image=i2_tk)
                i2.image = i2_tk
                i2.place(x=750, y=50)

                i3_tk = PhotoImage(file="***")
                i3 = Label(self.window, image=i3_tk)
                i3.image = i3_tk
                i3.place(x=50, y=350)

                t1 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t1.place(x=360, y=90)

                t2 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t2.place(x=770, y=420)

                t3 = Label(self.window, text="***", bg="#e797e8", font="Bold")
                t3.place(x=360, y=430)

                tl = Label(self.window, text="Winter 2022", bg="#e797e8", font="Bold", bd="7", relief="ridge")
                tl.place(x=442, y=280)

        reset = Button(self.window, text="Reset", bg="Red", command=lambda: self.start2(i1, i2, i3, t1, t2, t3, tl, reset))     #reset button that calls start 2
        reset.place(x=490, y=550)

