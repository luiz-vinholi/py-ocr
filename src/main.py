import pytesseract as tesseract
import numpy
import cv2

from PIL import Image


def treat_image() -> Image:
  image = Image.open('./ocr/images/cpfl.jpeg').convert('RGB')
  image = numpy.asarray(image).astype(numpy.uint8)
  image = cv2.detailEnhance(image, sigma_s=100, sigma_r=1)

  image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
  ret, thresh = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)
  
  treated_image = Image.fromarray(thresh)
  treated_image.save('./ocr/images/treated-cpfl.jpeg')

  return treated_image


def main():
  image = treat_image()

  response: str = tesseract.image_to_string(
    image,
    lang='por',
  )

  print(response)


if __name__ == '__main__':
  main()