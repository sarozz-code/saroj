from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os



class login:
    """
    this class is for login
    """
    def login_user(self):
        """
        this function is for opening login data
        """
        loginusername = username_verify.get()
        loginpassword = password_verify.get()
        loginusernameentry.delete(0, END)
        loginpasswordentry.delete(0, END)

        list_of_files = os.listdir()
        if loginusername in list_of_files:
            file1 = open(loginusername, "r")
            verify = file1.read().splitlines()
            if loginpassword in verify:
                messagebox.showinfo("Success", "Login successfull")
                frame.destroy()

                class login_file:
                    """
                    this class is used after successfull login and consist employee detail
                    """
                    def __init__(self, root):
                        """
                        this function contains all the label and entry of employee form and department form
                        """
                        self.root = root
                        self.root.title("Login successfull")
                        self.root.config(background="silver")
                        self.root.geometry("1524x787+0+0")

                        self.id = StringVar()
                        self.name = StringVar()
                        self.age = StringVar()
                        self.address = StringVar()
                        self.contact = StringVar()
                        self.department = StringVar()
                        self.dob = StringVar()
                        self.dname = StringVar()
                        self.dcode = StringVar()

                        maintitle = Label(self.root, text="EMPLOYEE MANAGEMENT SYSTEM", bd=9, relief=GROOVE,
                                          font=("jester", 27, "bold"), bg="silver").pack(fill=X)

                        employeeframe = Frame(self.root, bd=9, relief=GROOVE, bg="silver").place(x=0, y=98, height=570,
                                                                                                 width=1112)

                        msgframe = Frame(employeeframe, bd=5, relief=GROOVE, bg="silver").place(x=579, y=180,
                                                                                                height=345, width=515)

                        msgtitle = Label(msgframe, text="Department", font=("jester", 14, "bold"), bg="silver")
                        msgtitle.place(x=585, y=194)

                        examination = Label(msgframe,
                                            text="1.Examination       01           It mainly deal with the appointment of paper ",
                                            font=("jester", 11, "bold"), bg="silver")
                        examination.place(x=585, y=235)

                        examination1 = Label(msgframe,
                                             text="setters,publication of schedule of \n examinations and conducts examination.",
                                             font=("jester", 11, "bold"), bg="silver")
                        examination1.place(x=770, y=255)

                        technical = Label(msgframe,
                                          text="2.Technical           02          Management of using, reparing, purchasing ",
                                          font=("jester", 11, "bold"), bg="silver")
                        technical.place(x=585, y=295)

                        technical1 = Label(msgframe, text="equipments for business operations in \n Company.",
                                           font=("jester", 11, "bold"), bg="silver")
                        technical1.place(x=770, y=315)

                        administration = Label(msgframe,
                                               text="3.Administration    03          To enhance the office staff’s ability to ",
                                               font=("jester", 11, "bold"), bg="silver")
                        administration.place(x=585, y=355)

                        administration1 = Label(msgframe,
                                                text="manage and organize office effectively \n and professionally. ",
                                                font=("jester", 11, "bold"), bg="silver")
                        administration1.place(x=770, y=375)

                        faculty = Label(msgframe,
                                        text="4.Faculty                 04             Provides learning opportunities.",
                                        font=("jester", 11, "bold"), bg="silver")
                        faculty.place(x=585, y=415)

                        sports = Label(msgframe,
                                       text="5.sports                  05             Organising, developing and delivering a",
                                       font=("jester", 11, "bold"), bg="silver")
                        sports.place(x=585, y=435)

                        sports1 = Label(msgframe, text="varied range of sporting activities, projects\n programmes.",
                                        font=("jester", 11, "bold"), bg="silver")
                        sports1.place(x=774, y=455)

                        msgtitle1 = Label(msgframe, text="code", font=("jester", 14, "bold"), bg="silver")
                        msgtitle1.place(x=710, y=194)

                        msgtitle2 = Label(msgframe, text="Work", font=("jester", 14, "bold"), bg="silver")
                        msgtitle2.place(x=900, y=194)

                        employeetitle = Label(employeeframe, text="Employee Register Form", font=("jester", 27, "bold"),
                                              bg="silver")
                        employeetitle.place(x=95, y=112)

                        employeetitle = Label(employeeframe, text="Department Form", font=("jester", 27, "bold"),
                                              bg="silver")
                        employeetitle.place(x=677, y=112)

                        dname = Label(employeeframe, text="Department Name", font=("jester", 25, "bold"), bg="silver")
                        dname.place(x=582, y=532)

                        namecombo = ttk.Combobox(employeeframe, textvariable=self.dname, width=32)
                        namecombo["values"] = ("Examination", "Technical", "Administration", "Facaulty", "Sports")
                        namecombo.place(x=873, y=545)

                        codecombo = ttk.Combobox(employeeframe, textvariable=self.dcode, width=32)
                        codecombo["values"] = ("01", "02", "03", "04", "05")
                        codecombo.place(x=873, y=615)

                        dcode = Label(employeeframe, text="Department Code", font=("jester", 25, "bold"), bg="silver")
                        dcode.place(x=582, y=602)

                        id = Label(employeeframe, text="Employee ID", font=("jester", 25, "bold"), bg="silver")
                        id.place(x=15, y=182)

                        name = Label(employeeframe, text="Employee Name", font=("jester", 25, "bold"), bg="silver")
                        name.place(x=15, y=252)

                        age = Label(employeeframe, text="Employee Age", font=("jester", 25, "bold"), bg="silver")
                        age.place(x=15, y=322)

                        address = Label(employeeframe, text="Employee Address", font=("jester", 25, "bold"),
                                        bg="silver")
                        address.place(x=15, y=392)

                        contact = Label(employeeframe, text="Employee contact no", font=("jester", 25, "bold"),
                                        bg="silver")
                        contact.place(x=15, y=462)

                        department = Label(employeeframe, text="Worked Department", font=("jester", 25, "bold"),
                                           bg="silver")
                        department.place(x=15, y=532)

                        dob = Label(employeeframe, text="Date of birth", font=("jester", 25, "bold"), bg="silver")
                        dob.place(x=15, y=602)

                        identry = Entry(employeeframe, textvariable=self.id, width=32)
                        identry.place(x=368, y=192)

                        nameentry = Entry(employeeframe, textvariable=self.name, width=32)
                        nameentry.place(x=368, y=262)

                        ageentry = Entry(employeeframe, textvariable=self.age, width=32)
                        ageentry.place(x=368, y=332)

                        addressentry = Entry(employeeframe, textvariable=self.address, width=32)
                        addressentry.place(x=368, y=402)

                        contactentry = Entry(employeeframe, textvariable=self.contact, width=32)
                        contactentry.place(x=368, y=472)

                        departmententry = Entry(employeeframe, textvariable=self.department, width=32)
                        departmententry.place(x=368, y=542)

                        dobentry = Entry(employeeframe, textvariable=self.dob, width=32)
                        dobentry.place(x=368, y=612)

                        savedfileframe = Frame(self.root, bd=9, relief=GROOVE, bg="silver").place(x=1120, y=98,
                                                                                                  height=570,
                                                                                                  width=400)
                        savedfile = Label(savedfileframe, text="Saved Files", font="arial 25 bold", bg="silver")
                        savedfile.place(x=1190, y=112)

                        y_scroll = Scrollbar(savedfileframe, orient=VERTICAL)
                        self.file_list = Listbox(savedfileframe, yscrollcommand=y_scroll.set)
                        y_scroll.place(x=1497, y=160, height=505)
                        y_scroll.config(command=self.file_list.yview)
                        self.file_list.place(x=1129, y=160, height=502, width=369)
                        self.file_list.bind("<ButtonRelease-1>", self.get_file)
                        self.show_data()

                        submissionframe = Frame(self.root, bd=9, relief=GROOVE, bg="silver").place(x=0, y=675,
                                                                                                   height=100,
                                                                                                   width=1520)

                        backbutton = Button(submissionframe, text="Quit", height=3, width=25, command=self.lastexit)
                        backbutton.place(x=1290, y=700)

                        resetbutton = Button(submissionframe, text="Reset", width=25, height=3, command=self.reset)
                        resetbutton.place(x=490, y=700)

                        logoutbutton = Button(submissionframe, text="Logout", width=25, height=3, command=self.logout)
                        logoutbutton.place(x=890, y=700)

                        submitbutton = Button(submissionframe, text="Submit", width=25, height=3,
                                              command=self.saved_file)
                        submitbutton.place(x=90, y=700)

                    def reset(self):
                        """
                        this function is used for resetting existing data
                        """
                        self.id.set("")
                        self.name.set("")
                        self.age.set("")
                        self.address.set("")
                        self.contact.set("")
                        self.department.set("")
                        self.dob.set("")
                        self.dname.set("")
                        self.dcode.set("")

                        self.root.mainloop()
                        self.show_data()

                    def saved_file(self):
                        """
                        this function is used to declare how data should be saved
                        """
                        length2 = len(self.contact.get())
                        if self.id.get() == "":
                            messagebox.showerror("ERROR", "Employee id needed")
                        elif self.name.get() == "":
                            messagebox.showerror("ERROR", "Employee name needed")
                        elif (self.age.get()) == "":
                            messagebox.showerror("ERROR", "Employee age needed")
                        elif (self.address.get()) == "":
                            messagebox.showerror("ERROR", "Employee address needed")
                        elif (self.contact.get()) == "":
                            messagebox.showerror("ERROR", "Employee contact needed")
                        elif length2 != 10:
                            message = messagebox.showerror("ERROR", "contact no must be 10 digit")
                            raise Exception(message)
                        elif (self.department.get()) == "":
                            messagebox.showerror("ERROR", "Employee worked department needed")
                        elif (self.dob.get()) == "":
                            messagebox.showerror("ERROR", "Employee date of birth needed")
                        elif (self.dname.get()) == "":
                            messagebox.showerror("ERROR", "Department name needed")
                        elif (self.contact.get()) == "":
                            messagebox.showerror("ERROR", "Department code needed")
                        else:
                            f = open("mero_file/" + str(self.id.get()) + str(self.name.get()) + ".txt", "w")
                            f.write(
                                str(self.id.get()) + " , " +
                                str(self.name.get()) + " , " +
                                str(self.age.get()) + " , " +
                                str(self.address.get()) + " , " +
                                str(self.contact.get()) + " , " +
                                str(self.department.get()) + " , " +
                                str(self.dob.get()) + " , " +
                                str(self.dname.get()) + " , " +
                                str(self.dcode.get())
                            )
                            f.close()
                            messagebox.showinfo("successful", "Your record has been saved")
                            self.show_data()

                    def show_data(self):
                        """
                        this function is used to declare where data should be saved
                        """
                        files = os.listdir("mero_file/")
                        if len(files) > 0:
                            self.file_list.delete(0, END)
                            for i in files:
                                self.file_list.insert(END, i)

                    def get_file(self, ev):
                        get_cursor = self.file_list.curselection()
                        fi1 = open("mero_file/" + self.file_list.get(get_cursor))
                        value = []
                        for f in fi1:
                            value = f.split(",")

                            self.id.set(value[0])
                            self.name.set(value[1])
                            self.age.set(value[2])
                            self.address.set(value[3])
                            self.contact.set(value[4])
                            self.department.set(value[5])
                            self.dob.set(value[6])
                            self.dname.set(value[7])
                            self.dcode.set(value[8])

                    def lastexit(self):
                        """
                        this function is used to exit the selected frame

                        """
                        last = messagebox.askyesno("BACK", "Do you really wanna exit?")
                        if last > 0:
                            self.root.destroy()
                        else:
                            return

                    def logout(self):
                        """
                        this function is used for logging out your id

                        """
                        self.root.destroy()
                        main_frame()

                root = Tk()
                ob = login_file(root)
                root.mainloop()

            else:
                messagebox.showerror("ERROR", "Password did not matched")
        else:
            messagebox.showerror("ERROR", "User does not exist\nRegister first")

    def login(self):
        """
        this function contains all the label and entry box for logging in to employee and department form
        """
        global loginscreen
        loginscreen = Toplevel(frame)
        loginscreen.title("Login")
        loginscreen.geometry("1297x767+112+21")
        loginscreen.config(bg="silver")
        global username_verify
        global password_verify
        global loginusernameentry
        global loginpasswordentry

        username_verify = StringVar()
        password_verify = StringVar()

        F3 = Frame(loginscreen, bd=11, relief=GROOVE)
        F3.place(x=429, y=249, height=308, width=437)

        logintitle = Label(F3, text="Login page", font=("jester", 27, "bold"), fg="black")
        logintitle.place(x=70, y=10)

        loginusernamelabel = Label(F3, text="Username *", font=("jester", 19, "bold"), fg="black")
        loginusernamelabel.place(x=29, y=80)

        loginusernameentry = Entry(F3, width=30, textvariable=username_verify)
        loginusernameentry.place(x=180, y=90)

        loginpasswordlabel = Label(F3, text="Password *", font=("jester", 19, "bold"), fg="black")
        loginpasswordlabel.place(x=29, y=150)

        loginpasswordentry = Entry(F3, width=30, show=("*"), textvariable=password_verify)
        loginpasswordentry.place(x=180, y=160)

        submitbutton = Button(F3, text="Login", width=10, height=2, command=lambda:login.login_user(self))
        submitbutton.place(x=75, y=220)

        def back():
            """
           this function is used to exit the selected frame

            """

            loginscreen.destroy()

        backbutton = Button(F3, text="Back", width=10, height=2, command=back)
        backbutton.place(x=250, y=220)

