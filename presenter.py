# presenter.py
from model import ImageModel
from windows import ImageView
from tkinter import messagebox

class ImagePresenter:
    '''
    This class acts as the presenter in the MVP (Model-View-Presenter) pattern.
    It connects the model (ImageModel) and the view (ImageView).
    It handles user interactions and updates the view based on model changes.
    '''
    def __init__(self, root):
        self.model = ImageModel()
        self.view = ImageView(root, self)

    def on_load_image(self):
        path = self.view.choose_file()
        if path:
            image = self.model.load_image(path)
            messagebox.showinfo("Check out!", "The image is loaded successfully!")
            self.view.show_image(image.resize((300, 300)))  # Resize for display
        else:
            messagebox.showerror("Error", "Failed to load image. Please try again.")

    def on_convert_grayscale(self):
        gray = self.model.convert_to_grayscale()
        if gray:
            messagebox.showinfo("Check out!", "The image is converted to grayscale successfully!")
            self.view.show_image(gray.resize((300, 300)))  # Resize for display
        else:
            messagebox.showerror("Error", "Conversion to grayscale failed. Please load an image first.")

    def on_compress_image(self):
        k = self.view.get_k_value()
        compressed = self.model.compress_image_svd(k)
        if compressed:
            messagebox.showinfo("Check out!", "The image is compressed successfully!")
            self.view.show_image(compressed.resize((300, 300)))  # Resize for display
        else:
            messagebox.showerror("Error", "Compression failed. Please check the image format or try a different value for k.")

    def on_compress_image_rgb(self):
        k = self.view.get_k_value()
        compressed = self.model.compress_image_svd_rgb(k)
        if compressed:
            messagebox.showinfo("Check out!", "The image is compressed successfully!")
            self.view.show_image(compressed.resize((300, 300)))  # Resize for display
        else:
            messagebox.showerror("Error", "Compression failed. Please check the image format or try a different value for k.")