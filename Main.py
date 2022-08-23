from this import d
import tkinter as tk
from tkinter import filedialog
from win10toast import ToastNotifier
import sys
from tkinter import *
import random
import os

class Main:
    classno = {}
    
    def __init__(self):
        # self.textbook()
        # self.ClassNotes()
        # self.VideoLecture()
        # self.printdetails()
        print("hello")
        
        
    def textbook(self):
        toaster.show_toast("RPAISlate Software Admin", "Please Choose Folder Where TextBook Are Stored", threaded=True,icon_path=None, duration=4)  # 3 seconds
        path_file = filedialog.askdirectory()
        textb = {'TextBook' : path_file}
        self.classno.update(textb)

    def VideoLecture(self):
        toaster.show_toast("RPAISlate Software Admin", "Please Choose Folder Where VideoLecture Are Stored", threaded=True,icon_path=None, duration=4)
        path_file = filedialog.askdirectory()
        textb = {'VideLecture' : path_file}
        self.classno.update(textb)
    
    def ClassNotes(self):
        toaster.show_toast("RPAISlate Software Admin", "Please Choose Folder Where ClassNotes Are Stored", threaded=True,icon_path=None, duration=4)
        path_file = filedialog.askdirectory()
        textb = {'ClassNotes' : path_file}
        self.classno.update(textb)

    def printdetails(self):
        print(self.classno)
        
    def Exit():
        sys.exit()


    def texttojsonconverter(self):
        list_of_txt_file = ["./readme.txt"]
        for ele in list_of_txt_file:
            base = os.path.splitext(ele)[0]
            os.rename(ele, base + '.json')
        # engine = pyttsx3.init()
        # engine.say("ALl Details Saved Succesfully Thank You For Using RPAISlate's Detail Updater")
        # engine.runAndWait()
        sys.exit(0)

    
    #-----------------------------------------------------------------------------#
    def write_details(self):
        # lines = ['RPAISlate', 'Storing the data in the text file']
        f = open('readme.txt', 'r+')
        temp = f.readlines()
        if (len(temp) == 0):
            f.write("\n{\n")
            f.write("\t{")
            f.write("\n\t\t \"Employee Id\""+ ": "+ teachers_id.get()+","+"\n")
            f.write("\t\t \"Teacher's Designation\"" + ": \"" + teachers_designation.get()+"\","+"\n")
            f.write("\t\t \"Username\"" + ": \"" + user_name.get()+"\","+"\n")
            f.write("\t\t \"User Password\"" + ":\"" + user_password.get()+"\","+"\n")  
            f.write("\t}")#replaced by niche walla code         
            f.write("\n}")
        else:
            lines = f.readlines()
            # move file pointer to the beginning of a file
            f.seek(0)
            # truncate the file
            f.truncate()

            # start writing lines except the first line
            # lines[1:] from line 2 to last line
            print(temp)
            f.writelines(temp[:-2])
            f.write("\t},")
            f.write("\n\t{")
            f.write("\n\t\t \"Employee Id\""+ ": "+ teachers_id.get()+","+"\n")
            f.write("\t\t \"Teacher's Designation\"" + ": \"" + teachers_designation.get()+"\","+"\n")
            f.write("\t\t \"Username\"" + ": \"" + user_name.get()+"\","+"\n")
            f.write("\t\t \"User Password\"" + ":\"" + user_password.get()+"\","+"\n")  
            f.write("\t}")#replaced by niche walla code         
            f.write("\n}")

    #-----------------------------------------------------------------------------#

def call():
    
    if(len(user_name.get()) < 0):
        print("Empty")
    else:
        print(user_name.get())
    obj = Main()
    obj.write_details()
    obj.texttojsonconverter()

def pin_generator():

    pin = random.sample(range(10), 4)
    #print (pin)
    
    global merged_list
    merged_list = ""
    for ele in pin:
        merged_list += str(ele)
    print(merged_list)

 

