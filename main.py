# import sys
# import os
# from src.PasswordGenerator.ProcessRandomPassword import RandomPassword

# def main() -> None:
#     while True:    
#         _length = int(input("Enter the length of the password: "))
#         sys.stdout.write("Your password is: " + RandomPassword(_length))
#         _choice = str(input("\nDo you want to save it to a text file? (y/n): "))
#         if _choice == "y":
#             _path = "./Saves/"
#             _file_name = "password.txt"
#             _save_reason = str(input("\nEnter the website or application name you intended to save: "))
#             if not os.path.exists(_path):
#                 os.makedirs(_path)
#                 sys.stdout.write("\nCreated directory: " + _path + "\n")
#             else:
#                 with open(_path + _file_name, "a+") as op:
#                     op.writelines(f"Password for {_save_reason}: {RandomPassword(_length)}\n")
#                     sys.stdout.write("\nSaved to: " + _path + _file_name + "\n")
#             _choice = str(input("\nDo you want to continue? (y/n): "))
#             if _choice == "y":
#                 continue
#             else:
#                 sys.stdout.flush()
#                 sys.stdout.write("Bye bye! ")
#                 break
#         elif _choice == "n":
#             sys.stdout.flush()
#             sys.stdout.write("Bye!")
#             break


from src.UI.UIMain import UIMain

if __name__ == "__main__":
    try:
        app = UIMain()
        app.mainloop()
    except KeyboardInterrupt:
        print("\nBye bye!")
        exit(1)