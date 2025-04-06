from functions import is_virtualenv
from presenter import ImagePresenter
import tkinter as tk

def main():
    print("/*** The main function is running ***/")
    if is_virtualenv():
        print("Running in a virtual environment")
    else:
        print("Not running in a virtual environment")

    root = tk.Tk()
    app = ImagePresenter(root)
    root.mainloop()


    print("/*** Exiting the main function ***/")

if __name__ == "__main__":
    main()