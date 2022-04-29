from src.UI.UIMain import UIMain

if __name__ == "__main__":
    try:
        #Executing the main UI class
        app = UIMain()
        app.mainloop()
    except KeyboardInterrupt:
        #Exit if have any keyboard interruptions
        print("\nBye bye!")
        exit(1)
