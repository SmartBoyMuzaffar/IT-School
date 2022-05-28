from PIL import ImageTk
import PIL.Image
from tkinter import *
import os, sys
from tkinter.messagebox import *
import webbrowser as wb
from tkinter import ttk
import sqlite3
# import psycopg2
from datetime import datetime
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# import pyodbc



m = Tk()
m.title("IT School")
m.config(bg="black")
m.geometry(f"700x900+500+0")




# con = sqlite3.connect("user_db.db")
# con = psycopg2.connect("user_db.db")

# c = con.cursor()


engine = create_engine("sqlite:///db/user_db.db", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
db = Session()








unit = ""
course = ""
code_db = ""





Base.metadata.create_all(engine)



##############################################


try:

    class python_db(Base):

        __tablename__ = f"python_db"

        id = Column(Integer, primary_key=True, nullable=False)
        ism = Column(String, nullable=False)
        familya = Column(String, nullable=False)
        telefon = Column(String, nullable=False)
        manzil = Column(String, nullable=False)
        kurs = Column(String, nullable=False)
        vaqt = Column(String, nullable=False)


    class javadroid_db(Base):

        __tablename__ = f"javadroid_db"

        id = Column(Integer, primary_key=True)
        ism = Column(String, nullable=False)
        familya = Column(String, nullable=False)
        telefon = Column(String, nullable=False)
        manzil = Column(String, nullable=False)
        kurs = Column(String, nullable=False)
        vaqt = Column(String, nullable=False)


    class web_db(Base):

        __tablename__ = f"web_db"

        id = Column(Integer, primary_key=True)
        ism = Column(String, nullable=False)
        familya = Column(String, nullable=False)
        telefon = Column(String, nullable=False)
        manzil = Column(String, nullable=False)
        kurs = Column(String, nullable=False)
        vaqt = Column(String, nullable=False)


    class robotech_db(Base):

        __tablename__ = f"robotech_db"

        id = Column(Integer, primary_key=True)
        ism = Column(String, nullable=False)
        familya = Column(String, nullable=False)
        telefon = Column(String, nullable=False)
        manzil = Column(String, nullable=False)
        kurs = Column(String, nullable=False)
        vaqt = Column(String, nullable=False)


    class photoshop_db(Base):

        __tablename__ = f"photoshop_db"

        id = Column(Integer, primary_key=True)
        ism = Column(String, nullable=False)
        familya = Column(String, nullable=False)
        telefon = Column(String, nullable=False)
        manzil = Column(String, nullable=False)
        kurs = Column(String, nullable=False)
        vaqt = Column(String, nullable=False)


    class coreldraw_db(Base):

        __tablename__ = f"coreldraw_db"

        id = Column(Integer, primary_key=True)
        ism = Column(String, nullable=False)
        familya = Column(String, nullable=False)
        telefon = Column(String, nullable=False)
        manzil = Column(String, nullable=False)
        kurs = Column(String, nullable=False)
        vaqt = Column(String, nullable=False)


    class illustrator_db(Base):

        __tablename__ = f"illustrator_db"

        id = Column(Integer, primary_key=True)
        ism = Column(String, nullable=False)
        familya = Column(String, nullable=False)
        telefon = Column(String, nullable=False)
        manzil = Column(String, nullable=False)
        kurs = Column(String, nullable=False)
        vaqt = Column(String, nullable=False)

    class tridmax_db(Base):

        __tablename__ = f"tridmax_db"

        id = Column(Integer, primary_key=True)
        ism = Column(String, nullable=False)
        familya = Column(String, nullable=False)
        telefon = Column(String, nullable=False)
        manzil = Column(String, nullable=False)
        kurs = Column(String, nullable=False)
        vaqt = Column(String, nullable=False)


    class autocad_db(Base):

        __tablename__ = f"autocad_db"

        id = Column(Integer, primary_key=True)
        ism = Column(String, nullable=False)
        familya = Column(String, nullable=False)
        telefon = Column(String, nullable=False)
        manzil = Column(String, nullable=False)
        kurs = Column(String, nullable=False)
        vaqt = Column(String, nullable=False)


    class computer_db(Base):

        __tablename__ = f"computer_db"

        id = Column(Integer, primary_key=True)
        ism = Column(String, nullable=False)
        familya = Column(String, nullable=False)
        telefon = Column(String, nullable=False)
        manzil = Column(String, nullable=False)
        kurs = Column(String, nullable=False)
        vaqt = Column(String, nullable=False)


    class iteng_db(Base):

        __tablename__ = f"iteng_db"

        id = Column(Integer, primary_key=True)
        ism = Column(String, nullable=False)
        familya = Column(String, nullable=False)
        telefon = Column(String, nullable=False)
        manzil = Column(String, nullable=False)
        kurs = Column(String, nullable=False)
        vaqt = Column(String, nullable=False)



except:

    pass


##############################################
###############################################

# data = python_db(ism="", familya="", telefon="", manzil="", kurs=course, vaqt=datetime.now())
# db.add(data)
# db.commit()


# data = javadroid_db(ism="", familya="", telefon="", manzil="", kurs=course, vaqt=datetime.now())
# db.add(data)
# db.commit()

        
# data = web_db(ism="", familya="", telefon="", manzil="", kurs=course, vaqt=datetime.now())
# db.add(data)
# db.commit()

        
# data = robotech_db(ism="", familya="", telefon="", manzil="", kurs=course, vaqt=datetime.now())
# db.add(data)
# db.commit()
        

# data = photoshop_db(ism="", familya="", telefon="", manzil="", kurs=course, vaqt=datetime.now())
# db.add(data)
# db.commit()


# data = coreldraw_db(ism="", familya="", telefon="", manzil="", kurs=course, vaqt=datetime.now())
# db.add(data)
# db.commit()

        
# data = illustrator_db(ism="", familya="", telefon="", manzil="", kurs=course, vaqt=datetime.now())
# db.add(data)
# db.commit()

        
# data = tridmax_db(ism="", familya="", telefon="", manzil="", kurs=course, vaqt=datetime.now())
# db.add(data)
# db.commit()


# data = autocad_db(ism="", familya="", telefon="", manzil="", kurs=course, vaqt=datetime.now())
# db.add(data)
# db.commit()

        
# data = computer_db(ism="", familya="", telefon="", manzil="", kurs=course, vaqt=datetime.now())
# db.add(data)
# db.commit()


# data = iteng_db(ism="", familya="", telefon="", manzil="", kurs=course, vaqt=datetime.now())
# db.add(data)
# db.commit()


##############################################
#############################################








def show():
    
    frame_place = False

    global frame
    global btn
    
    # btn.forget()
    frame.place(x=0, y=0)
    btn['bg']='grey'
    m['bg']='grey'
    lbl_['bg']='grey'
    reg_btn_['bg']='grey'
    info_btn_['bg']='grey'
    contact_btn_['bg']='grey'
    about_btn_['bg']='grey'
    




def hide():
    global frame
    global btn

    # btn.pack(side=RIGHT, anchor=NE)
    frame.place(x=-1000, y=0)
    btn['bg']='white'
    m['bg']='black'
    lbl_['bg']='black'
    reg_btn_['bg']='grey17'
    info_btn_['bg']='grey17'
    contact_btn_['bg']='grey17'
    about_btn_['bg']='grey17'


def hide_nav(event):
    global frame
    global btn

    # btn.pack(side=RIGHT, anchor=NE)
    frame.place(x=-1000, y=0)
    btn['bg']='white'
    m['bg']='black'
    lbl_['bg']='black'
    reg_btn_['bg']='grey17'
    info_btn_['bg']='grey17'
    contact_btn_['bg']='grey17'
    about_btn_['bg']='grey17'



##########################################
##########################################
#images

img = PIL.Image.open("img/coding3.jpg").resize((50, 50))
coding = ImageTk.PhotoImage(img)

img = PIL.Image.open("img/python2.jpg").resize((40, 40))
python = ImageTk.PhotoImage(img)

img = PIL.Image.open("img/javadroid.jpg").resize((50, 50))
javadroid = ImageTk.PhotoImage(img)

img = PIL.Image.open("img/web.jpg").resize((60, 50))
web = ImageTk.PhotoImage(img)

img = PIL.Image.open("img/robot.jpg").resize((50, 50))
robot = ImageTk.PhotoImage(img)

img = PIL.Image.open("img/robotech.jpg").resize((50, 50))
robotech = ImageTk.PhotoImage(img)

img = PIL.Image.open("img/graphic.jpg").resize((70, 50))
graphic = ImageTk.PhotoImage(img)

img = PIL.Image.open("img/photoshop.png").resize((50, 50))
foto = ImageTk.PhotoImage(img)

img = PIL.Image.open("img/illustrator.png").resize((50, 50))
illustrator = ImageTk.PhotoImage(img)

img = PIL.Image.open("img/coreldraw.jpg").resize((70, 50))
corel = ImageTk.PhotoImage(img)

img = PIL.Image.open("img/3dmax.jpg").resize((70, 50))
tridmax = ImageTk.PhotoImage(img)

img = PIL.Image.open("img/autocad.jpg").resize((90, 50))
autocad_ = ImageTk.PhotoImage(img)

img = PIL.Image.open("img/iten.jpg").resize((90, 50))
iteng = ImageTk.PhotoImage(img)

img = PIL.Image.open("img/itparkcompsavod.jpg").resize((90, 50))
compsavod = ImageTk.PhotoImage(img)

img = PIL.Image.open("img/architect.jpg").resize((90, 50))
architect = ImageTk.PhotoImage(img)

img = PIL.Image.open("img/curs.jpg").resize((90, 50))
curs = ImageTk.PhotoImage(img)

img = PIL.Image.open("img/man.jpg").resize((100, 120))
man = ImageTk.PhotoImage(img)




############################################
############################################

def registration():


    # global top
    global python_db

    topm = Toplevel()
    topm.geometry("700x1000+500+0")
    topm.title("Registration")





    Label(topm, text="Registratsiya", font=("Arial", 30)).pack(padx=20, pady=20)



    Label(topm, text=f"Bo'lim: {unit}",  font=("Bold", 13)).pack(anchor=NW)
    Label(topm, text=f"Kurs: {course}",  font=("Bold", 13)).pack(anchor=NW)


    Label(topm, text=f"", image=man).pack(padx=10, pady=10)

    LFrame = LabelFrame(topm, text=f"Register", relief=SUNKEN, bd=5)

    Label(LFrame, text=f"Ism: ", fg="blue", bd=5).grid(row=5, column=1)
    en1 = Entry(LFrame, fg="red")
    en1.grid(row=5, column=2)
    Label(LFrame, text=f"Familya: ", fg="blue", bd=5).grid(row=6, column=1)
    en2 = Entry(LFrame, fg="red")
    en2.grid(row=6, column=2)
    Label(LFrame, text=f"Telefon raqam: ", fg="blue", bd=5).grid(row=8, column=1)
    en3 = Entry(LFrame, fg="red")
    en3.grid(row=8, column=2)
    Label(LFrame, text=f"Manzil: ", fg="blue", bd=5).grid(row=9, column=1)
    en4 = Entry(LFrame, fg="red")
    en4.grid(row=9, column=2)
    
    
    LFrame.pack()






    

    ##########################################################################

    def submit():


        """
        python_db
        javadroid_db
        web_db
        robotech_db
        photoshop_db
        coreldraw_db
        illustrator_db
        tridmax_db
        autocad_db
        computer_db
        iteng_db
        """
        

        if code_db == "python":

            data = python_db(ism=en1.get(), familya=en2.get(), telefon=en3.get(), manzil=en4.get(), kurs=course, vaqt=datetime.now())

            db.add(data)
            db.commit()

        if code_db == "javadroid":

            data = javadroid_db(ism=en1.get(), familya=en2.get(), telefon=en3.get(), manzil=en4.get(), kurs=course, vaqt=datetime.now())

            db.add(data)
            db.commit()

        
        if code_db == "web":

            data = web_db(ism=en1.get(), familya=en2.get(), telefon=en3.get(), manzil=en4.get(), kurs=course, vaqt=datetime.now())

            db.add(data)
            db.commit()

        
        if code_db == "robotech":

            data = robotech_db(ism=en1.get(), familya=en2.get(), telefon=en3.get(), manzil=en4.get(), kurs=course, vaqt=datetime.now())

            db.add(data)
            db.commit()

        
        if code_db == "photoshop":

            data = photoshop_db(ism=en1.get(), familya=en2.get(), telefon=en3.get(), manzil=en4.get(), kurs=course, vaqt=datetime.now())

            db.add(data)
            db.commit()

        
        if code_db == "coreldraw":

            data = coreldraw_db(ism=en1.get(), familya=en2.get(), telefon=en3.get(), manzil=en4.get(), kurs=course, vaqt=datetime.now())

            db.add(data)
            db.commit()

        
        if code_db == "illustrator":

            data = illustrator_db(ism=en1.get(), familya=en2.get(), telefon=en3.get(), manzil=en4.get(), kurs=course, vaqt=datetime.now())

            db.add(data)
            db.commit()

        
        if code_db == "tridmax":

            data = tridmax_db(ism=en1.get(), familya=en2.get(), telefon=en3.get(), manzil=en4.get(), kurs=course, vaqt=datetime.now())

            db.add(data)
            db.commit()

        
        if code_db == "autocad":

            data = autocad_db(ism=en1.get(), familya=en2.get(), telefon=en3.get(), manzil=en4.get(), kurs=course, vaqt=datetime.now())

            db.add(data)
            db.commit()

        
        if code_db == "computer":

            data = computer_db(ism=en1.get(), familya=en2.get(), telefon=en3.get(), manzil=en4.get(), kurs=course, vaqt=datetime.now())

            db.add(data)
            db.commit()

        
        if code_db == "iteng":

            data = iteng_db(ism=en1.get(), familya=en2.get(), telefon=en3.get(), manzil=en4.get(), kurs=course, vaqt=datetime.now())

            db.add(data)
            db.commit()

        
        


        showinfo("Info", "Registration has been successfully!")

        top = Toplevel()
        top.geometry("700x120+500+0")
        top.title("Registration")
        top.config(bg="green")
        


        
        if code_db == "python":

            student_id = db.query(python_db.id).filter(python_db.telefon==en3.get()).first()


        if code_db == "javadroid":

            student_id = db.query(javadroid_db.id).filter(javadroid_db.telefon==en3.get()).first()


        
        if code_db == "web":

            student_id = db.query(web_db.id).filter(web_db.telefon==en3.get()).first()

        
        if code_db == "robotech":

            student_id = db.query(robotech_db.id).filter(robotech_db.telefon==en3.get()).first()

        
        if code_db == "photoshop":

            student_id = db.query(photoshop_db.id).filter(photoshop_db.telefon==en3.get()).first()


        if code_db == "coreldraw":

            student_id = db.query(coreldraw_db.id).filter(coreldraw_db.telefon==en3.get()).first()


        
        if code_db == "illustrator":

            student_id = db.query(illustrator_db.id).filter(illustrator_db.telefon==en3.get()).first()


        
        if code_db == "tridmax":

            student_id = db.query(tridmax_db.id).filter(tridmax_db.telefon==en3.get()).first()

        
        if code_db == "autocad":

            student_id = db.query(autocad_db.id).filter(autocad_db.telefon==en3.get()).first()

        
        if code_db == "computer":

            student_id = db.query(computer_db.id).filter(computer_db.telefon==en3.get()).first()

        if code_db == "iteng":

            student_id = db.query(iteng_db.id).filter(iteng_db.telefon==en3.get()).first()


        
        print(student_id)
        print(student_id[0])
        print(student_id[-0])
        Label(top, text=f"Course code: {code_db}_db", bg="green", font=("Bold", 30)).pack(anchor=NW)
        Label(top, text=f"Student id: {student_id[0]}", bg="green", font=("Bold", 30)).pack(anchor=NW)

 

        
    # def submit_(event):

    #     data = python_db(ism=en1.get(), familya=en2.get(), telefon=en3.get(), manzil=en4.get(), kurs=course, vaqt=datetime.now())

    #     db.add(data)
    #     db.commit()

        













    Button(topm, text="Submit", command=submit).pack(padx=20, pady=20)

    # en1.bind("<Return>", submit_)
    # en2.bind("<Return>", submit_)
    # en3.bind("<Return>", submit_)
    # en4.bind("<Return>", submit_)

    # LFrame.bind("<Return>", submit_)
    # top.bind("<Return>", submit_)







    

    





############################################
############################################
def course():
    global top

    top = Toplevel()

    top.geometry("500x900+500+0")
    top.title("Course")
    top.config(bg="green")


    var = StringVar()


    #create a Main Frame
    main_frame=Frame(top, bg="green")
    main_frame.pack(fill=BOTH,expand=1)

    #Create A Canvas
    my_canvas=Canvas(main_frame, bg="green")
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

    #Add A Scrollbar To The Canvas
    my_scrollbar=ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)

    #Configure Canvas
    my_canvas.config(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e: my_canvas.config(scrollregion=my_canvas.bbox("all")))

    #Create Another Frame INSIDE The Canvas
    second_frame=Frame(my_canvas, bg="green")

    #Add That New frame To a Window In Canvas
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")




 








    #dasturlash
    def func_1():global unit; global course; global code_db; unit="Dasturlash"; course="Python"; code_db="python"; registration()
    def func_2():global unit; global course; global code_db; unit="Dasturlash"; course="Java Android"; code_db="javadroid"; registration()
    def func_3():global unit; global course; global code_db; unit="Dasturlash"; course="Web"; code_db="web"; registration()

    #Robototech global code_db;
    def func_4():global unit; global course; global code_db; unit="Roboto texnika"; course="Roboto texnika"; code_db="robotech"; registration()

    #Grafika global code_db;
    def func_5():global unit; global course; global code_db; unit="Grafika"; course="Photoshop"; code_db="photoshop"; registration()
    def func_6():global unit; global course; global code_db; unit="Grafika"; course="Corel Draw"; code_db="coreldraw"; registration()
    def func_7():global unit; global course; global code_db; unit="Grafika"; course="Illustrator"; code_db="illustrator"; registration()

    #Arxitektura global code_db;
    def func_8():global unit; global course; global code_db; unit="Arxitektura"; course="3DMax"; code_db="tridmax"; registration()
    def func_9():global unit; global course; global code_db; unit="Arxitektura"; course="Autocad"; code_db="autocad"; registration()

    #Qoshimcha kurslar
    def func_10():global unit; global course; global code_db; unit="Qo'shimcha kurslar"; course="Computer savodxonligi"; code_db="computer"; registration()
    def func_11():global unit; global course; global code_db; unit="Qo'shimcha kurslar"; course="IT English"; code_db="iteng"; registration()










    # radiobtn = Radiobutton(top, text=f"{text}", indicatoron=0, width=10, value="m").pack(fill=X)




    Label(second_frame, text="Kurslar: ", fg="red", bg="green", font=("Arial", 40)).pack(fill=X, pady=35, padx=35)



    Label(second_frame, text="Dasturlash:", image=coding, compound=LEFT, bg="green", font=("Arial", 15)).pack(fill=X, pady=20, padx=30)
    Button(second_frame, text="Python", image=python, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_1).pack(fill=X)
    Button(second_frame, text="Java Android", image=javadroid, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_2).pack(fill=X)
    Button(second_frame, text="Web", image=web, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_3).pack(fill=X)

    Label(second_frame, text="Roboto texnika:", image=robot, compound=LEFT, bg="green", font=("Arial", 15)).pack(fill=X, pady=20, padx=30)
    Button(second_frame, text="Roboto texnika", image=robotech, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_4).pack(fill=X)

    Label(second_frame, text="Grafika:", image=graphic, compound=LEFT, bg="green", font=("Arial", 15)).pack(fill=X, pady=20, padx=30)
    Button(second_frame, text="Photoshop", image=foto, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_5).pack(fill=X)
    Button(second_frame, text="Corel Draw", image=corel, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_6).pack(fill=X)
    Button(second_frame, text="Illustrator", image=illustrator, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_7).pack(fill=X)

    Label(second_frame, text="Arxitektura:", image=architect, compound=LEFT, bg="green", font=("Arial", 15)).pack(fill=X, pady=20, padx=30)
    Button(second_frame, text="3DMax", image=tridmax, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_8).pack(fill=X)
    Button(second_frame, text=" ", image=autocad_, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_9).pack(fill=X)

    Label(second_frame, text="Qo'shimcha kurslar:", image=curs, compound=LEFT, bg="green", font=("Arial", 15)).pack(fill=X, pady=20, padx=30)
    Button(second_frame, text="Kompyuter savodxonligi",  image=compsavod, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_10).pack(fill=X)
    Button(second_frame, text="IT English",  image=iteng, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_11).pack(fill=X)


    Label(second_frame, text=" ",  bg="green", font=("Arial", 15)).pack(fill=X, pady=20, padx=30)








