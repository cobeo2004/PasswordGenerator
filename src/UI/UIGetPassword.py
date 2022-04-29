#Modules
from tkinter import ttk, messagebox
import tkinter
from src.Database.DBFunc import getFromDatabase

#UIGetPassword class, the UI for getting the password
class UIGetPassword(tkinter.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Database Getter")
        self.geometry("420x768")
        self.iconbitmap("./src/img/key.ico")

        self.userName_label = ttk.LabelFrame(self, text="Your User Name(*):")
        self.userName_label.pack(pady=10)
        self.userName_entry = ttk.Entry(self.userName_label, font=("Helvetica", 18))
        self.userName_entry.pack(padx=10,pady=10)

        self.email_label = ttk.LabelFrame(self, text="Your Email(*):")
        self.email_label.pack(pady=10)
        self.email_entry = ttk.Entry(self.email_label, font=("Helvetica", 18))
        self.email_entry.pack(padx=10,pady=10)

        self.firstName_label = ttk.LabelFrame(self, text="Your First Name(*):")
        self.firstName_label.pack(pady=10)
        self.firstName_entry = ttk.Entry(self.firstName_label, font=("Helvetica", 18))
        self.firstName_entry.pack(padx=10,pady=10)

        self.website_label = ttk.LabelFrame(self, text="Your Website that you saved(*):")
        self.website_label.pack(pady=10)
        self.website_entry = ttk.Entry(self.website_label, font=("Helvetica", 18))
        self.website_entry.pack(padx=10,pady=10)

        self.application_label = ttk.LabelFrame(self, text="Your Application that you saved(*):")
        self.application_label.pack(pady=10)
        self.application_entry = ttk.Entry(self.application_label, font=("Helvetica", 18))
        self.application_entry.pack(padx=10,pady=10)

        self.btn_frame = ttk.Frame(self)
        self.btn_frame.pack(pady=10)

        self.submit_btn = ttk.Button(self.btn_frame, text="Get From Database", command=self._submit)
        self.submit_btn.grid(row=0,column=0, padx=10,pady=10)

        self.exit_btn = ttk.Button(self.btn_frame, text="Exit", command=self._exit)
        self.exit_btn.grid(row=0, column=1, padx=10, pady=10)
        
        self.notice = ttk.Label(self, text="""
                    Remember to fill the (*) or the requirements field, 
        if you don't want to save application, website or both, please put No on it!""")
        self.notice.pack(padx=5,pady=5)

        self.text_box = ttk.Label(self, text="Created by Simon Nguyen @2022", state="readonly")
        self.text_box.pack(padx=10,pady=10)

    #Get data from the database and put it to the _UIShow class
    def _submit(self):
        if self.userName_entry.index("end") == "":
            messagebox.showwarning("Please fill in the indicated field")
        else:
            self.__list = getFromDatabase(
                self.userName_entry.get(), 
                self.firstName_entry.get(),
                self.email_entry.get(), 
                self.website_entry.get(), 
                self.application_entry.get()
            )
            print(self.__list)
            _SHOW = _UIShow(self.__list)
            _SHOW.mainloop()

    #Exit 
    def _exit(self):
        messagebox.showinfo("Exit", "Thanks for using my service ! - Simon Nguyen")
        self.destroy()


#UIShow class, the UI for showing the data
class _UIShow(tkinter.Tk):
    def __init__(self, __list:list) -> None:
        super().__init__()

        self.dt = __list

        self.title("Database Getter")
        self.iconbitmap("./src/img/key.ico")
        self.geometry("1024x1568")

        self.userName_label = ttk.LabelFrame(self, text="User Name:")
        self.userName_label.pack(pady=10)
        self.userName_entry = ttk.Entry(self.userName_label, font=("Helvetica", 18))
        self.userName_entry.insert(0,self.dt[0])
        self.userName_entry.pack(padx=10,pady=10)

        self.email_label = ttk.LabelFrame(self, text="Email:")
        self.email_label.pack(pady=10)
        self.email_entry = ttk.Entry(self.email_label, font=("Helvetica", 18))
        self.email_entry.insert(0, self.dt[4])
        self.email_entry.pack(padx=10,pady=10)

        self.firstName_label = ttk.LabelFrame(self, text="First Name:")
        self.firstName_label.pack(pady=10)
        self.firstName_entry = ttk.Entry(self.firstName_label, font=("Helvetica", 18))
        self.firstName_entry.pack(padx=10,pady=10)
        self.firstName_entry.insert(0, self.dt[1])
        
        self.lastName_label = ttk.LabelFrame(self, text="Last Name:")
        self.lastName_label.pack(pady=10)
        self.lastName_entry = ttk.Entry(self.lastName_label, font=("Helvetica", 18))
        self.lastName_entry.pack(padx=10,pady=10)
        self.lastName_entry.insert(0, self.dt[2])

        self.website_label = ttk.LabelFrame(self, text="Your Saved Website:")
        self.website_label.pack(pady=10)
        self.website_entry = ttk.Entry(self.website_label, font=("Helvetica", 18))
        self.website_entry.insert(0, self.dt[5])
        self.website_entry.pack(padx=10,pady=10)

        self.application_label = ttk.LabelFrame(self, text="Your Saved Application:")
        self.application_label.pack(pady=10)
        self.application_entry = ttk.Entry(self.application_label, font=("Helvetica", 18))
        self.application_entry.insert(0, self.dt[6])
        self.application_entry.pack(padx=10,pady=10)

        self.password_label = ttk.LabelFrame(self, text="Your Saved Password:")
        self.password_label.pack(pady=10)
        self.password_entry = ttk.Entry(self.password_label, font=('Helvetica',18))
        self.password_entry.insert(0, self.dt[3])
        self.password_entry.pack(padx=10, pady=10)

        self.btn_frame = ttk.Frame(self)
        self.btn_frame.pack(pady=10)

        self.copy_btn = ttk.Button(self.btn_frame, text="Copy Password", command=self._copy)
        self.copy_btn.grid(row=0,column=0,padx=10,pady=10)

        self.exit_btn = ttk.Button(self.btn_frame, text="Exit", command=self._exit)
        self.exit_btn.grid(row=0, column=1, padx=10, pady=10)

        self.text_box = ttk.Label(self, text="Created by Simon Nguyen @2022", state="readonly")
        self.text_box.pack(padx=10,pady=10)

    #Copy to the clipboard 
    def _copy(self):
        self.clipboard_clear()
        self.clipboard_append(self.dt[3])
        messagebox.showinfo("Password Copied", "Password copied to clipboard")

    #Exit
    def _exit(self):
        messagebox.showinfo("Exit", "Thanks for using my service ! - Simon Nguyen")
        self.destroy()


if __name__ == "__main__": UIGetPassword().mainloop()