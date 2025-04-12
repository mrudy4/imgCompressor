import unittest
from model import ImageModel
from PIL import Image


class TestLoadImage(unittest.TestCase):
    def setUp(self):
        self.model = ImageModel()

    def test_load_image_success(self):
        # Test loading a valid image
        self.assertEqual(self.model.load_image('photos\photo1.jpg'), self.model.image)


    def test_load_image_failure(self):
        # Test loading a non-existent image
        self.assertFalse(self.model.load_image('photos\invalid_image.jpg'))

class TestConvertToGrayscale(unittest.TestCase):
    def setUp(self):
        self.model = ImageModel()
        self.model.load_image('photos\photo1.jpg')

    def test_convert_to_grayscale_success(self):
        # Test converting to grayscale
        self.assertEqual(self.model.convert_to_grayscale(), self.model.gray_image)

    def test_convert_to_grayscale_failure(self):
        # Test converting to grayscale without loading an image
        model = ImageModel()
        self.assertFalse(model.convert_to_grayscale())

if __name__ == '__main__':
    unittest.main()
