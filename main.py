from src.UI.UIMain import UIMain

if __name__ == "__main__":
    try:
        app = UIMain()
        app.mainloop()
    except KeyboardInterrupt:
        print("\nBye bye!")
        exit(1)
