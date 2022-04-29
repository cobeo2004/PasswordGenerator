#Modules
import sqlite3
import tkinter
from tkinter import ttk, messagebox
from src.Database.DBFunc import addDataToDatabase
from src.UI._fun import delete_everything_from_path, read_from_path
#MARK: __userName: str, __savedPassword: str, __firstName: str = "", __lastName: str = "", __email: str, __website: str = "", __application: str = ""

#UISetPassword class, the UI for setting the password
class UISetPassword(tkinter.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.password = read_from_path()

        self.title("Database Setter")
        self.geometry("1024x768")
        self.iconbitmap("./src/img/key.ico")

        self.userName_label = tkinter.LabelFrame(self, text="Your User Name(*):")
        self.userName_label.pack(pady=20)
        self.userName_entry = tkinter.Entry(self.userName_label, font=("Helvetica", 18))
        self.userName_entry.pack(padx=5,pady=5)

        self.email_label = tkinter.LabelFrame(self, text="Your Email(*):")
        self.email_label.pack(pady=20)
        self.email_entry = tkinter.Entry(self.email_label, font=("Helvetica", 18))
        self.email_entry.pack(padx=5,pady=5)

        self.firstName_label = tkinter.LabelFrame(self, text="Your First Name(*):")
        self.firstName_label.pack(pady=20)
        self.firstName_entry = tkinter.Entry(self.firstName_label, font=("Helvetica", 18))
        self.firstName_entry.pack(padx=5,pady=5)

        self.lastName_label = tkinter.LabelFrame(self, text="Your Last Name:")
        self.lastName_label.pack(pady=20)
        self.lastName_entry = tkinter.Entry(self.lastName_label, font=("Helvetica", 18))
        self.lastName_entry.pack(padx=5,pady=5)

        self.website_label = tkinter.LabelFrame(self, text="Your Website that you wanted to save(*):")
        self.website_label.pack(pady=20)
        self.website_entry = tkinter.Entry(self.website_label, font=("Helvetica", 18))
        self.website_entry.pack(padx=5,pady=5)

        self.application_label = tkinter.LabelFrame(self, text="Your Application that you wanted to save(*):")
        self.application_label.pack(pady=20)
        self.application_entry = tkinter.Entry(self.application_label, font=("Helvetica", 18))
        self.application_entry.pack(padx=5,pady=5)

        self.btn_frame = ttk.Frame(self)
        self.btn_frame.pack(pady=20)

        self.submit_btn = ttk.Button(self.btn_frame, text="Save To Database", command=self._submit)
        self.submit_btn.grid(row=0,column=0, padx=5,pady=5)

        self.exit_btn = ttk.Button(self.btn_frame, text="Exit", command=self._exit)
        self.exit_btn.grid(row=0, column=1, padx=5, pady=5)

        self.notice = ttk.Label(self, text="""
                    Remember to fill the (*) or the requirements field, 
        if you don't want to save application, website or both, please put No on it!""")
        self.notice.pack(padx=5,pady=5)

        self.text_box = ttk.Label(self, text="Created by Simon Nguyen @2022", state="readonly")
        self.text_box.pack(padx=5,pady=5)

    #Submit to the database
    def _submit(self):
        conf = messagebox.askyesno("Confirmation", "Do you really wanted to save the data ?")
        if conf:
            if self.userName_entry.index("end") == 0:
                messagebox.showwarning("Empty Field", "Please Fill the Required Field!")
            else: 
                conf = messagebox.askokcancel("Confirmation", "Are you sure that you wanted to submit? (Remember to fill all of the required field or (*) field because it is very important for data saving purpose and also try to fill the information that is close to you in order to get your infos from database easier!) ")
                if conf:
                    try:
                        addDataToDatabase(self.userName_entry.get(), self.password, self.email_entry.get(), self.firstName_entry.get(), self.website_entry.get(), self.application_entry.get(), self.lastName_entry.get())
                        # print(f"{self.userName_entry.get()} {self.password} {self.email_entry.get()} {self.firstName_entry.get()} {self.website_entry.get()} {self.application_entry.get()} {self.lastName_entry.get()}")
                        messagebox.showinfo("Successful", "Successfully fetch the data")
                    except sqlite3.Error as e:
                        messagebox.showwarning("Error", f"Can't fetch the data, error: {e} ")
                        print(e)
                else:
                    messagebox.showwarning("Warning", "Think twice before doing something :D")
        else:
            messagebox.showinfo("Denied", "All right then !")
        
    #Exit
    def _exit(self):
        delete_everything_from_path()
        messagebox.showinfo("Exit", "Thanks for using my service ! - Simon Nguyen")
        self.destroy()


if __name__ == "__main__": UISetPassword().mainloop()