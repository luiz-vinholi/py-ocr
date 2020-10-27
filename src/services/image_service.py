import PIL as pillow
import numpy as np
import cv2


class ImageService:
    def __init__(self, image_src: str):
        image = pillow.Image.open(image_src).convert('RGB')
        image = np.asarray(image).astype(np.uint8)

        self._original_image = image
        self.treated_image = None

    @property
    def original_image(self):
        return pillow.Image.fromarray(self._original_image)

    def treat(self):
        image = cv2.detailEnhance(self._original_image, sigma_s=100, sigma_r=1)

        image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        thresh = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)[1]

        treated_image = pillow.Image.fromarray(thresh)
        treated_image.save('./src/images/treated-cpfl.jpeg')

        self.treated_image = treated_image

        return self

    def crop(self, areas: tuple):
        cropped_image = self._original_image.crop(areas)
        cropped_image.save('./src/images/cropped-cpfl.jpeg')
        return cropped_image