class register:
    """
    this class is used to keep all the data that are being registered
    """
    def register_user(self):
        """
        this function is used to fetch the registered data

        """
        length = len(registerpasswordentry.get())
        length1=len(registerusernameentry.get())
        if length1 < 3:
            message = messagebox.showerror("Weak username", "Username must be 3 character or more")
            raise Exception(message)
        elif length < 8:
            message = messagebox.showerror("Weak password", "Password must be 8 character or more")
            raise Exception(message)
        else:
            username_information = self.username.get()
            password_information = self.password.get()

            file = open(username_information, "w")
            file.write(username_information + "\n")
            file.write(password_information)
            file.close()

            registerusernameentry.delete(0, END)
            registerpasswordentry.delete(0, END)

            messagebox.showinfo("SUCCESS","Registration successful")



    def register(self):
        """
        this function contains all the label and entry box of register page
        """
        global username
        global password
        global registerusernameentry
        global registerpasswordentry
        global registerscreen
        global F2

        self.username = StringVar()
        self.password = StringVar()

        registerscreen = Toplevel(frame)
        registerscreen.title("Register")
        registerscreen.geometry("1297x767+112+21")
        registerscreen.config(bg="silver")

        F2 = Frame(registerscreen, bd=11, relief=GROOVE)
        F2.place(x=429, y=249, height=308, width=437)

        registertitle = Label(F2, text="Register page", font=("jester", 27, "bold"), fg="black")
        registertitle.place(x=70, y=10)

        registerusername = Label(F2, text="Username *", font=("jester", 19, "bold"), fg="black")
        registerusername.place(x=29, y=80)

        registerusernameentry = Entry(F2, width=30, textvariable=self.username)
        registerusernameentry.place(x=180, y=90)

        registerpassword = Label(F2, text="Password *", font=("jester", 19, "bold"), fg="black")
        registerpassword.place(x=29, y=150)


        registerpasswordentry = Entry(F2, width=30, show=("*"), textvariable=self.password)
        registerpasswordentry.place(x=180, y=160)


        submitbutton = Button(F2, text="Submit", width=10, height=2, command=lambda:register.register_user(self))
        submitbutton.place(x=75, y=220)

        def back():
            registerscreen.destroy()

        backbutton = Button(F2, text="Back", width=10, height=2, command=back)
        backbutton.place(x=250, y=220)




def main_frame():
    """
    this function is used to open the first frame after running the programme
    """
    global frame
    frame=Tk()
    frame.title("GUI app")
    frame.config(bg="silver")
    frame.geometry("1297x767+112+21")

    F1 = Frame(frame, bd=11, relief=GROOVE)
    F1.place(x=429, y=249, height=308, width=437)

    heading = Label(F1, text="Employee Management System", font=("jester", 19, "bold"), fg="black")
    heading.place(x=17,y=11)

    heading1 = Label(F1, text="Select any option", fg="black")
    heading1.place(x=120, y=52)

    loginbutton = Button(F1, text="Login", width=20, height=3,command=lambda:login.login(frame))
    loginbutton.place(x=120,y=80)

    registerbutton = Button(F1, text="Register", width=20, height=3,command=lambda:register.register(frame))
    registerbutton.place(x=120, y=140)


    def exit():
        """
        this function is used to exit the selected frame

        """
        menu=messagebox.askyesno("BACK","do you really wanna exit?")
        if menu>0:
            frame.destroy()
        else:
            return

    exitbutton = Button(F1, text="Exit", width=20, height=3,command=exit)
    exitbutton.place(x=120, y=200)


    frame.mainloop()

main_frame()