if __name__ == "__main__" :    
    root = tk.Tk()
    win = Tk()
    toaster = ToastNotifier()
    root.withdraw()
    obj = Main()
    
    
    #tk.Entry(root).pack()
    
    ##GUI
    titl = tk.Label(win, bg="black", relief="flat", bd=10, font=("arial", 35))
    titl.pack(fill=X)

    title1=tk.Label(win, text = "Enter", bg = "black", fg = "dark orange", font=("arial", 27),borderwidth=0)
    title1.place(x=115,y=12)

    title2=tk.Label(win, text = "your", bg = "black", fg = "white", font=("arial", 27),borderwidth=0)
    title2.place(x=212,y=12)

    title3=tk.Label(win, text = "Details", bg = "black", fg = "green", font=("arial", 27),borderwidth=0)
    title3.place(x=290,y=12)

    #Set the geometry of Tkinter frame

    #------- J's edit later------------#
    # width,height=autopy.screen.size()
    win.geometry("500x500")
    # win.pack_propagate(0)
    win.resizable(0, 0)

    #Create an Entry widget to accept User Input
    #------- J's edit------------#
    user_name = tk.Label(
        win,
        text="User Name",
        width=13,
        height=2,
        bd=5,
        # relief=RIDGE,
        font=("times new roman", 12),
        bg="black",
        fg="green",
        borderwidth=0,

    )
    user_name.place(x=50, y=250)

    user_name= Entry(win,
            width=15,
            bd=5,
            validate="key",
            bg="grey",
            fg="white",
            # relief=RIDGE,
            font=("times", 25, "bold"),
            borderwidth=1,
            relief="groove")
    user_name.focus_set()
    user_name.place(x=200,y=250)

    user_password = tk.Label(
        win,
        text="User Pin",
        width=13,
        height=2,
        bd=5,
        # relief=RIDGE,
        font=("times new roman", 12),
        bg="black",
        fg="green",
        borderwidth=0,

    )
    user_password.place(x=50, y=300)

    user_password= Entry(win,
            width=11,
            bd=5,
            validate="key",
            bg="grey",
            fg="white",
            # relief=RIDGE,
            font=("times", 25, "bold"),
            borderwidth=1,
            relief="groove")
    user_password.focus_set()
    user_password.place(x=200,y=300)

    #To create a submit button for random pin

    #-----------------------------------------------------------------------------#
    #tk.Entry(root).pack()
    # tk.Label(root, text=" ").pack()

#     button_border = tk.Frame(root, highlightbackground = "black", 
#                             highlightthickness = 2, bd=0)
#     button_border.pack()
    #-----------------------------------------------------------------------------#
    random_pin = tk.Button(
            win,
            #button_border,
            text="Random Pin",
            command=pin_generator,
            bd=11,
            font=("times new roman", 12),
            bg="white",
            fg="black",
            height=0,
            width=8,
            # relief=RIDGE,
            borderwidth=6
        )

    random_pin.place(x=370, y=300)
    

    ##For Inputing Class Teachers Designation
    teachers_designation = tk.Label(
        win,
        text="Designation",
        width=13,
        height=2,
        bd=5,
        # relief=RIDGE,
        font=("times new roman", 12),
        bg="black",
        fg="green",
        borderwidth=0,

    )
    teachers_designation.place(x=50, y=200)

    teachers_designation =  Entry(win,
            width=15,
            bd=5,
            validate="key",
            bg="grey",
            fg="white",
            # relief=RIDGE,
            font=("times", 25, "bold"),
            borderwidth=1,
            relief="groove")
    teachers_designation.focus_set()
    teachers_designation.place(x=200,y=200)

    teachers_id = tk.Label(
        win,
        text="Teacher Id",
        width=13,
        height=2,
        bd=5,
        # relief=RIDGE,
        font=("times new roman", 12),
        bg="black",
        fg="green",
        borderwidth=0,

    )
    teachers_id.place(x=50, y=150)

    teachers_id =  Entry(win,
            width=15,
            bd=5,
            validate="key",
            bg="grey",
            fg="white",
            # relief=RIDGE,
            font=("times", 25, "bold"),
            borderwidth=1,
            relief="groove")
    teachers_id.focus_set()
    teachers_id.place(x=200,y=150)
    
    var =""
    if user_password.get():
        var = merged_list
    else:
        var = user_password.get()


    notify = tk.Label(
        win,
        text="Random generated pin",
        bg = "light grey",
        fg= "black", 
        width= 18,
        height= 0,
        bd=5,
        font=("times", 12, "bold"),
        borderwidth=1,
        relief="groove"
     )

    notify.place(x=290, y=350)


    #Create a Button to validate Entry Widget

    submit = tk.Button(
            win,
            text="Submit",
            command=call,
            bd=10,
            font=("times new roman", 18),
            bg="black",
            fg="red",
            height=0,
            width=10,
            # relief=RIDGE,
            borderwidth=0
        )
    submit.place(x=290, y=400)
    
    
    exit = tk.Button(
            win,
            text="Exit",
            command= quit,
            bd=10,
            font=("times new roman", 18),
            bg="black",
            fg="red",
            height=0,
            width=10,
            # relief=RIDGE,
            borderwidth=0
        )
    exit.place(x=90, y=400)


    win.mainloop()
