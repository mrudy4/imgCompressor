import numpy as np
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageModel:
    def __init__(self):
        self.image = None
        self.grayed_image = None
        self.compressed_image = None
        self.compressed_image_rgb = None

    def load_image(self, path):
        try:
            self.image = Image.open(path).convert('RGB')
            return self.image
        except Exception as e:
            print(f"Error loading image: {e}")
            return False

    def convert_to_grayscale(self):
        try:
            self.gray_image = self.image.convert('L')
            return self.gray_image
        except Exception as e:
            print(f"Error during grayscale conversion: {e}")
            return False

    
    def compress_image_svd(self, k):
        try :
            image_array = np.array(self.gray_image)

            # Perform SVD on the image array
            U, S, Vt = np.linalg.svd(image_array, full_matrices=False)

            # Keep only the first k singular values and corresponding vectors
            compressed = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vt[:k, :]))

            # Normalize the compressed image to the range [0, 255]
            compressed_image = Image.fromarray(np.clip(compressed, 0, 255).astype('uint8'))

            self.compressed_image = compressed_image

            return self.compressed_image
        except Exception as e:
            print(f"Error during compression: {e}")
            return False
    
    def compress_image_svd_rgb(self, k):
        try:
            image_array = np.array(self.image)
            
            # seperate channels
            # Perform SVD on each channel separately
            compressed_channels = []
            for i in range(3):  # R, G, B
                channel = image_array[:, :, i]
                U, S, Vt = np.linalg.svd(channel, full_matrices=False)
                compressed = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vt[:k, :]))
                compressed = np.clip(compressed, 0, 255)
                compressed_channels.append(compressed.astype(np.uint8))

            # combine the compressed channels back into an RGB image
            compressed_rgb = np.stack(compressed_channels, axis=2)
            self.compressed_image_rgb = Image.fromarray(compressed_rgb)
            return self.compressed_image_rgb
        except Exception as e:
            print(f"Error during RGB compression: {e}")
            return False
