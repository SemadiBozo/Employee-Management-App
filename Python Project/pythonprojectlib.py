from tkinter import Label,Entry,Button,IntVar,PhotoImage,Spinbox,Menu,Toplevel,Listbox,Scrollbar,Frame,messagebox,StringVar,filedialog
from tkinter.ttk import Combobox,Checkbutton,Radiobutton,Style
import matplotlib.pyplot as plt
#----------Program's Form----------
class Program():
    def Start(self):
        font="Bahnschrift"
        #----------Form Body----------
        self.form1=Toplevel()
        self.form1.title("Organization")
        self.form1.geometry("900x700")
        self.form1.resizable(False,False)
        self.form1.iconbitmap("icon.ico")
        self.form1.configure(bg="Orange")
            #Making style for radiobutton and checkbutton orange background
        rbs=Style()
        rbs.configure("rbs.TRadiobutton",background="Orange",font=(font,13))
        chbs=Style()
        chbs.configure("chbs.TCheckbutton",background="Orange",font=(font,13,))
        #----------Organize Employee Section----------
        Label(self.form1,text="First Name:",font=(font,17,"bold"),bg="Orange").place(x=15,y=10)
        self.FirstNameEntry=Entry(self.form1,font=(font,17,"bold"),bd=3)
        self.FirstNameEntry.place(x=155,y=10)
        
        Label(self.form1,text="Last Name:",font=(font,17,"bold"),bg="Orange").place(x=440,y=10)
        self.LastNameEntry=Entry(self.form1,font=(font,17,"bold"),bd=3)
        self.LastNameEntry.place(x=580,y=10)
        
        delicon=PhotoImage(file="trash.png")
        Button(self.form1,image=delicon,command=self.DeleteEntries).place(x=860,y=13)
        
        Label(self.form1,text="Date of Birth:",font=(font,17,"bold"),bg="Orange").place(x=15,y=60)
        self.YearIntVar=IntVar()
        self.YearSpinBox=Spinbox(self.form1,from_=1950,to_=2005,textvariable=self.YearIntVar,width=5,font=(font,11))
        self.YearSpinBox.place(x=163,y=66)
        Label(self.form1,text="/",font=(font,13,"bold"),bg="Orange").place(x=218,y=64)
        self.MonthComboBox=Combobox(self.form1,state="readonly",width=8,font=(font,8),values=("","January","February","March","April","May","June","July","August","September","October","November","December"))
        self.MonthComboBox.place(x=233,y=67.5)
        self.MonthComboBox.current(0)
        Label(self.form1,text="/",font=(font,13,"bold"),bg="Orange").place(x=303,y=64)
        self.DayIntVar=IntVar()
        self.DaySpinBox=Spinbox(self.form1,from_=1,to_=31,textvariable=self.DayIntVar,width=2,font=(font,11))
        self.DaySpinBox.place(x=318,y=66)
        
        Label(self.form1,text="Code:",font=(font,17,"bold"),bg="Orange").place(x=352,y=60)
        self.CodeEntry=Entry(self.form1,font=(font,17,"bold"),bd=3,width=15)
        self.CodeEntry.place(x=420,y=60)
        
        Label(self.form1,text="Salary:",font=(font,17,"bold"),bg="Orange").place(x=630,y=60)
        self.SalaryStringVar=StringVar()
        self.SalaryEntry=Entry(self.form1,font=(font,17,"bold"),textvariable=self.SalaryStringVar,bd=3,width=12)
        self.SalaryEntry.place(x=715,y=60)
        self.SalaryStringVar.trace_add("write",self.SalaryFormat)
        
        Label(self.form1,text="Gender:",font=(font,17,"bold"),bg="Orange").place(x=15,y=110)
        self.GenderIntVar=IntVar()
        self.MaleRadioButton=Radiobutton(self.form1,text="Male",variable=self.GenderIntVar,value=1,style="rbs.TRadiobutton")
        self.MaleRadioButton.place(x=120,y=116)
        self.FemaleRadioButton=Radiobutton(self.form1,text="Female",variable=self.GenderIntVar,value=2,style="rbs.TRadiobutton")
        self.FemaleRadioButton.place(x=190,y=116)
        
        Label(self.form1,text="Languages:",font=(font,17,"bold"),bg="Orange").place(x=15,y=160)
        self.PersianIntVar=IntVar(value=1)
        self.PersianCheckBox=Checkbutton(self.form1,text="Persian",variable=self.PersianIntVar,style="chbs.TCheckbutton")
        self.PersianCheckBox.place(x=140,y=166)
        self.EnglishIntVar=IntVar()
        self.EnglishCheckBox=Checkbutton(self.form1,text="English",variable=self.EnglishIntVar,style="chbs.TCheckbutton")
        self.EnglishCheckBox.place(x=225,y=166)
        
        Button(self.form1,font=(font,17,"bold"),text="Add",width=9,height=2,command=self.Add).place(x=320,y=120)
        Button(self.form1,font=(font,17,"bold"),text="Delete",width=9,height=2,command=self.DeleteEmployee).place(x=460,y=120)
        Button(self.form1,font=(font,17,"bold"),text="Edit",width=9,height=2,command=self.Edit).place(x=600,y=120)
        Button(self.form1,font=(font,17,"bold"),text="Search",width=9,height=2,command=self.Search).place(x=740,y=120)
        #-----------Employee List----------
        frame2=Frame(self.form1)
        frame2.place(x=15,y=215)
        
        self.EmployeesListBox=Listbox(frame2,selectmode="SINGLE",font=(font,12),height=17,width=94)
        self.EmployeesListBox.pack(side="left",fill="y")
        
        self.ScrollY=Scrollbar(frame2,orient="vertical")
        self.ScrollY.config(command=self.EmployeesListBox.yview)
        self.ScrollY.pack(side="right",fill="y")
        #----------Average----------
        Button(self.form1,font=(font,17,"bold"),text="Salary Average",width=32,height=2,command=self.SalaryAverage).place(x=15,y=580)
        #----------Chart----------
        Button(self.form1,font=(font,17,"bold"),text="Salary Chart",width=32,height=2,command=self.SalaryChart).place(x=460,y=580)
        #----------Form Menu----------
        men=Menu(self.form1)
        
        men_file=Menu(men,tearoff=0)
        men.add_cascade(label="File",menu=men_file)
        men_file.add_command(label="New File",command=self.NewFile)
        men_file.add_command(label="Open",command=self.Open)
        men_file.add_separator()
        men_file.add_command(label="Save",command=self.Save)
        men_file.add_command(label="Save As",command=self.SaveAs)
        men_file.add_separator()
        men_file.add_command(label="Exit",command=self.form1.destroy)
        
        men_help=Menu(men,tearoff=0)
        men.add_cascade(label="Help",menu=men_help)
        men_help.add_command(label="About",command=self.About)
        
        self.form1.config(menu=men)
        self.form1.mainloop()
    def SalaryFormat(self,name,index,mode): #Making a number like 14000 be 14,000
        Salary=self.SalaryStringVar.get()
        Salary="".join(filter(str.isdigit,Salary))
        if Salary:
            Salary="{:,}".format(int(Salary))
        self.SalaryStringVar.set(Salary)
    def NewFile(self): #Making a new form and destroy the old one
        self.form1.destroy()
        self.Start()
    def Open(self): #Openning an existed text-based database
        DBPath=filedialog.askopenfilename()
        if DBPath:
            with open(DBPath,"r",encoding="utf-8") as db:
                dbcontent=db.read().splitlines()
                db.close()
            self.EmployeesListBox.delete(0,"end")
            for item in dbcontent:
                self.EmployeesListBox.insert("end",item)
    def Save(self): #Save the current changes
        DBPath=filedialog.asksaveasfilename()
        with open(DBPath,"a",encoding="utf-8") as db:
            for item in self.EmployeesListBox.get(0,"end"):
                db.write(item+"\n")
            db.close()
    def SaveAs(self): #Save and overwrite current changes
        DBPath=filedialog.asksaveasfilename()
        with open(DBPath,"w",encoding="utf-8") as db:
            for item in self.EmployeesListBox.get(0,"end"):
                db.write(item+"\n")
            db.close()
    def About(self): #About software
        messagebox.showinfo(title="About",message="Organization Program written in python by Seyed Mahdi Mousavi Nezhad student of Mrs.Isavandi")
    def DeleteEntries(self): #Removing given datas in fields
        self.FirstNameEntry.delete(0,"end")
        self.LastNameEntry.delete(0,"end")
        self.YearIntVar.set(1950)
        self.MonthComboBox.current(0)
        self.DayIntVar.set(1)
        self.CodeEntry.delete(0,"end")
        self.SalaryEntry.delete(0,"end")
        self.GenderIntVar.set(3)
        self.PersianIntVar.set(0)
        self.EnglishIntVar.set(0)
    def Add(self): #Add to list
        if not self.FirstNameEntry.get():
            messagebox.showerror(title="Required Data Not Found",message="Please fill the first name field.")
            return
        else:
            FirstName=self.FirstNameEntry.get()
        if not self.LastNameEntry.get():
            messagebox.showerror(title="Required Data Not Found",message="Please fill the last name field.")
            return
        else:
            LastName=self.LastNameEntry.get()
        DateOfBirth=self.YearSpinBox.get()+"/"+self.MonthComboBox.get()+"/"+self.DaySpinBox.get()
        if not self.CodeEntry.get():
            messagebox.showerror(title="Required Data Not Found",message="Please fill the code field.")
            return
        else:
            Code=self.CodeEntry.get()
        if not self.SalaryEntry.get():
            messagebox.showerror(title="Required Data Not Found",message="Please fill the salary field.")
            return
        else:
            Salary=self.SalaryEntry.get()
        if self.GenderIntVar.get()==1:
            Gender="Male"
        elif self.GenderIntVar.get()==2:
            Gender="Female"
        else:
            messagebox.showerror(title="Required Data Not Found",message="Please select your gender.")
            return
        languages=[]
        if self.PersianIntVar.get()==1:
            languages.append("Persian")
        if self.EnglishIntVar.get()==1:
            languages.append("English")
        if not languages:
            messagebox.showerror(title="Required Data Not Found",message="Please select at least one known language.")
            return
        Language=", ".join(languages)
        self.EmployeesListBox.insert(0,f"{FirstName} {LastName} {DateOfBirth} {Gender} Code:{Code} Salary:{Salary} Languages:{Language}")
    def DeleteEmployee(self): #Delete from list
        Selected=self.EmployeesListBox.curselection()
        if Selected and messagebox.askyesno(title="Confirmation",message="Are you sure you want to delete the selected employee?")==False:
            return
        if Selected:
            self.EmployeesListBox.delete(Selected)
        else:
            messagebox.showerror(title="Nothing Selected",message="Please select an employee to delete.")
    def Edit(self): #Edit employee
        self.SelectedEmployee=self.EmployeesListBox.curselection()
        if self.SelectedEmployee:
            SelectedItem=self.EmployeesListBox.get(self.SelectedEmployee[0])
            self.EditWindow=Toplevel(self.form1)
            self.EditWindow.title("Edit Employee")
            self.EditWindow.geometry("400x100")
            Label(self.EditWindow,text="Edit Employee:",font=("Bahnschrift",17,"bold")).pack()
            self.EditEntry=Entry(self.EditWindow,font=("Bahnschrift",12,"bold"),width=40,bd=3)
            self.EditEntry.insert(0,SelectedItem)
            self.EditEntry.pack()
            Button(self.EditWindow,text="Save",font=("Bahnschrift",15,"bold"),command=self.SaveEdit).pack()
        else:
            messagebox.showerror(title="Nothing Selected",message="Please select an employee to edit.")
    def SaveEdit(self): #Save employee changes
        if self.EditEntry:
            Answer=messagebox.askyesno(title="Confirmation",message="Are you sure you want to make this changes? (NOTE: Make sure what you changed didn't damage program's structure!)")
            if Answer==True:
                self.EmployeesListBox.delete(self.SelectedEmployee)
                self.EmployeesListBox.insert(self.SelectedEmployee,self.EditEntry.get())
                self.EditWindow.destroy()
    def Search(self): #Search for an employee
        self.Searched=[]
        if self.FirstNameEntry.get():
            self.Searched.append(self.FirstNameEntry.get())
        if self.LastNameEntry.get():
            self.Searched.append(self.LastNameEntry.get())
        if self.CodeEntry.get():
            self.Searched.append(f"Code:{self.CodeEntry.get()}")
        if self.SalaryEntry.get():
            self.Searched.append(f"Salary:{self.SalaryEntry.get()}")
        if self.GenderIntVar.get()==1:
            self.Searched.append("Male")
        elif self.GenderIntVar.get()==2:
            self.Searched.append("Female")
        languages=[]
        if self.PersianIntVar.get()==1:
            languages.append("Persian")
        if self.EnglishIntVar.get()==1:
            languages.append("English")
        if languages:
            self.Searched.append(f"Languages:{", ".join(languages)}")
        if self.Searched:
            for i in range(self.EmployeesListBox.size()):
                item=self.EmployeesListBox.get(i)
                if all(values in item for values in self.Searched):
                    self.EmployeesListBox.select_clear(0,"end")
                    self.EmployeesListBox.selection_set(i)
                    self.EmployeesListBox.see(i)
                    break
                else:
                    self.EmployeesListBox.select_clear(0,"end")
    def SalaryAverage(self): #Average salary calculator
        Salaries=[]
        for i in range(self.EmployeesListBox.size()):
            item=self.EmployeesListBox.get(i)
            Salary=item[item.find("Salary:")+len("Salary:"):item.find("Languages")]
            Salary=Salary.replace(",","")
            Salaries.append(int(Salary))
        if not Salaries:
            messagebox.showerror(title="Nothing Found",message="Please add at least one employee.")
            return
        Sum=0
        for i in Salaries:
            Sum+=i
        Average=Sum/len(Salaries)
        messagebox.showinfo(title="Employees Average Salary",message="The Average Salary: {:,}".format(int(Average)))
    def SalaryChart(self): #Making a chart for employees
        Salaries=[]
        Employees=[]
        for i in range(self.EmployeesListBox.size()):
            item=self.EmployeesListBox.get(i)
            Salary=item[item.find("Salary:")+len("Salary:"):item.find("Languages")]
            Salary=Salary.replace(",","")
            Salaries.append(int(Salary))
            Employee=f"{item.split()[0]} {item.split()[1]}"
            Employees.append(Employee)
        if Salaries and Employee:
            pass
        else:
            messagebox.showerror(title="Nothing Found",message="Please add at least one employee.")
            return
        plt.figure(figsize=(10,6))
        plt.bar(Employees,Salaries,color="green",width=0.3)
        for i in range(len(Employees)):
            plt.text(i,(Salaries[i])/2,"{:,}".format(int(Salaries[i])),ha="center")
        plt.xlabel("Employees",color="red")
        plt.ylabel("Salary",color="red")
        plt.title("Salary Chart")
        plt.ticklabel_format(style="plain",axis="y")
        plt.show()
