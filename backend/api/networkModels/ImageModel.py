import time
# import keras_cv
from tensorflow import keras


class ImageModel:
    def __init__(self):
        self.model = None
        self.image = None

    def generate(self, description):
        # self.model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)
        self.image = self.model.text_to_image(description, batch_size=3)
        return self.image