############################################
############################################
def course_():
    global top

    top = Toplevel()

    top.geometry("500x900+500+0")
    top.title("Course")
    top.config(bg="green")


    var = StringVar()


    #create a Main Frame
    main_frame=Frame(top, bg="green")
    main_frame.pack(fill=BOTH,expand=1)

    #Create A Canvas
    my_canvas=Canvas(main_frame, bg="green")
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

    #Add A Scrollbar To The Canvas
    my_scrollbar=ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)

    #Configure Canvas
    my_canvas.config(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e: my_canvas.config(scrollregion=my_canvas.bbox("all")))

    #Create Another Frame INSIDE The Canvas
    second_frame=Frame(my_canvas, bg="green")

    #Add That New frame To a Window In Canvas
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")




 








    #dasturlash
    def func_1():global unit; global course; global code_db; unit="Dasturlash"; course="Python"; code_db="python"; student()
    def func_2():global unit; global course; global code_db; unit="Dasturlash"; course="Java Android"; code_db="javadroid"; student()
    def func_3():global unit; global course; global code_db; unit="Dasturlash"; course="Web"; code_db="web"; student()

    #Robototech global code_db;
    def func_4():global unit; global course; global code_db; unit="Roboto texnika"; course="Roboto texnika"; code_db="robotech"; student()

    #Grafika global code_db;
    def func_5():global unit; global course; global code_db; unit="Grafika"; course="Photoshop"; code_db="photoshop"; student()
    def func_6():global unit; global course; global code_db; unit="Grafika"; course="Corel Draw"; code_db="coreldraw"; student()
    def func_7():global unit; global course; global code_db; unit="Grafika"; course="Illustrator"; code_db="illustrator"; student()

    #Arxitektura global code_db;
    def func_8():global unit; global course; global code_db; unit="Arxitektura"; course="3DMax"; code_db="tridmax"; student()
    def func_9():global unit; global course; global code_db; unit="Arxitektura"; course="Autocad"; code_db="autocad"; student()

    #Qoshimcha kurslar
    def func_10():global unit; global course; global code_db; unit="Qo'shimcha kurslar"; course="Computer savodxonligi"; code_db="computer"; student()
    def func_11():global unit; global course; global code_db; unit="Qo'shimcha kurslar"; course="IT English"; code_db="iteng"; student()










    # radiobtn = Radiobutton(top, text=f"{text}", indicatoron=0, width=10, value="m").pack(fill=X)




    Label(second_frame, text="Kurslar: ", fg="red", bg="green", font=("Arial", 40)).pack(fill=X, pady=35, padx=35)



    Label(second_frame, text="Dasturlash:", image=coding, compound=LEFT, bg="green", font=("Arial", 15)).pack(fill=X, pady=20, padx=30)
    Button(second_frame, text="Python", image=python, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_1).pack(fill=X)
    Button(second_frame, text="Java Android", image=javadroid, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_2).pack(fill=X)
    Button(second_frame, text="Web", image=web, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_3).pack(fill=X)

    Label(second_frame, text="Roboto texnika:", image=robot, compound=LEFT, bg="green", font=("Arial", 15)).pack(fill=X, pady=20, padx=30)
    Button(second_frame, text="Roboto texnika", image=robotech, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_4).pack(fill=X)

    Label(second_frame, text="Grafika:", image=graphic, compound=LEFT, bg="green", font=("Arial", 15)).pack(fill=X, pady=20, padx=30)
    Button(second_frame, text="Photoshop", image=foto, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_5).pack(fill=X)
    Button(second_frame, text="Corel Draw", image=corel, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_6).pack(fill=X)
    Button(second_frame, text="Illustrator", image=illustrator, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_7).pack(fill=X)

    Label(second_frame, text="Arxitektura:", image=architect, compound=LEFT, bg="green", font=("Arial", 15)).pack(fill=X, pady=20, padx=30)
    Button(second_frame, text="3DMax", image=tridmax, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_8).pack(fill=X)
    Button(second_frame, text=" ", image=autocad_, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_9).pack(fill=X)

    Label(second_frame, text="Qo'shimcha kurslar:", image=curs, compound=LEFT, bg="green", font=("Arial", 15)).pack(fill=X, pady=20, padx=30)
    Button(second_frame, text="Kompyuter savodxonligi",  image=compsavod, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_10).pack(fill=X)
    Button(second_frame, text="IT English",  image=iteng, compound=LEFT, font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", bd=20, command=func_11).pack(fill=X)


    Label(second_frame, text=" ",  bg="green", font=("Arial", 15)).pack(fill=X, pady=20, padx=30)






#############################################
#############################################


def student():

    global info_l
    global btn_
    global LFrame_
    global entry1
    global entry2


    top = Toplevel()

    top.geometry("700x1000+500+0")

    top.title("Student Info")
    top.config(bg="green")


    info_l = Label(top, text="Student Information", bg="green", font=("bold", 35)).pack(padx=20, pady=20)
    LFrame_ = LabelFrame(top, text="Info", relief=SUNKEN)
    
    LFrame_.pack()



    Label(LFrame_, text="Course code: ").grid(row=5, column=1) 
    entry1 = Entry(LFrame_)
    entry1.grid(row=5, column=2)

    Label(LFrame_, text="Student id: ").grid(row=6, column=1)
    entry2 = Entry(LFrame_)
    entry2.grid(row=6, column=2)



    def get_info():

        top_info = Toplevel()
        top_info.geometry("700x300+500+0")
        top_info.title("Registration")
        top_info.config(bg="green")



        
        
        if code_db == "python":

            student_info = db.query(python_db.ism, python_db.familya, python_db.telefon, python_db.manzil, python_db.kurs, python_db.vaqt).filter(python_db.id==entry2.get()).first()


        if code_db == "javadroid":

            student_info = db.query(javadroid_db.ism, javadroid_db.familya, javadroid_db.telefon, javadroid_db.manzil, javadroid_db.kurs, javadroid_db.vaqt).filter(javadroid_db.id==entry2.get()).first()


        
        if code_db == "web":

            student_info = db.query(web_db.ism, web_db.familya, web_db.telefon, web_db.manzil, web_db.kurs, web_db.vaqt).filter(web_db.id==entry2.get()).first()

        
        if code_db == "robotech":

            student_info = db.query(robotech_db.ism, robotech_db.familya, robotech_db.telefon, robotech_db.manzil, robotech_db.kurs, robotech_db.vaqt).filter(robotech_db.id==entry2.get()).first()

        
        if code_db == "photoshop":

            student_info = db.query(photoshop_db.ism, photoshop_db.familya, photoshop_db.telefon, photoshop_db.manzil, photoshop_db.kurs, photoshop_db.vaqt).filter(photoshop_db.id==entry2.get()).first()


        if code_db == "coreldraw":

            student_info = db.query(coreldraw_db.ism, coreldraw_db.familya, coreldraw_db.telefon, coreldraw_db.manzil, coreldraw_db.kurs, coreldraw_db.vaqt).filter(coreldraw_db.id==entry2.get()).first()


        
        if code_db == "illustrator":

            student_info = db.query(illustrator_db.ism, illustrator_db.familya, illustrator_db.telefon, illustrator_db.manzil, illustrator_db.kurs, illustrator_db.vaqt).filter(illustrator_db.id==entry2.get()).first()


        
        if code_db == "tridmax":

            student_info = db.query(tridmax_db.ism, tridmax_db.familya, tridmax_db.telefon, tridmax_db.manzil, tridmax_db.kurs, tridmax_db.vaqt).filter(tridmax_db.id==entry2.get()).first()

        
        if code_db == "autocad":

            student_info = db.query(autocad_db.ism, autocad_db.familya, autocad_db.telefon, autocad_db.manzil, autocad_db.kurs, autocad_db.vaqt).filter(autocad_db.id==entry2.get()).first()

        
        if code_db == "computer":

            student_info = db.query(computer_db.ism, computer_db.familya, computer_db.telefon, computer_db.manzil, computer_db.kurs, computer_db.vaqt).filter(computer_db.id==entry2.get()).first()

        if code_db == "iteng":

            student_info = db.query(iteng_db.ism, iteng_db.familya, iteng_db.telefon, iteng_db.manzil, iteng_db.kurs, iteng_db.vaqt).filter(iteng_db.id==entry2.get()).first()


        
        # student_info = db.query(python_db).filter(python_db.id==entry2.get()).first()


        Label(top_info, text=f"Student info: ", bg="green", font=("Bold", 20)).pack(anchor=NW)
        Label(top_info, text=f"\tIsm: {student_info[0]}", bg="green", font=("Bold", 20)).pack(anchor=NW)
        Label(top_info, text=f"\tFamilya: {student_info[1]}", bg="green", font=("Bold", 20)).pack(anchor=NW)
        Label(top_info, text=f"\tTelefon raqam: {student_info[2]}", bg="green", font=("Bold", 20)).pack(anchor=NW)
        Label(top_info, text=f"\tManzil: {student_info[3]}", bg="green", font=("Bold", 20)).pack(anchor=NW)
        Label(top_info, text=f"\tKurs: {student_info[4]}", bg="green", font=("Bold", 20)).pack(anchor=NW)
        Label(top_info, text=f"\tVaqt: {student_info[5]}", bg="green", font=("Bold", 20)).pack(anchor=NW)





    btn_ = Button(top, text="submit", command=get_info).pack(padx=10, pady=10)


    # global code_db

    # course = entry1.get()
    # code_db = entry1.get()
            



############################################
############################################

def contact():
    # top = Toplevel()

    # top.geometry("700x1000+500+0")

    wb.open("t.me/NITS_ADMIN")

############################################
###########################################

def about():
#     top = Toplevel()
#     top.geometry("700x1000+500+0")
#     top.title("Information")

    wb.open("t.me/NITSchool")


##############################################
###############################################

img = PIL.Image.open("img/itpark.jpg").resize((250, 95))
itpark = ImageTk.PhotoImage(img)

main_lbl = Label(m, text="IT School", image=itpark, fg="green", bg="lightblue", height=120, width=500, padx=20, relief=SUNKEN)

btn = Button(m, text="->", height=2, width=4, bd=5, command=show)




lbl_ = Label(m, bd=10, bg="black")
reg_btn_ = Button(m, text="Registratsiya", font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", width=35, bd=20, command=course)
info_btn_ = Button(m, text="O'quvchi haqida ma'lumot", font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", width=35, bd=20, command=course_)
contact_btn_ = Button(m, text="Bog'lanish", font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", width=35, bd=20, command=contact)
about_btn_ = Button(m, text="Ma'lumot", font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", width=35, bd=20, command=about)




frame = Frame(m, bg="red", bd=5, width=500, height=5000)



lbl = Label(frame, text="IT School", fg="green", bg="yellow", height=3, width=500, padx=20, relief=SUNKEN)
btn_f = Button(frame, text='x', height=2, width=4, bd=5, command=hide)
btn_f.place(x=450, y=2.5)

y = 70











reg_btn = Button(frame, text="Registratsiya", font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", width=20, bd=10, command=course).place(x=0, y=y);y += 70

info_btn = Button(frame, text="O'quvchi haqida ma'lumot", font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", width=20, bd=10, command=course_).place(x=0, y=y);y += 70

contact_btn = Button(frame, text="Bog'lanish", font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", width=20, bd=10, command=contact).place(x=0, y=y);y += 70

about_btn = Button(frame, text="Ma'lumot", font="BahnschriftLight 15", bg="gray17", fg="orange", activebackground="gray17", activeforeground="green", width=20, bd=10, command=about).place(x=0, y=y);y += 70









frame.place(x=-1000, y=0)



lbl.place(x=0, y=0)













# m.bind("<Enter>", hide_nav)
# m.bind("<Button-1>", hide_nav)
main_lbl.bind("<Return>", hide_nav)
main_lbl.bind("<Button-1>", hide_nav)

main_lbl.pack(fill=X)

btn.pack(side=RIGHT, anchor=NE)


lbl_.pack()
reg_btn_.pack(padx=50, pady=20)
info_btn_.pack(padx=50, pady=20)
contact_btn_.pack(padx=50, pady=20)
about_btn_.pack(padx=50, pady=20)




m.mainloop()
