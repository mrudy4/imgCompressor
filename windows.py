import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk

class ImageView:
    '''
    This class contains all the methods and contructors for Tkinter GUI
    '''
    def __init__(self, root, presenter):

        self.presenter = presenter
        self.root = root
        self.root.title("Image App")

        # Get the screen width and height
        # and set the window size to 720x480 pixels
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.root.geometry(f"720x480+{(screen_width // 2) - (720 // 2)}+{(screen_height // 2) - (480 // 2)}")
        self.root.resizable(False, False)


        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.load_button = tk.Button(root, text="Load Image", command=self.presenter.on_load_image)
        self.load_button.pack()

        self.gray_button = tk.Button(root, text="To Grayscale", command=self.presenter.on_convert_grayscale)
        self.gray_button.pack()

        self.compress_button = tk.Button(root, text="Compress Grayed (SVD)", command=self.presenter.on_compress_image)
        self.compress_button.pack()

        self.compress_button = tk.Button(root, text="Compress RGB (SVD)", command=self.presenter.on_compress_image_rgb)
        self.compress_button.pack()

        self.k_entry = tk.Entry(root)
        self.k_entry.insert(0, "50")
        self.k_entry.pack()

    def choose_file(self):
        return filedialog.askopenfilename()

    def get_k_value(self):
        try:
            return int(self.k_entry.get())
        except ValueError:
            return 50

    def show_image(self, pil_image):
        img_tk = ImageTk.PhotoImage(pil_image)
        self.image_label.configure(image=img_tk)
        
        # prevent garbage collection
        self.image_label.image = img_tk 
