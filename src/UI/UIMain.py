#import all neccessary modules
import tkinter
from tkinter import BooleanVar, ttk
import tkinter.messagebox
from src.PasswordGenerator.ProcessRandomPassword import RandomPassword
from src.UI.UISetPassword import UISetPassword
from src.UI.UIGetPassword import UIGetPassword
from src.UI._fun import save_to_txt, delete_everything_from_path

#UIMain Class, the main class of the UI, where contains all of the UI components and also a password generator as well
class UIMain(tkinter.Tk):
    def __init__(self) -> None:

        delete_everything_from_path()
        super().__init__()
        self.isNumber = BooleanVar()
        self.isUpperCase = BooleanVar()
        self.isLowerCase = BooleanVar()
        self.isSymbol = BooleanVar()
        self.password = ""

        self.title("Password Generator")
        self.iconbitmap("./src/img/key.ico")
        self.geometry("700x450")
        self.resizable(True, True)

        self.options_frame = ttk.LabelFrame(self, text="Options")
        self.options_frame.pack(pady=10)

        self.optionsWithNumbers = ttk.Checkbutton(self.options_frame, text="Numbers", variable=self.isNumber)
        self.optionsWithNumbers.grid(row=0, column=0, sticky="w")

        self.optionsWithLowercase = ttk.Checkbutton(self.options_frame, text="Lowercase", variable=self.isLowerCase)
        self.optionsWithLowercase.grid(row=0, column=1, sticky="w")

        self.optionsWithUppercase = ttk.Checkbutton(self.options_frame, text="Uppercase", variable=self.isUpperCase)
        self.optionsWithUppercase.grid(row=0, column=2, sticky="w")

        self.optionsWithSymbols = ttk.Checkbutton(self.options_frame, text="Symbols", variable=self.isSymbol)
        self.optionsWithSymbols.grid(row=0, column=3, sticky="w")

        self.char_label = ttk.LabelFrame(self, text="How many characters?")
        self.char_label.pack(pady=20)

        self.char_label_entry = ttk.Entry(self.char_label, font=("Helvetica", 24))
        self.char_label_entry.pack(padx=20,pady=20)

        self.password = ttk.LabelFrame(self, text="Your password:")	
        self.password.pack(pady=20)

        self.password_entry = ttk.Entry(self.password, font=("Helvetica", 24))
        self.password_entry.pack(padx=10)

        self.btn_frame = ttk.Frame(self)
        self.btn_frame.pack(pady=20)

        self.password_button = ttk.Button(self.btn_frame, text="Generate Password", command=self._password_generator)
        self.password_button.grid(row=0, column=0, padx=10, pady=10)

        self.copy_button = ttk.Button(self.btn_frame, text="Copy Password", command = self._copy_password)
        self.copy_button.grid(row=0, column=1, padx=10, pady=10)

        self.save_to_db_btn = ttk.Button(self.btn_frame, text="Save to Database", command=self._save_to_db)
        self.save_to_db_btn.grid(row=0, column=2, padx=10, pady=10)

        self.get_from_db_btn = ttk.Button(self.btn_frame, text="Get from Database", command=self._get_from_db)
        self.get_from_db_btn.grid(row=0, column=3, padx=10, pady=10)

        self.text_box = ttk.Label(self, text="Created by Simon Nguyen @2022", state="readonly")
        self.text_box.pack(padx=10,pady=10)

    #Call the password generator and set the password to the entry
    def _password_generator(self):
        if not(self.isLowerCase.get() or self.isUpperCase.get() or self.isSymbol.get() or self.isNumber.get()):
            tkinter.messagebox.showwarning("Warning", "Please select at least one option")

        else:
            if self.char_label_entry.get() == "":
                self.password_entry.delete(0, tkinter.END)
                tkinter.messagebox.showwarning("Warning", "Please enter the intended characters")
            else:
                self.password_entry.delete(0, tkinter.END)
                _length = int(self.char_label_entry.get())
                _password = RandomPassword(_length)
                self.password = _password.WithAllCases(self.isLowerCase.get(),self.isUpperCase.get(), self.isNumber.get(), self.isSymbol.get())
                self.password_entry.insert(0,self.password)
                save_to_txt(self.password)

    #Copy the password to the clipboard
    def _copy_password(self) -> None:
        if self.password_entry.get() == "":
            tkinter.messagebox.showwarning("Warning", "Please generate a password first")
        else:
            self.clipboard_clear()
            self.clipboard_append(self.password_entry.get())
            tkinter.messagebox.showinfo("Password Copied", "Password copied to clipboard")

    #Save the password to the database 
    def _save_to_db(self) -> None:
        _response = tkinter.messagebox.askyesno("Save to Database", "Do you want to save this password to the database?")
        if _response:
            if self.password_entry.get() == "":
                tkinter.messagebox.showwarning("Warning", "Please generate a password first")
            else:
                _DB_SETPASS = UISetPassword()
                _DB_SETPASS.mainloop()
        else:
            tkinter.messagebox.showinfo("Not Saved", "Password not saved to database")
    
    #Get the password from the database
    def _get_from_db(self) -> None:
        # tkinter.messagebox.showinfo("Not Implemented", "This feature is not implemented yet")
        _response = tkinter.messagebox.askyesno("Get from Database", "Do you want to get your password from the database?")

        if _response:
            _DB_GETPASS = UIGetPassword()
            _DB_GETPASS.mainloop()
        else:
            tkinter.messagebox.showinfo("Not Retrieved", "Password not retrieved from database")
            



